"""F-003-rlc: c→s→r recovery-tail walk in series RLC substrate.

cdv1 §Stability predicts that the relaxation profile at the s-boundary
(Q = 0.5, chit ≈ 0) is qualitatively distinct from c-regime (Q > 0.5,
exponential-with-oscillation) and r-regime (Q < 0.5, double-exponential).
Specifically: at critical damping, the analytical step response carries an
algebraic factor (1 + α·t)·e^(-α·t), which neither pure-exponential nor
pure-double-exponential forms capture.

This experiment sweeps Q across the c→s→r range, generates the analytical
step response at each, and measures the RMS residual when reconstructing
the step response from two candidate envelope forms:
    A: pure exponential          1 - e^(-α·t)
    B: algebraic-exponential     1 - (1 + α·t)·e^(-α·t)

cdv1 prediction: B beats A *only* at Q = 0.5. Specifically, the ratio
RMS(B) / RMS(A) bottoms out at zero at Q = 0.5 and is well above zero
elsewhere. This is the F-003-rlc signature.

The RLC substrate is textbook-analytical with no noise, no unmeasured loss
channels, no substrate-conditional artefacts. This is the null-check
substrate: if the F-003 prediction doesn't land here, the framework's
prediction is wrong (or the test machinery is wrong). If it lands here,
the test machinery is correct and we can apply it to real substrates with
confidence.
"""
from __future__ import annotations

import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from mpa_relaxation_packs.rlc import (  # noqa: E402
    algebraic_signature,
    envelope_form,
    overshoot,
    rlc_from_Q,
    step_response,
)


# Fine sweep around Q = 0.5 to catch the minimum sharply; coarser elsewhere.
Q_SWEEP = [
    0.05, 0.10, 0.15, 0.20, 0.30, 0.40,
    0.45, 0.47, 0.49, 0.495, 0.500, 0.505, 0.51, 0.53, 0.55,
    0.60, 0.707, 0.80, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0,
]


def main() -> dict:
    results = {
        "experiment": "f003_rlc_walk",
        "run_at": datetime.now(timezone.utc).isoformat(),
        "phase_b": True,
        "substrate": "series RLC (substrate-two)",
        "claim_under_test": (
            "cdv1 §Stability: at the s-boundary (Q = 0.5, chit ≈ 0), the step-response "
            "decay envelope carries an algebraic factor (1 + α·t)·e^(-α·t) qualitatively "
            "distinct from c-regime (exponential with oscillation) and r-regime "
            "(double-exponential)."
        ),
        "test_form": (
            "Sweep Q. For each Q, reconstruct the analytical step response from two "
            "candidate envelope forms (pure-exp 'A', algebraic-exp 'B'). Compare RMS "
            "residuals. F-003 signature: residual ratio RMS(B)/RMS(A) bottoms out at "
            "Q = 0.5 (B is the exact form there; A is wrong)."
        ),
        "sweep": [],
        "summary": {},
    }

    omega_0 = 1.0   # All entries normalized to ω₀ = 1; absolute scale immaterial.

    min_ratio = float("inf")
    min_Q = None
    for Q in Q_SWEEP:
        p = rlc_from_Q(Q, omega_0=omega_0)
        sig = algebraic_signature(p, n_periods=5)
        entry = {
            "Q": Q,
            "regime": p.regime,
            "alpha_div_omega0": p.alpha / omega_0,
            "omega_d_div_omega0": (p.omega_damped / omega_0) if p.omega_damped is not None else None,
            "overshoot_pct": overshoot(p) * 100.0,
            "envelope_form": envelope_form(Q),
            "rms_residual_pure_exp": sig["rms_residual_pure_exp"],
            "rms_residual_algebraic_exp": sig["rms_residual_algebraic_exp"],
            "ratio_alg_to_pure": sig["ratio_alg_to_pure"],
        }
        results["sweep"].append(entry)
        if sig["ratio_alg_to_pure"] < min_ratio:
            min_ratio = sig["ratio_alg_to_pure"]
            min_Q = Q

    # Summary metrics.
    pure_at_critical = next(e for e in results["sweep"] if e["Q"] == 0.500)
    pure_far_c = next(e for e in results["sweep"] if e["Q"] == 2.0)
    pure_far_r = next(e for e in results["sweep"] if e["Q"] == 0.10)

    results["summary"] = {
        "ratio_minimum_at_Q": min_Q,
        "ratio_minimum_value": min_ratio,
        "Q_critical_prediction": 0.5,
        "ratio_at_Q_0500": pure_at_critical["ratio_alg_to_pure"],
        "ratio_at_Q_2000_c_regime": pure_far_c["ratio_alg_to_pure"],
        "ratio_at_Q_0100_r_regime": pure_far_r["ratio_alg_to_pure"],
        "prediction_passes": min_Q == 0.500 and min_ratio < 0.05,
        "interpretation": (
            "F-003-rlc passes if RMS(B)/RMS(A) minimum occurs at Q = 0.5 with ratio "
            "essentially zero. Failure modes: minimum off-center (test machinery has "
            "a bias); minimum not at zero (algebraic form is approximate); minimum "
            "below 0.5 (overdamped solution closer to algebraic-exp than to pure-exp, "
            "test diagnostic but not regime-specific)."
        ),
    }

    return results


def print_summary(results: dict) -> None:
    print("=" * 76)
    print(f"  F-003-rlc · c→s→r recovery-tail walk in series RLC")
    print(f"  run {results['run_at']}")
    print("=" * 76)
    print(f"\n  Substrate: {results['substrate']}")
    print(f"  Claim    : {results['claim_under_test'][:70]}...")
    print()
    print(f"  {'Q':>7} {'regime':>5} {'overshoot%':>11} {'pure_exp_RMS':>14} {'alg_exp_RMS':>13} {'ratio':>8}")
    print(f"  {'-'*7} {'-'*5} {'-'*11} {'-'*14} {'-'*13} {'-'*8}")
    for e in results["sweep"]:
        print(f"  {e['Q']:>7.3f} {e['regime']:>5} {e['overshoot_pct']:>10.2f}% "
              f"{e['rms_residual_pure_exp']:>14.6f} {e['rms_residual_algebraic_exp']:>13.6f} "
              f"{e['ratio_alg_to_pure']:>8.4f}")

    s = results["summary"]
    print()
    print(f"  [F-003-rlc result]")
    print(f"    Q at which ratio minimum occurs : {s['ratio_minimum_at_Q']}")
    print(f"    Ratio at the minimum            : {s['ratio_minimum_value']:.6f}")
    print(f"    Ratio at Q = 0.500 (predicted s) : {s['ratio_at_Q_0500']:.6f}")
    print(f"    Ratio at Q = 2.000 (deep c)      : {s['ratio_at_Q_2000_c_regime']:.6f}")
    print(f"    Ratio at Q = 0.100 (deep r)      : {s['ratio_at_Q_0100_r_regime']:.6f}")
    print(f"    Prediction passes               : {s['prediction_passes']}")
    print()


if __name__ == "__main__":
    results = main()
    output_path = REPO_ROOT / "docs" / "results" / "f003_rlc_walk.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=2)
    print_summary(results)
    print(f"Wrote {output_path.relative_to(REPO_ROOT)}")
