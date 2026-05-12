"""cdv1 chit reading on voice coil linear actuator substrate data.

For a voice coil linear actuator (coil + magnet + flexure + load), the
substrate's mechanical exchange surface is the second-order damped oscillator:

    m·ẍ + c·ẋ + k·x = (BL)·i(t)

Substrate-conditional parameters: m (moving mass), c (damping coefficient),
k (suspension stiffness), R (coil resistance), L_e (coil inductance), BL
(force constant = magnetic flux density × coil length).

Substrate-structural Q-factor and regime classification:

    ω₀ = √(k/m)                  natural frequency
    ζ  = c / (2·√(m·k))          damping ratio
    Q  = 1 / (2·ζ) = ω₀ / (2γ)   quality factor

    Q > 0.5  → c (underdamped, oscillatory recovery)
    Q = 0.5  → s (critically damped, fastest non-oscillatory recovery)
    Q < 0.5  → r (overdamped, sluggish)

Note: Q is a *structural* parameter (substrate property), not an
operating-point order parameter. chit is the operating-point order parameter.
At steady-state sinusoidal drive at ω₀, the substrate sits at chit ≈ 0 by
power balance (G₀ = L_total) — the SOC attractor for sustained NESS.

Multimodal substrates (e.g., HDD VCM with 16 modes) carry one Q per mode.
Each mode is its own cdv1 oscillator instance.
"""
from __future__ import annotations

import json
import math
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass(frozen=True)
class ActuatorMode:
    """One mode of a voice coil actuator.

    Single-mode lumped actuators (e.g., MDPI 2020 cantilever VCA) have one
    entry. Multimodal actuators (e.g., PyHDDBenchmark VCM with 16 modes)
    have N entries.
    """
    index: int
    omega_radps: float
    zeta: float
    Q: Optional[float]   # None for rigid-body mode (ζ = 0, ω = 0)
    regime: str          # "c" | "s" | "r" | "rigid_body"
    kappa_residue: Optional[float] = None  # Modal residue (multimodal only)
    notes: Optional[str] = None


@dataclass(frozen=True)
class Actuator:
    """A voice coil actuator characterization, single-mode or multimodal."""
    substrate_id: str
    substrate_class_variant: str
    modes: tuple[ActuatorMode, ...]
    structural_parameters: dict
    source_citation: str


def compute_Q(omega_radps: float, zeta: float) -> Optional[float]:
    """Quality factor from natural frequency and damping ratio.

    Returns None for rigid-body mode (ω = 0 or ζ = 0).
    """
    if zeta <= 0.0 or omega_radps <= 0.0:
        return None
    return 1.0 / (2.0 * zeta)


def compute_omega(stiffness_npm: float, mass_kg: float) -> float:
    """Natural frequency of a single-mode mass-spring system."""
    return math.sqrt(stiffness_npm / mass_kg)


def compute_zeta(damping_nspm: float, mass_kg: float, stiffness_npm: float) -> float:
    """Damping ratio of a single-mode mass-spring-damper."""
    return damping_nspm / (2.0 * math.sqrt(mass_kg * stiffness_npm))


def regime_from_Q(Q: Optional[float], s_band: float = 0.02) -> str:
    """Classify substrate regime from quality factor.

    s_band: half-width around Q = 0.5 counted as s-boundary. Default 0.02 →
    Q ∈ [0.48, 0.52] is s. Outside that, c for Q > 0.5, r for Q < 0.5.
    """
    if Q is None:
        return "rigid_body"
    if abs(Q - 0.5) <= s_band:
        return "s"
    if Q > 0.5:
        return "c"
    return "r"


def chit_max_predicted(eta_electromechanical_max: float) -> float:
    """F-001 prediction: chit_max ≈ -ln(1 - η).

    For an actuator, η is the electromechanical conversion efficiency
    (mechanical work delivered to load / electrical power consumed). For
    high-quality voice coil actuators η can reach 0.3–0.8; for HDD VCMs
    operated near saturation it's lower.
    """
    if not (0.0 < eta_electromechanical_max < 1.0):
        raise ValueError("efficiency must be in (0, 1)")
    return -math.log(1.0 - eta_electromechanical_max)


