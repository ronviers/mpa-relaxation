"""Phase F.1 step 2: F-001-led test on cross-substrate LED stack.

cdv1 F-001 (chit_max ≈ -ln(1 - η_max)) applied to LEDs as a drive-axis,
mode-separated substrate. For LEDs, η is the wall-plug efficiency
η_wpe = (optical power radiated) / (electrical power consumed) at the
design operating point.

13 LEDs ingested from data/leds.json, spanning:
- Chemistries: white, blue, red, deep red, yellow-green, UV
- Power classes: indicator, smartphone, automotive, bulb, industrial,
  industrial high-power
- Regions: Western (USA, German), Japanese, Chinese, Korean, Taiwan

Tests:
1. F-001-led: chit_max bound from η_wpe per LED.
2. Substrate-class fingerprint: distribution of chit_max bounds across LEDs.
3. Cross-substrate position: where do LEDs sit relative to engines, voice
   coil actuators, viscoelastic damping, RLC?
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from mpa_relaxation_packs.led import (  # noqa: E402
    chit_max_predicted,
    load_leds,
    substrate_class_summary,
)


def main() -> dict:
    leds = load_leds(REPO_ROOT / "data" / "leds.json")

    results = {
        "experiment": "f001_led",
        "run_at": datetime.now(timezone.utc).isoformat(),
        "phase_f_step": "1.2",
        "claim_under_test": (
            "F-001 applies to LEDs as a mode-separated drive-axis substrate. "
            "chit_max ≤ -ln(1 - η_wpe) where η_wpe is wall-plug efficiency."
        ),
        "n_leds": len(leds),
        "instances": [],
        "substrate_class_summary": substrate_class_summary(leds),
        "cross_substrate_position": {},
    }

    for led in leds:
        chit_max_bound = chit_max_predicted(led.eta_wpe)
        results["instances"].append({
            "id": led.id,
            "vendor": led.vendor,
            "model": led.model,
            "chemistry": led.chemistry,
            "power_class": led.power_class,
            "V_th_V": led.V_th_V,
            "eta_wpe": led.eta_wpe,
            "chit_max_bound": chit_max_bound,
        })

    chit_bounds = [i["chit_max_bound"] for i in results["instances"]]

    results["substrate_class_summary"]["chit_max_bound_range"] = (
        min(chit_bounds), max(chit_bounds)
    )
    results["substrate_class_summary"]["chit_max_bound_median"] = sorted(chit_bounds)[len(chit_bounds) // 2]

    # Cross-substrate position
    results["cross_substrate_position"] = {
        "leds_chit_max_bound_range": (min(chit_bounds), max(chit_bounds)),
        "leds_chit_max_bound_median": sorted(chit_bounds)[len(chit_bounds) // 2],
        "vs_engine_Camry_observed": 0.410,
        "vs_actuator_mdpi_plastic_bound": 0.752,
        "vs_actuator_pyhddbenchmark_open_loop_Q_range": [12.5, 71.4],
        "vs_viscoelastic_Q_median": 0.750,
        "vs_loudspeaker_chit_observed_range": [0.003, 0.014],

        "ordering_chit_max": (
            "UV LED (0.084, low conversion efficiency) ≈ loudspeaker (0.003-0.014, "
            "radiation cap) < indicator LEDs (0.16, low-end) < red/blue LEDs (0.43, "
            "moderate) ≈ engine Camry (0.41, thermal cap) < white LEDs (0.50-0.69, "
            "premium efficiency) ≈ VCA-plastic-bobbin (0.75, coupling-limited)"
        ),

        "interpretation": (
            "LEDs span the full chit_max envelope from UV (0.08, lowest of any "
            "substrate-class characterized) to premium white (0.69, near the "
            "actuator coupling limit). The substrate-class is internally "
            "heterogeneous in F-001 — chemistry dictates η_wpe more than power "
            "class does. AlGaInP red and InGaN blue/white share the substrate-class "
            "but live at very different chit_max bounds because of different "
            "internal quantum efficiencies."
        ),
    }

    # F-002 reading at the LED substrate
    results["f_002_reading"] = {
        "claim": (
            "At sustained operation in c-regime (V_drive > V_th + kT/q), the LED "
            "is in NESS: average G₀ = electrical input power, average L = "
            "electrical input - radiated optical power - junction heat. By energy "
            "conservation at steady state, chit at the operating point is "
            "well-defined but not necessarily 0."
        ),
        "subtlety": (
            "Unlike damping-axis substrates where chit ≈ 0 at the SOC attractor "
            "by power balance (G₀ = L_dissipation), drive-axis substrates have "
            "the additional 'useful work out' channel (η_wpe of input emerges as "
            "photons). chit at sustained operation = ln(G₀/L) where L excludes "
            "the photon-output term. This is the F-001 reading — chit_max is "
            "bounded by η_wpe."
        ),
    }

    # Drive-axis F-003 hypothesis (research-pending)
    results["drive_axis_f_003_hypothesis"] = {
        "status": "OPEN — hypothesis surfaced from cross-research, fit pending data",
        "candidate_1": (
            "Static I-V threshold smearing: V_th transition zone ~kT/q wide. "
            "Sub-threshold leakage (SRH) vs exponential turn-on. The s-region "
            "width on the drive-axis is set by thermal noise."
        ),
        "candidate_2": (
            "Dynamic efficiency droop peak: ABC recombination model R = "
            "A·n + B·n² + C·n³ where A = SRH non-radiative, B = radiative, "
            "C = Auger non-radiative. η_wpe peaks at intermediate carrier "
            "density where B·n²/(A·n + B·n² + C·n³) is maximized. The peak "
            "position and curvature may be the substrate-conditional drive-axis "
            "signature, analogous to the algebraic-exp factor at Q = 0.5 on "
            "damping-axis substrates."
        ),
        "test_path": (
            "University of Bath ABC-recombination dataset (Excel, multiple "
            "commercial InGaN LEDs, 0-500 mA L-I + I-V) is the most direct "
            "data source for testing hypothesis 2. NBSDC China LED "
            "Optoelectronic Characteristics dataset (4.42 MB) is the secondary "
            "candidate. Both pending verification in a future turn."
        ),
    }

    return results


def print_summary(results: dict) -> None:
    print("=" * 78)
    print(f"  F-001-led · Phase F.1 step 2")
    print(f"  run {results['run_at']}")
    print("=" * 78)

    print(f"\n  {'id':<28} {'chem':<12} {'V_th':>6} {'η_wpe':>7} {'chit_max':>10}")
    for inst in results["instances"]:
        print(f"  {inst['id']:<28} {inst['chemistry']:<12} "
              f"{inst['V_th_V']:>6.2f} {inst['eta_wpe']:>7.3f} "
              f"{inst['chit_max_bound']:>10.4f}")

    s = results["substrate_class_summary"]
    print(f"\n  Substrate-class summary:")
    print(f"    n_leds                 : {s['n_leds']}")
    print(f"    V_th range (V)         : [{s['V_th_range_V'][0]:.2f}, {s['V_th_range_V'][1]:.2f}]")
    print(f"    η_wpe range            : [{s['eta_wpe_range'][0]:.3f}, {s['eta_wpe_range'][1]:.3f}]")
    print(f"    chit_max bound range   : [{s['chit_max_bound_range'][0]:.4f}, {s['chit_max_bound_range'][1]:.4f}]")
    print(f"    chit_max bound median  : {s['chit_max_bound_median']:.4f}")
    print(f"    chemistries            : {s['chemistries']}")
    print(f"    power classes          : {s['power_classes']}")

    x = results["cross_substrate_position"]
    print(f"\n  Cross-substrate position:")
    print(f"    LEDs chit_max range    : [{x['leds_chit_max_bound_range'][0]:.4f}, {x['leds_chit_max_bound_range'][1]:.4f}]")
    print(f"    Engine Camry observed  : {x['vs_engine_Camry_observed']:.4f}")
    print(f"    Actuator plastic bound : {x['vs_actuator_mdpi_plastic_bound']:.4f}")
    print(f"    Viscoelastic Q median  : {x['vs_viscoelastic_Q_median']:.4f}")
    print(f"    Loudspeaker chit range : {x['vs_loudspeaker_chit_observed_range']}")
    print()
    print(f"  Drive-axis F-003 hypothesis: {results['drive_axis_f_003_hypothesis']['status']}")
    print()


if __name__ == "__main__":
    results = main()
    output_path = REPO_ROOT / "docs" / "results" / "f001_led.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=2)
    print_summary(results)
    print(f"Wrote {output_path.relative_to(REPO_ROOT)}")
