"""F-001-actuator: chit_max bound from substrate-class electromechanical
conversion efficiency.

cdv1 F-001 from mpa-engine: chit_max ≈ -ln(1 - η_max), where η_max is the
substrate's peak conversion efficiency at the operating sweet spot. For
engines: η_thermal_max = brake_power / fuel_power. For voice coil actuators
at mechanical resonance with no external load specified, η is the fraction
of input electrical power that crosses the BL coupling into the mechanical
degree of freedom:

    η_em = (BL)² / (c·R + (BL)²)

This is a *substrate-intrinsic bound*: the actuator's electromechanical
coupling caps the maximum chit any future use-case configuration could
reach at this operating point. It is *not* an observed chit value at a
specific operating point — that would require step-response measurements
under a specified load.

For substrate-zero stack:

- MDPI 2020 cantilever VCA: parameters R, BL, c published in Table 2;
  η_em computable directly per bobbin instance.
- PyHDDBenchmark VCM and PZT: published as modal parameters (ω, ζ, κ);
  no direct (BL, R, c) per mode in plant.py. η_em not extractable from
  current ingest. Deferred pending fetch of Atsumi & Yabui 2020 physical
  parameters or direct measurement.
"""
from __future__ import annotations

import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from mpa_relaxation_packs.voice_coil import (  # noqa: E402
    chit_max_predicted,
    electromechanical_efficiency_at_resonance,
)


def main() -> dict:
    results = {
        "experiment": "f001_actuator",
        "run_at": datetime.now(timezone.utc).isoformat(),
        "phase_a_step": 7,
        "claim_under_test": (
            "cdv1 F-001: chit_max ≈ -ln(1 - η_max) for any driven-dissipative "
            "substrate-class instance, where η_max is the operating-point peak "
            "conversion efficiency. For voice coil actuators at mechanical "
            "resonance, η_em = (BL)² / (c·R + (BL)²)."
        ),
        "instances": [],
        "cross_substrate_comparison": {},
        "deferred": [],
    }

    # ---- MDPI 2020 cantilever VCA, two instances ----
    BL = 28.46
    R = 28.9
    L_e = 0.024535
    m = 0.0652
    k = 1485.0
    omega_0 = math.sqrt(k / m)
    reactance_ratio = (L_e * omega_0) / R

    for bobbin, c in [("aluminum", 300.0), ("plastic", 25.0)]:
        eta = electromechanical_efficiency_at_resonance(BL, R, c, L_e=L_e, omega_0=omega_0)
        chit_bound = chit_max_predicted(eta)
        zeta = c / (2.0 * math.sqrt(m * k))
        Q = 1.0 / (2.0 * zeta)
        results["instances"].append({
            "substrate": "MDPI 2020 cantilever VCA",
            "instance": f"{bobbin}_bobbin",
            "regime": "r" if Q < 0.5 else ("s" if abs(Q - 0.5) < 0.02 else "c"),
            "Q": Q,
            "BL_npa": BL,
            "R_ohm": R,
            "c_nspm": c,
            "L_e_henry": L_e,
            "omega_0_radps": omega_0,
            "L_e_reactance_ratio": reactance_ratio,
            "eta_em": eta,
            "chit_max_bound": chit_bound,
            "interpretation": (
                f"At mechanical resonance ω₀={omega_0:.2f} rad/s, fraction {eta:.4f} of "
                f"input electrical power crosses BL coupling into mechanical motion. "
                f"chit at any operating point delivering useful work bounded above by {chit_bound:.4f}."
            ),
        })

    # ---- PyHDDBenchmark VCM and PZT: deferred ----
    results["deferred"].append({
        "substrate": "PyHDDBenchmark VCM",
        "reason": (
            "plant.py provides modal parameters (ω, ζ, κ) but not direct (BL, R, c) "
            "per mode. η_em formula requires substrate-intrinsic electrical and "
            "mechanical parameters. Deferred pending Atsumi & Yabui 2020 paper "
            "extraction or direct measurement back-out from Fre_Resp.json."
        ),
        "alternative_path": (
            "DC gain Kp_vcm = 3.7976e7 and modal residues κ encode coupling indirectly. "
            "Recovering (BL, R, c) per mode requires the physical-parameter form of the "
            "plant model, which is downstream of the modal-sum representation in plant.py."
        ),
    })
    results["deferred"].append({
        "substrate": "PyHDDBenchmark PZT",
        "reason": (
            "PZT is electrostrictive drive, not Lorentz. The BL-coupling form of the "
            "η_em formula does not apply directly. PZT efficiency at mechanical resonance "
            "uses d33-coefficient × stress geometry; a different substrate-class formula. "
            "Substrate-class scope decision deferred (one class spanning both drive "
            "mechanisms, or two)."
        ),
    })

    # ---- Cross-substrate comparison ----
    mdpi_bounds = [i["chit_max_bound"] for i in results["instances"]]
    results["cross_substrate_comparison"] = {
        "mdpi_2020_chit_max_bound_range": [min(mdpi_bounds), max(mdpi_bounds)],
        "engine_chit_max_observed_camry": 0.410,
        "engine_chit_max_predicted_camry": 0.432,
        "loudspeaker_chit_max_estimated_typical_range": [0.003, 0.014],
        "observation": (
            "MDPI 2020 plastic-bobbin actuator bound (chit_max ≤ 0.752) is HIGHER than "
            "engines (~0.41). The 'narrow chit envelope' was a loudspeaker-specific "
            "finding, not a substrate-class one for actuators. Voice coil substrates "
            "span a wider chit envelope than engines when the mechanical damping is "
            "light and electromagnetic coupling is strong."
        ),
        "substrate_class_chit_max_ordering": (
            "loudspeaker (≤0.014, radiation-capped) << engine (~0.41, thermal-capped) < "
            "VCA-eddy-damped (≤0.089, dissipation-capped) < engine again < "
            "VCA-light-damped (≤0.752, coupling-capped)"
        ),
    }

    return results


