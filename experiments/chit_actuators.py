"""Smoke experiment: chit reading across the substrate-zero stack.

Loads the three substrate-zero JSON files (MDPI 2020 cantilever VCA in two
bobbin variants; PyHDDBenchmark VCM with 16 modes; PyHDDBenchmark PZT with
8 modes) and computes substrate-structural regime classifications and the
F-001 chit_max prediction across a sweep of electromechanical efficiencies.

Writes structured output to docs/results/chit_actuators_smoke.json.

This is Phase A step 6 in docs/handoff_next_session.md. Closes the kernel
+ data ingestion loop before the F-001-actuator test (Phase A step 7) and
F-002-contrast FOOTING entry (Phase A step 8).
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# Make sure to print UTF-8 safely on Windows consoles.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from mpa_relaxation_packs.voice_coil import (  # noqa: E402
    chit_max_predicted,
    gamma_decay_rate,
    load_actuator,
    omega_damped,
    regime_summary,
)


SUBSTRATE_FILES = [
    REPO_ROOT / "data" / "mdpi-2020-cantilever-vca.json",
    REPO_ROOT / "data" / "pyhddbenchmark-vcm.json",
    REPO_ROOT / "data" / "pyhddbenchmark-pzt.json",
]

EFFICIENCY_SWEEP = [0.02, 0.05, 0.10, 0.20, 0.30, 0.50, 0.80]


def main() -> dict:
    results = {
        "experiment": "chit_actuators_smoke",
        "run_at": datetime.now(timezone.utc).isoformat(),
        "phase_a_step": 6,
        "substrate_zero_stack": [],
        "cross_substrate_envelope": {},
        "F-001_chit_max_prediction_sweep": {},
    }

    all_modes = []
    all_qs = []

    for path in SUBSTRATE_FILES:
        actuator = load_actuator(path)
        summary = regime_summary(actuator)

        substrate_entry = {
            "source_file": path.name,
            "substrate_id": actuator.substrate_id,
            "variant": actuator.substrate_class_variant,
            "citation": actuator.source_citation,
            "summary": {
                "total_modes": summary["total_modes"],
                "regime_counts": summary["regime_counts"],
                "Q_range": summary["Q_range"],
                "omega_range_radps": summary["omega_range_radps"],
            },
            "modes": [],
        }

        for mode in actuator.modes:
            mode_entry = {
                "index": mode.index,
                "omega_radps": mode.omega_radps,
                "zeta": mode.zeta,
                "Q": mode.Q,
                "regime": mode.regime,
            }
            if mode.Q is not None and mode.Q > 0:
                mode_entry["gamma_decay_radps"] = gamma_decay_rate(mode.omega_radps, mode.Q)
                mode_entry["omega_damped_radps"] = omega_damped(mode.omega_radps, mode.Q)
            if mode.kappa_residue is not None:
                mode_entry["kappa_residue"] = mode.kappa_residue
            if mode.notes:
                mode_entry["notes"] = mode.notes
            substrate_entry["modes"].append(mode_entry)

            if mode.Q is not None and mode.Q > 0:
                all_modes.append((path.name, mode.index, mode.omega_radps, mode.Q, mode.regime))
                all_qs.append(mode.Q)

        results["substrate_zero_stack"].append(substrate_entry)

    # Cross-substrate envelope across all real (non-rigid-body) modes.
    results["cross_substrate_envelope"] = {
        "total_real_modes": len(all_modes),
        "Q_min": min(all_qs),
        "Q_max": max(all_qs),
        "regime_distribution": {
            "c": sum(1 for m in all_modes if m[4] == "c"),
            "s": sum(1 for m in all_modes if m[4] == "s"),
            "r": sum(1 for m in all_modes if m[4] == "r"),
        },
        "Q_span_decades": f"{all_qs and ((max(all_qs) / min(all_qs)) if min(all_qs) > 0 else float('inf')):.1f}x",
        "regime_coverage": "c-regime and r-regime represented; s-boundary (Q ≈ 0.5) unsampled in current stack",
    }

    # F-001 prediction sweep.
    for eta in EFFICIENCY_SWEEP:
        results["F-001_chit_max_prediction_sweep"][f"eta={eta}"] = {
            "chit_max_bound": chit_max_predicted(eta),
            "interpretation": f"For a substrate-class instance with electromechanical efficiency {eta:.0%}, F-001 predicts chit_max ≤ {chit_max_predicted(eta):.4f}.",
        }

    # Predictions queued for next phase (recorded in JSON for handoff continuity).
    results["queued_for_phase_a_step_7"] = {
        "F-001-actuator": {
            "description": "chit_max bound across substrate-zero instances.",
            "needs": "Electromechanical efficiency eta for each instance (MDPI 2020 Al/plastic, PyHDDBenchmark VCM, PyHDDBenchmark PZT). Compute eta = useful_mechanical_work / electrical_input at sustained operating point.",
            "status": "pending eta extraction",
        },
    }

    results["queued_for_phase_a_step_8"] = {
        "F-002-contrast": {
            "description": "Record SOC-attractor reading as substrate-conditional, not universal.",
            "claim": "HDD VCMs are deliberately engineered for c-regime; engines tune to chit≈0 at idle by SOC self-tuning; loudspeakers sit at chit≈0 by radiation efficiency cap. Three different substrates, three different positions on the chit axis by design.",
            "status": "ready to land in docs/journey/FOOTING.md as F-002-contrast",
        },
    }

    return results


def print_summary(results: dict) -> None:
    print("=" * 72)
    print(f"  {results['experiment']}  (run {results['run_at']})")
    print("=" * 72)

    for entry in results["substrate_zero_stack"]:
        s = entry["summary"]
        print(f"\n[{entry['source_file']}]")
        print(f"  Variant : {entry['variant'][:64]}{'...' if len(entry['variant']) > 64 else ''}")
        print(f"  Modes   : {s['total_modes']}  ({s['regime_counts']})")
        if s["Q_range"]:
            print(f"  Q range : {s['Q_range'][0]:.3f} to {s['Q_range'][1]:.3f}")
        if s["omega_range_radps"]:
            print(f"  ω range : {s['omega_range_radps'][0]:.1f} to {s['omega_range_radps'][1]:.1f} rad/s")

    env = results["cross_substrate_envelope"]
    print(f"\n[cross-substrate envelope]")
    print(f"  Real modes : {env['total_real_modes']}")
    print(f"  Q span     : {env['Q_min']:.3f} to {env['Q_max']:.2f}  ({env['Q_span_decades']})")
    print(f"  Regimes    : {env['regime_distribution']}")
    print(f"  Coverage   : {env['regime_coverage']}")

    print(f"\n[F-001 chit_max prediction sweep]")
    for key, val in results["F-001_chit_max_prediction_sweep"].items():
        print(f"  {key:12s} → chit_max ≤ {val['chit_max_bound']:.4f}")

    print(f"\n[queued]")
    print(f"  Phase A step 7 : F-001-actuator (needs eta)")
    print(f"  Phase A step 8 : F-002-contrast (ready to land in FOOTING)")
    print()


if __name__ == "__main__":
    results = main()

    output_path = REPO_ROOT / "docs" / "results" / "chit_actuators_smoke.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=2)

    print_summary(results)
    print(f"Wrote {output_path.relative_to(REPO_ROOT)}")
