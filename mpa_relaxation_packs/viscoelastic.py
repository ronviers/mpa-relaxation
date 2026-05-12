"""cdv1 reading on viscoelastic damping material substrate (substrate-three).

A viscoelastic damping material is a polymeric medium with frequency- and
temperature-dependent complex modulus E*(ω, T) = E'(ω, T) + i·E''(ω, T).
The loss tangent η = tan δ = E''/E' characterizes the material's
substrate-class signature: η near 0 means elastic (rings indefinitely),
η near 2 means critically damped (no oscillation, fast relaxation), η > 2
means overdamped (sluggish reflective layer).

Relation to mass-spring oscillator coupled to a viscoelastic damper:

    ω₀ = √(k/m)                  natural frequency of coupled system
    ζ = η / 2                    damping ratio (ζ = 1 ⇔ η = 2 ⇔ critical)
    Q = 1 / η                    quality factor at resonance

Regime classification from η (same boundaries as from Q, just inverted):

    η < 2  (Q > 0.5)  → c (underdamped, oscillatory relaxation)
    η = 2  (Q = 0.5)  → s (critically damped, algebraic settling)
    η > 2  (Q < 0.5)  → r (overdamped, two-exponential relaxation)

**Substrate-class scope limit on F-001.** cdv1 F-001 (chit_max ≈ -ln(1 - η_conv))
applies to substrates where the drive is in one mode and the useful output
is in a different mode (engine: fuel → brake-power; loudspeaker: electrical
→ acoustic; voice coil actuator: electrical → mechanical motion). For
viscoelastic damping materials, dissipation IS the useful work — the
material's purpose is to convert mechanical vibration into heat. There is
no separate "useful output" mode. F-001 chit_max → ∞ in the limit; the
formula breaks down.

This is the first substrate where F-001 doesn't apply directly. The
implication is that F-001 is *not* universal across all driven-dissipative
substrates — it has a scope limit: substrates with mode-separated
drive-vs-useful-work. F-003 (regime structure from Q) is more general:
it applies wherever a second-order damped oscillator can be defined, which
includes both mode-separated substrates and pure-dissipative substrates
like this one.
"""
from __future__ import annotations

import json
import math
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass(frozen=True)
class ViscoelasticMaterial:
    """One viscoelastic damping material instance characterized at its peak."""
    id: str
    name: str
    composition: str
    typical_application: str
    peak_tan_delta: float       # η at the design sweet spot
    peak_temperature_C: float
    peak_frequency_Hz: float
    operating_temperature_range_C: tuple[float, float]
    operating_frequency_range_Hz: tuple[float, float]
    Q_at_peak: float             # = 1 / tan δ
    zeta_at_peak: float          # = tan δ / 2
    regime_at_peak: str          # "c" | "s" | "r"
    notes: Optional[str] = None


def Q_from_tan_delta(tan_delta: float) -> float:
    """Quality factor at resonance from loss tangent. Q = 1/η.

    Diverges at tan δ = 0 (lossless elastic limit).
    """
    if tan_delta <= 0.0:
        return float("inf")
    return 1.0 / tan_delta


def zeta_from_tan_delta(tan_delta: float) -> float:
    """Damping ratio from loss tangent. ζ = η/2.

    ζ = 1 at critical (s-boundary), corresponding to tan δ = 2.
    """
    return tan_delta / 2.0


def regime_from_tan_delta(tan_delta: float, s_band_tan_delta: float = 0.08) -> str:
    """Classify substrate regime from loss tangent.

    s_band_tan_delta: half-width around tan δ = 2 (s-boundary) counted as s.
    Default 0.08 → tan δ ∈ [1.92, 2.08] is s. Corresponds to Q ∈ [0.48, 0.52],
    matching the voice_coil.regime_from_Q s_band of 0.02.
    """
    if tan_delta <= 0.0:
        return "elastic_limit"
    if abs(tan_delta - 2.0) <= s_band_tan_delta:
        return "s"
    if tan_delta < 2.0:
        return "c"   # underdamped
    return "r"       # overdamped


def load_materials(json_path: str | Path) -> list[ViscoelasticMaterial]:
    """Load viscoelastic damping materials from JSON."""
    with open(json_path, encoding="utf-8") as fh:
        data = json.load(fh)
    out = []
    for m in data["materials"]:
        out.append(ViscoelasticMaterial(
            id=m["id"],
            name=m["name"],
            composition=m["composition"],
            typical_application=m["typical_application"],
            peak_tan_delta=m["peak_tan_delta"],
            peak_temperature_C=m["peak_conditions"]["temperature_C"],
            peak_frequency_Hz=m["peak_conditions"]["frequency_Hz"],
            operating_temperature_range_C=tuple(m["operating_range"]["temperature_C"]),
            operating_frequency_range_Hz=tuple(m["operating_range"]["frequency_Hz"]),
            Q_at_peak=m["Q_at_peak"],
            zeta_at_peak=m["zeta_at_peak"],
            regime_at_peak=m["regime_at_peak"],
            notes=m.get("notes"),
        ))
    return out


def regime_distribution(materials: list[ViscoelasticMaterial]) -> dict:
    """Count materials per regime; report median Q and clustering near s-boundary."""
    counts = {"c": 0, "s": 0, "r": 0}
    Qs = []
    for m in materials:
        counts[m.regime_at_peak] = counts.get(m.regime_at_peak, 0) + 1
        Qs.append(m.Q_at_peak)
    Qs_sorted = sorted(Qs)
    n = len(Qs_sorted)
    median_Q = Qs_sorted[n // 2] if n % 2 == 1 else (Qs_sorted[n // 2 - 1] + Qs_sorted[n // 2]) / 2.0

    # Distance from s-boundary (Q = 0.5)
    distances_from_s = [abs(Q - 0.5) for Q in Qs]
    near_s_count = sum(1 for d in distances_from_s if d <= 0.17)  # within ~33% of critical

    return {
        "n_materials": n,
        "regime_counts": counts,
        "Q_range": (min(Qs), max(Qs)),
        "Q_median": median_Q,
        "n_materials_within_0_17_of_critical": near_s_count,
        "fraction_within_0_17_of_critical": near_s_count / n,
    }


__all__ = [
    "ViscoelasticMaterial",
    "Q_from_tan_delta",
    "zeta_from_tan_delta",
    "regime_from_tan_delta",
    "load_materials",
    "regime_distribution",
]