def print_summary(results: dict) -> None:
    print("=" * 76)
    print(f"  F-001-actuator · chit_max bound from electromechanical efficiency")
    print(f"  run {results['run_at']}")
    print("=" * 76)

    for inst in results["instances"]:
        print(f"\n[{inst['substrate']} · {inst['instance']}]")
        print(f"  Regime              : {inst['regime']}  (Q = {inst['Q']:.3f})")
        print(f"  BL, R, c            : {inst['BL_npa']:.2f} N/A, {inst['R_ohm']:.1f} Ω, {inst['c_nspm']:.1f} N·s/m")
        print(f"  L_e·ω₀/R            : {inst['L_e_reactance_ratio']:.4f}  (small ⇒ formula applies)")
        print(f"  η_em                : {inst['eta_em']:.4f}")
        print(f"  chit_max bound      : {inst['chit_max_bound']:.4f}")

    print(f"\n[deferred]")
    for d in results["deferred"]:
        print(f"  {d['substrate']:30s} : {d['reason'][:60]}...")

    print(f"\n[cross-substrate]")
    c = results["cross_substrate_comparison"]
    print(f"  MDPI 2020 chit_max range : [{c['mdpi_2020_chit_max_bound_range'][0]:.4f}, {c['mdpi_2020_chit_max_bound_range'][1]:.4f}]")
    print(f"  Engine Camry observed     : {c['engine_chit_max_observed_camry']:.4f}")
    print(f"  Engine Camry predicted    : {c['engine_chit_max_predicted_camry']:.4f}")
    print(f"  Loudspeaker typical range : {c['loudspeaker_chit_max_estimated_typical_range']}")
    print(f"\n  Ordering: {c['substrate_class_chit_max_ordering']}")
    print()


if __name__ == "__main__":
    results = main()
    output_path = REPO_ROOT / "docs" / "results" / "f001_actuator.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=2)
    print_summary(results)
    print(f"Wrote {output_path.relative_to(REPO_ROOT)}")