def gamma_decay_rate(omega_radps: float, Q: float) -> float:
    """Exponential decay rate γ in e^(-γt) for a damped oscillator.

    γ = ω₀ / (2Q). At Q = 0.5, γ = ω₀ (critical). At Q > 0.5, γ < ω₀
    (underdamped, slower decay). At Q < 0.5, the actual decay involves two
    real exponentials with rates γ ± √(γ² - ω₀²); this function returns the
    γ value used in the underlying ODE characteristic equation.
    """
    return omega_radps / (2.0 * Q)


def omega_damped(omega_radps: float, Q: float) -> float:
    """Damped oscillation frequency ω_d = ω₀·√(1 - 1/(4Q²)).

    Real (non-zero) for Q > 0.5 (underdamped). Zero at Q = 0.5 (critical).
    For Q < 0.5, the system has no damped oscillation — this function
    returns 0.0 in that case (sentinel; the physical regime is two real
    exponentials, no oscillation).
    """
    if Q <= 0.5:
        return 0.0
    return omega_radps * math.sqrt(1.0 - 1.0 / (4.0 * Q * Q))


def _load_single_mode(data: dict) -> Actuator:
    """Load an MDPI-2020-style single-mode lumped actuator with multiple instances."""
    shared = data["shared_parameters"]
    instances = data["instances"]

    modes = []
    for i, (instance_name, instance) in enumerate(instances.items()):
        Q = instance["computed_quality_factor_Q"]
        modes.append(ActuatorMode(
            index=i,
            omega_radps=shared["natural_frequency_radps"],
            zeta=instance["computed_damping_ratio_zeta"],
            Q=Q,
            regime=regime_from_Q(Q),
            kappa_residue=None,
            notes=f"Instance: {instance_name}. {instance.get('regime_notes', '')}",
        ))

    return Actuator(
        substrate_id=Path(data["source"]["url"]).stem if data["source"].get("url") else "mdpi-2020",
        substrate_class_variant=data["substrate_class_variant"],
        modes=tuple(modes),
        structural_parameters=shared,
        source_citation=data["source"]["citation"],
    )


def _load_modal(data: dict) -> Actuator:
    """Load a PyHDDBenchmark-style multimodal actuator."""
    modes = []
    for m in data["modes"]:
        Q = m.get("Q")
        modes.append(ActuatorMode(
            index=m["index"],
            omega_radps=m["omega_radps"],
            zeta=m["zeta"],
            Q=Q,
            regime=m.get("regime") or regime_from_Q(Q),
            kappa_residue=m.get("kappa_residue"),
            notes=m.get("notes"),
        ))

    return Actuator(
        substrate_id=data["source"].get("repository", "unknown"),
        substrate_class_variant=data["substrate_class_variant"],
        modes=tuple(modes),
        structural_parameters=data.get("structural_parameters", {}),
        source_citation=data["source"].get("originating_benchmark", "unknown"),
    )


def load_actuator(json_path: str | Path) -> Actuator:
    """Load an actuator characterization from JSON.

    Detects single-mode (shared_parameters + instances) vs multimodal (modes
    list) format from the JSON schema.
    """
    with open(json_path, encoding="utf-8") as fh:
        data = json.load(fh)

    if "instances" in data and "shared_parameters" in data:
        return _load_single_mode(data)
    if "modes" in data:
        return _load_modal(data)
    raise ValueError(f"Unrecognized actuator JSON schema in {json_path}")


def regime_summary(actuator: Actuator) -> dict:
    """Aggregate regime counts across an actuator's modes."""
    counts = {"c": 0, "s": 0, "r": 0, "rigid_body": 0}
    for mode in actuator.modes:
        counts[mode.regime] = counts.get(mode.regime, 0) + 1

    qs = [m.Q for m in actuator.modes if m.Q is not None]
    return {
        "substrate_id": actuator.substrate_id,
        "total_modes": len(actuator.modes),
        "regime_counts": counts,
        "Q_range": (min(qs), max(qs)) if qs else None,
        "omega_range_radps": (
            min(m.omega_radps for m in actuator.modes if m.omega_radps > 0),
            max(m.omega_radps for m in actuator.modes),
        ) if any(m.omega_radps > 0 for m in actuator.modes) else None,
    }


__all__ = [
    "ActuatorMode",
    "Actuator",
    "compute_Q",
    "compute_omega",
    "compute_zeta",
    "regime_from_Q",
    "chit_max_predicted",
    "gamma_decay_rate",
    "omega_damped",
    "load_actuator",
    "regime_summary",
]
