"""F-002-restoration test on PyHDDBenchmark closed-loop.

F-002-contrast in FOOTING (entry from 2026-05-12): HDD VCM plant lives far from
chit ≈ 0 by design — open-loop modes Q ∈ [12.5, 71.4], all c-regime. The
universal SOC-attractor reading of F-002 doesn't generalize to this substrate
as-is. The proposed falsifier: examine the closed-loop trajectory. If the
controller's job is to *natively hunt for the s-boundary* (Q_cl ≈ 0.5),
F-002's universality is restored at the plant+controller level.

This experiment loads PyHDDBenchmark's published frequency-response data:
- Pc_vcm: continuous-time VCM plant (9 manufacturing variations)
- Cd_vcm: digital servo controller
- Fm_vcm: multi-rate filter (interpolation between sampling rates)

and computes:
- L(jω) = Pc · Cd · Fm  (open-loop transfer)
- T(jω) = L / (1 + L)    (closed-loop complementary sensitivity, reference→output)
- S(jω) = 1 / (1 + L)    (sensitivity, disturbance→output)

From |T| and |S| peak values, infers the closed-loop effective Q_cl using the
second-order approximation M_s = 1 / (2ζ·√(1-ζ²)), Q = 1/(2ζ).

Requires: data/external/PyHDDBenchmark/ cloned locally (see SOURCES.md §1.0).
Phase data from the JSON is in RADIANS (not degrees — early conversion attempt
got wrong factor of π/180; correction noted here for future ingest).
"""
from __future__ import annotations

import json
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

EXTERNAL_REPO = REPO_ROOT / "data" / "external" / "PyHDDBenchmark"
FRE_RESP_PATH = EXTERNAL_REPO / "Fre_Resp.json"


def to_complex(mag: np.ndarray, phase_rad: np.ndarray) -> np.ndarray:
    """Combine magnitude and phase (RADIANS) into complex array."""
    return mag * np.exp(1j * phase_rad)


def Q_from_Ms(M_s: float) -> float:
    """Estimate closed-loop Q from peak sensitivity M_s, second-order approximation.

    M_s = 1 / (2ζ·√(1-ζ²))  →  4ζ²(1-ζ²) = 1/M_s²
    Let x = ζ²: 4x² - 4x + 1/M_s² = 0  →  x = (1 ± √(1 - 1/M_s²)) / 2

    Take smaller root (underdamped). Returns 0.5 (critical) if M_s ≤ 1 (no peak).
    """
    if M_s <= 1.0 + 1e-6:
        return 0.5
    disc = 1.0 - 1.0 / (M_s * M_s)
    if disc < 0.0:
        return float("nan")
    x = (1.0 - np.sqrt(disc)) / 2.0
    if x <= 0.0:
        return float("inf")
    return 1.0 / (2.0 * np.sqrt(x))


def first_gain_crossover_phase_margin(L: np.ndarray, fvec: np.ndarray) -> tuple[float, float]:
    """First |L| = 1 crossing (gain crossover), return (f_Hz, phase_margin_deg).

    Phase margin: 180° + angle(L) at the crossover, wrapped to [-180°, 180°].
    """
    mag = np.abs(L)
    # Find sign changes of (mag - 1).
    sign_changes = np.where(np.diff(np.sign(mag - 1.0)))[0]
    if len(sign_changes) == 0:
        return float("nan"), float("nan")
    idx = sign_changes[0]
    phase_deg = np.angle(L[idx], deg=True)
    PM = 180.0 + phase_deg
    # Wrap to [-180, 180].
    if PM > 180:
        PM -= 360
    elif PM < -180:
        PM += 360
    return fvec[idx], PM


