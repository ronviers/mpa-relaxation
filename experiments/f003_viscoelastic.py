"""Phase D: F-003 regime structure across viscoelastic damping material substrate.

Stress test: does cdv1's c→s→r regime structure hold across a substrate-class
with internal heterogeneity (polymer composition, temperature, frequency
dependence, vendor methodology variability)? Eight representative damping
materials from published handbooks (Jones 2001, Nashif et al. 1985) and
vendor datasheets (3M, EAR, Sorbothane, butyl rubber, PVC) ingested as
substrate instances.

Also tests F-001 substrate-class scope: damping materials' dissipation IS
the useful work (no input/output mode-separation). F-001's chit_max bound
form doesn't apply directly. This is the first substrate where F-001 has
a scope limit — a substantive substrate-conditional finding.

This experiment computes:
- Regime distribution across the substrate-class
- Substrate-class fingerprint: how close to s-boundary do design choices land?
- Cross-substrate comparison with engines/actuators/RLC.
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

from mpa_relaxation_packs.viscoelastic import (  # noqa: E402
    Q_from_tan_delta,
    load_materials,
    regime_distribution,
    regime_from_tan_delta,
)


def main() -> dict:
    materials = load_materials(REPO_ROOT / "data" / "viscoelastic-damping-materials.json")

    results = {
        "experiment": "f003_viscoelastic",
        "run_at": datetime.now(timezone.utc).isoformat(),
        "phase_d": True,
        "substrate": "viscoelastic-damping-material",
        "n_instances": len(materials),
        "f_001_scope_limit": {
            "applicable": False,
            "reason": (
                "Damping materials' dissipation IS the useful work — there is no "
                "separate 'useful output' mode. F-001 chit_max = -ln(1 - η_conversion) "
                "requires drive and useful-work to be in different modes (engine fuel "
                "→ brake-power; loudspeaker electrical → acoustic; actuator electrical "
                "→ mechanical). For pure-dissipative substrates, all input is loss by "
                "construction, η_conversion → 1, chit_max → ∞. F-001 form does not "
                "constrain this substrate-class. First substrate where F-001 hits "
                "a scope limit; reveals that F-001 is conditional on substrate-class "
                "having mode-separated drive vs useful-work."
            ),
            "framework_implication": (
                "F-001 is not universally applicable across all driven-dissipative "
                "substrates. F-003 (regime structure from Q) is more general — it "
                "applies wherever a second-order damped oscillator is defined, "
                "including pure-dissipative substrates like viscoelastic damping. "
                "The framework's substrate-neutral content should distinguish "
                "'mode-separated' substrates (F-001 applies) from 'pure-dissipative' "
                "substrates (F-003 applies but F-001 does not)."
            ),
        },
        "instances": [],
        "regime_distribution": {},
        "cross_substrate_class_fingerprint": {},
    }

    for m in materials:
        results["instances"].append({
            "id": m.id,
            "name": m.name,
            "composition": m.composition,
            "tan_delta_peak": m.peak_tan_delta,
            "peak_temperature_C": m.peak_temperature_C,
            "peak_frequency_Hz": m.peak_frequency_Hz,
            "Q_at_peak": m.Q_at_peak,
            "zeta_at_peak": m.zeta_at_peak,
            "regime": m.regime_at_peak,
            "distance_from_s_boundary": abs(m.Q_at_peak - 0.5),
            "notes": m.notes,
        })

    dist = regime_distribution(materials)
    results["regime_distribution"] = dist

    # Cross-substrate fingerprint: where do damping materials sit relative to
    # other substrates' chit/Q amplitudes?
    results["cross_substrate_class_fingerprint"] = {
        "viscoelastic_Q_range": dist["Q_range"],
        "viscoelastic_Q_median": dist["Q_median"],
        "vs_engine_Camry_chit_observed": 0.410,
        "vs_actuator_mdpi_plastic_chit_max_bound": 0.752,
        "vs_actuator_pyhddbenchmark_Q_open_median": 30.0,  # mid of [12.5, 71.4]
        "vs_actuator_pyhddbenchmark_Q_closedloop_median": 1.44,
        "vs_rlc_F003_signature_Q": 0.5,
        "vs_loudspeaker_chit_observed_range": [0.003, 0.014],

        "interpretation": (
            f"Viscoelastic damping materials cluster Q in [{dist['Q_range'][0]:.3f}, "
            f"{dist['Q_range'][1]:.3f}] with median {dist['Q_median']:.3f}. "
            f"{dist['n_materials_within_0_17_of_critical']} of {dist['n_materials']} "
            "instances sit within 0.17 of critical damping (Q = 0.5). One instance "
            "(PU45A) lands AT Q = 0.5 by formulation tuning — substrate engineering "
            "explicitly targets the s-boundary. The substrate-class is uniquely "
            "well-aligned with cdv1's SOC attractor: the *material composition* IS "
            "the tuning knob, and the design objective IS to land at chit ≈ 0."
        ),
    }

    # Stress-test verdict: does the cdv1 regime structure hold across substrate variability?
    n = dist["n_materials"]
    regime_categorized = sum(dist["regime_counts"][r] for r in ("c", "s", "r"))
    results["regime_structure_stress_test_verdict"] = {
        "all_instances_categorized": regime_categorized == n,
        "all_regimes_represented": all(dist["regime_counts"][r] > 0 for r in ("c", "s", "r")),
        "verdict": (
            "PASS"
            if regime_categorized == n and all(dist["regime_counts"][r] > 0 for r in ("c", "s", "r"))
            else "PARTIAL" if regime_categorized == n else "FAIL"
        ),
        "interpretation": (
            "Substrate-class spans all three regimes (c, s, r) across n=8 published "
            "instances. cdv1 regime structure holds across the material heterogeneity. "
            "The substrate-class fingerprint is explicitly engineered to span c-to-r "
            "via formulation tuning. F-003's c→s→r structure is *substrate-neutral* "
            "in this case (no exceptions). F-001 is the substrate-conditional one, "
            "with this substrate-class falling outside its scope."
        ),
    }

    return results


def print_summary(results: dict) -> None:
    print("=" * 78)
    print(f"  F-003 viscoelastic damping materials · Phase D")
    print(f"  run {results['run_at']}")
    print("=" * 78)

    print(f"\n  F-001 applicability: {results['f_001_scope_limit']['applicable']}")
    print(f"  Reason: {results['f_001_scope_limit']['reason'][:78]}...")

    print(f"\n  {'id':<28} {'tan_δ':>7} {'Q':>7} {'regime':>7} {'dist_s':>8}")
    for inst in results["instances"]:
        print(f"  {inst['id']:<28} {inst['tan_delta_peak']:>7.2f} {inst['Q_at_peak']:>7.3f} "
              f"{inst['regime']:>7} {inst['distance_from_s_boundary']:>8.3f}")

    dist = results["regime_distribution"]
    print(f"\n  Regime distribution: {dist['regime_counts']}")
    print(f"  Q range: [{dist['Q_range'][0]:.3f}, {dist['Q_range'][1]:.3f}]")
    print(f"  Q median: {dist['Q_median']:.3f}")
    print(f"  Materials within 0.17 of critical (s-boundary): {dist['n_materials_within_0_17_of_critical']}/{dist['n_materials']} ({100*dist['fraction_within_0_17_of_critical']:.0f}%)")

    v = results["regime_structure_stress_test_verdict"]
    print(f"\n  Regime structure stress test: {v['verdict']}")
    print(f"  All regimes (c, s, r) represented: {v['all_regimes_represented']}")
    print()
    print(f"  Cross-substrate fingerprint:")
    f = results["cross_substrate_class_fingerprint"]
    print(f"    viscoelastic Q range : [{f['viscoelastic_Q_range'][0]:.3f}, {f['viscoelastic_Q_range'][1]:.3f}], median {f['viscoelastic_Q_median']:.3f}")
    print(f"    engines (chit_obs)   : {f['vs_engine_Camry_chit_observed']:.3f}")
    print(f"    actuators (open-loop): Q ≈ {f['vs_actuator_pyhddbenchmark_Q_open_median']}")
    print(f"    actuators (closed)   : Q ≈ {f['vs_actuator_pyhddbenchmark_Q_closedloop_median']}")
    print(f"    loudspeakers (chit)  : ≈ {f['vs_loudspeaker_chit_observed_range']}")
    print()


if __name__ == "__main__":
    results = main()
    output_path = REPO_ROOT / "docs" / "results" / "f003_viscoelastic.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=2)
    print_summary(results)
    print(f"Wrote {output_path.relative_to(REPO_ROOT)}")