def main() -> dict:
    if not FRE_RESP_PATH.exists():
        raise FileNotFoundError(
            f"PyHDDBenchmark not cloned at {EXTERNAL_REPO}. "
            "Run: git clone https://github.com/macs-lab/PyHDDBenchmark.git "
            "data/external/PyHDDBenchmark"
        )

    with open(FRE_RESP_PATH, encoding="utf-8") as fh:
        d = json.load(fh)
    # Frequency vector per plot_control_system.py line 44 of the upstream repo
    fvec = np.logspace(1, np.log10(60000), 3000)

    P_mag = np.array(d["Fr_Pc_vcm_all_mag"])      # (3000, 9)
    P_pha = np.array(d["Fr_Pc_vcm_all_phase"])    # (3000, 9), RADIANS
    C_mag = np.array(d["Fr_Cd_vcm_mag"])[:, 0]    # (3000,)
    C_pha = np.array(d["Fr_Cd_vcm_phase"])[:, 0]  # (3000,) RADIANS
    F_mag = np.array(d["Fr_Fm_vcm_mag"])[:, 0]
    F_pha = np.array(d["Fr_Fm_vcm_phase"])[:, 0]

    realizations = []
    for i in range(9):
        L = (
            to_complex(P_mag[:, i], P_pha[:, i])
            * to_complex(C_mag, C_pha)
            * to_complex(F_mag, F_pha)
        )
        T = L / (1.0 + L)
        S = 1.0 / (1.0 + L)

        T_mag = np.abs(T)
        S_mag = np.abs(S)

        T_peak_idx = int(np.argmax(T_mag))
        S_peak_idx = int(np.argmax(S_mag))
        T_peak = float(T_mag[T_peak_idx])
        S_peak = float(S_mag[S_peak_idx])

        # Bandwidth: -3 dB from DC value of |T|
        bw_thresh = T_mag[0] / np.sqrt(2.0)
        bw_mask = T_mag < bw_thresh
        bw_idx = int(np.argmax(bw_mask)) if bw_mask.any() else len(fvec) - 1
        f_bw = float(fvec[bw_idx])

        f_xover, PM_deg = first_gain_crossover_phase_margin(L, fvec)

        Q_cl_est = Q_from_Ms(S_peak)

        realizations.append({
            "plant_realization": i,
            "T_peak": T_peak,
            "T_peak_f_Hz": float(fvec[T_peak_idx]),
            "S_peak": S_peak,
            "S_peak_f_Hz": float(fvec[S_peak_idx]),
            "bandwidth_Hz": f_bw,
            "first_gain_crossover_Hz": f_xover,
            "phase_margin_deg": PM_deg,
            "Q_cl_estimated_from_Ms": Q_cl_est,
        })

    # Aggregate
    Ts = np.array([r["T_peak"] for r in realizations])
    Ss = np.array([r["S_peak"] for r in realizations])
    Qs = np.array([r["Q_cl_estimated_from_Ms"] for r in realizations])
    PMs = np.array([r["phase_margin_deg"] for r in realizations])
    BWs = np.array([r["bandwidth_Hz"] for r in realizations])

    # F-002-restoration test summary
    PLANT_Q_OPEN_MIN = 12.5
    PLANT_Q_OPEN_MAX = 71.43
    Q_reduction_factor_min = PLANT_Q_OPEN_MIN / float(Qs.max())
    Q_reduction_factor_max = PLANT_Q_OPEN_MAX / float(Qs.min())

    summary = {
        "T_peak_range": [float(Ts.min()), float(Ts.max())],
        "S_peak_range_Ms": [float(Ss.min()), float(Ss.max())],
        "Q_cl_estimated_range": [float(Qs.min()), float(Qs.max())],
        "bandwidth_Hz_range": [float(BWs.min()), float(BWs.max())],
        "phase_margin_deg_range": [float(PMs.min()), float(PMs.max())],
        "phase_margin_deg_typical": float(np.median(PMs[(PMs > 0) & (PMs < 180)])),

        "plant_Q_open_range": [PLANT_Q_OPEN_MIN, PLANT_Q_OPEN_MAX],
        "closed_loop_Q_range": [float(Qs.min()), float(Qs.max())],
        "Q_reduction_factor_range": [Q_reduction_factor_min, Q_reduction_factor_max],
        "Q_reduction_factor_typical": float(np.mean(Qs)),
    }

    # F-002-restoration verdict
    qmid = float(np.mean(Qs))
    if qmid <= 0.5 + 0.05:
        verdict = "FULL_RESTORATION"
        verdict_text = "Closed-loop Q_cl lands at s-boundary (≈ 0.5). Universal SOC-attractor reading restored at plant+controller level."
    elif qmid <= 1.0:
        verdict = "PARTIAL_RESTORATION_NEAR_S"
        verdict_text = "Closed-loop Q_cl in [0.5, 1.0] — between s-boundary and Butterworth. Controller pulls plant most of the way toward chit ≈ 0."
    elif qmid <= 2.0:
        verdict = "PARTIAL_RESTORATION_MODERATE_C"
        verdict_text = f"Closed-loop Q_cl ≈ {qmid:.2f}, still c-regime but {12.5/qmid:.0f}-{71/qmid:.0f}× lower than open-loop plant. Controller pulls toward s-boundary by ~1-2 decades but stops short of critical damping. Design tradeoff between bandwidth and damping."
    else:
        verdict = "NO_RESTORATION"
        verdict_text = "Closed-loop Q_cl remains deeply c-regime. Controller does not pull substrate toward s-boundary."

    summary["f_002_restoration_verdict"] = verdict
    summary["f_002_restoration_text"] = verdict_text

    return {
        "experiment": "f002_restoration_pyhddbenchmark",
        "run_at": datetime.now(timezone.utc).isoformat(),
        "phase_c_step": 2,
        "substrate": "PyHDDBenchmark VCM plant + Cd_vcm controller + Fm_vcm multi-rate filter",
        "data_source": "data/external/PyHDDBenchmark/Fre_Resp.json (cloned 2026-05-12)",
        "claim_under_test": (
            "F-002-restoration falsifier from FOOTING 2026-05-12: when the HDD "
            "controller closes the loop on the c-regime plant, does the resulting "
            "closed-loop system land at or near Q_cl ≈ 0.5 (s-boundary)?"
        ),
        "method": (
            "Compute closed-loop transfer functions T = L/(1+L) and S = 1/(1+L) "
            "from published P, C, F frequency responses. Extract effective Q_cl "
            "via second-order approximation Q ≈ Q_from_Ms(peak |S|). 9 plant "
            "manufacturing variations characterized."
        ),
        "realizations": realizations,
        "summary": summary,
    }


def print_summary(results: dict) -> None:
    print("=" * 78)
    print(f"  F-002-restoration · PyHDDBenchmark closed-loop · Phase C step 2")
    print(f"  run {results['run_at']}")
    print("=" * 78)

    print(f"\n  {'#':>2} {'T_peak':>8} {'M_s':>7} {'f_bw_Hz':>10} {'f_x_Hz':>9} {'PM_deg':>8} {'Q_cl':>7}")
    for r in results["realizations"]:
        pm_str = f"{r['phase_margin_deg']:.2f}" if not np.isnan(r["phase_margin_deg"]) else "—"
        print(f"  {r['plant_realization']:>2} {r['T_peak']:>8.4f} {r['S_peak']:>7.4f} "
              f"{r['bandwidth_Hz']:>10.1f} {r['first_gain_crossover_Hz']:>9.1f} "
              f"{pm_str:>8} {r['Q_cl_estimated_from_Ms']:>7.4f}")

    s = results["summary"]
    print()
    print(f"  Plant Q_open (substrate-zero, F-002-contrast) : [{s['plant_Q_open_range'][0]:.1f}, {s['plant_Q_open_range'][1]:.1f}]")
    print(f"  Closed-loop Q_cl (substrate+controller)        : [{s['closed_loop_Q_range'][0]:.3f}, {s['closed_loop_Q_range'][1]:.3f}]")
    print(f"  Q reduction factor                              : {s['Q_reduction_factor_range'][0]:.1f}× to {s['Q_reduction_factor_range'][1]:.1f}×")
    print(f"  Phase margin (typical)                          : {s['phase_margin_deg_typical']:.1f}°")
    print(f"  Closed-loop bandwidth                           : ~{np.mean(s['bandwidth_Hz_range']):.0f} Hz")
    print()
    print(f"  F-002-restoration verdict : {s['f_002_restoration_verdict']}")
    print(f"  {s['f_002_restoration_text']}")
    print()


if __name__ == "__main__":
    results = main()
    output_path = REPO_ROOT / "docs" / "results" / "f002_restoration_pyhddbenchmark.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=2)
    print_summary(results)
    print(f"Wrote {output_path.relative_to(REPO_ROOT)}")
