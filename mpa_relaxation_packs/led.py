"""cdv1 reading on light-emitting diode substrate (substrate-N, drive-axis).

LEDs are the first **drive-axis substrate** in mpa-relaxation. Unlike voice
coil actuators, RLC circuits, and viscoelastic damping materials — where
c/s/r regime is determined by Q (damping) — LEDs are classified by drive
level relative to threshold V_th:

    V_drive < V_th - kT/q  → r (subthreshold, negligible current)
    V_drive ≈ V_th         → s-region (exponential I-V curvature peak, smeared)
    V_drive > V_th + kT/q  → c (sustained current, NESS at chit ≈ 0)

**The s-region is smeared by thermal noise.** Width ~kT/q ≈ 26 mV at room
temperature. This is a substrate-conditional refinement of cdv1's c/s/r:
drive-axis substrates have a *transition region* rather than a *single
critical point* (Q = 0.5). The smearing width is set by substrate physics —
kT/q for diodes, generic thermal noise for any threshold device.

**F-001 applies** via wall-plug efficiency:

    chit_max ≤ -ln(1 - η_wpe)

where η_wpe = P_optical / P_electrical at the design operating point.
LEDs are mode-separated (electrical drive → optical useful-work).

**F-003 is OPEN for drive-axis substrates.** The algebraic-exponential
signature at the s-boundary (from damping-axis substrates, F-003-rlc 2026-05-12)
may correspond to the exponential I-V curvature peak at V_th. Resolving this
is the substrate-conditional research question for v0.2.
"""
from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


# Thermal voltage at room temperature: kT/q ≈ 25.85 mV at 300 K.
THERMAL_VOLTAGE_300K_V = 0.02585


@dataclass(frozen=True)
class LED:
    """One LED instance characterized at its design operating point."""
    id: str
    vendor: str
    model: str
    chemistry: str            # red, green, blue, white, IR, UV, ...
    power_class: str          # indicator, smartphone, automotive, bulb, industrial
    V_th_V: float             # threshold forward voltage
    V_forward_design_V: float # forward voltage at design current
    I_design_mA: float        # design forward current
    eta_wpe: float            # wall-plug efficiency (optical out / electrical in)
    junction_temp_C: float    # temperature at which η_wpe was measured
    datasheet_url: Optional[str] = None
    notes: Optional[str] = None


def thermal_voltage_V(temperature_C: float = 25.0) -> float:
    """Thermal voltage kT/q in volts at a given temperature."""
    return 1.380649e-23 * (273.15 + temperature_C) / 1.602176634e-19


def regime_drive_axis(V_drive: float, V_th: float, temperature_C: float = 25.0,
                       smearing_factor: float = 1.0) -> str:
    """Classify drive-axis substrate regime from drive voltage and threshold.

    smearing_factor: half-width of s-region in units of kT/q. Default 1.0 →
    s-region is [V_th - kT/q, V_th + kT/q]. Larger smearing for noisier
    measurements or thermally agitated substrates.

    Returns "c", "s", or "r".
    """
    Vt = thermal_voltage_V(temperature_C)
    delta = smearing_factor * Vt
    if V_drive > V_th + delta:
        return "c"
    if V_drive < V_th - delta:
        return "r"
    return "s"


def chit_max_predicted(eta_wpe: float) -> float:
    """F-001 prediction: chit_max ≈ -ln(1 - η_wpe)."""
    if not (0.0 < eta_wpe < 1.0):
        raise ValueError("eta_wpe must be in (0, 1)")
    return -math.log(1.0 - eta_wpe)


def load_leds(json_path: str | Path) -> list[LED]:
    """Load LEDs from JSON.

    Expected schema (placeholder until substrate data lands):
        {
          "source": {...},
          "leds": [
            {"id": "...", "vendor": "...", "model": "...", "chemistry": "white",
             "power_class": "automotive", "V_th_V": 2.8, "V_forward_design_V": 3.1,
             "I_design_mA": 350, "eta_wpe": 0.35, "junction_temp_C": 25,
             "datasheet_url": "...", "notes": "..."},
            ...
          ]
        }
    """
    with open(json_path, encoding="utf-8") as fh:
        data = json.load(fh)
    out = []
    for entry in data["leds"]:
        out.append(LED(
            id=entry["id"],
            vendor=entry["vendor"],
            model=entry["model"],
            chemistry=entry["chemistry"],
            power_class=entry["power_class"],
            V_th_V=entry["V_th_V"],
            V_forward_design_V=entry["V_forward_design_V"],
            I_design_mA=entry["I_design_mA"],
            eta_wpe=entry["eta_wpe"],
            junction_temp_C=entry.get("junction_temp_C", 25.0),
            datasheet_url=entry.get("datasheet_url"),
            notes=entry.get("notes"),
        ))
    return out


def substrate_class_summary(leds: list[LED]) -> dict:
    """Cross-LED statistics for the substrate-class fingerprint."""
    if not leds:
        return {"n_leds": 0}
    etas = [l.eta_wpe for l in leds]
    Vths = [l.V_th_V for l in leds]
    chit_maxes = [chit_max_predicted(l.eta_wpe) for l in leds]
    return {
        "n_leds": len(leds),
        "eta_wpe_range": (min(etas), max(etas)),
        "eta_wpe_median": sorted(etas)[len(etas) // 2],
        "V_th_range_V": (min(Vths), max(Vths)),
        "chit_max_bound_range": (min(chit_maxes), max(chit_maxes)),
        "chit_max_bound_median": sorted(chit_maxes)[len(chit_maxes) // 2],
        "chemistries": sorted({l.chemistry for l in leds}),
        "power_classes": sorted({l.power_class for l in leds}),
    }


__all__ = [
    "LED",
    "THERMAL_VOLTAGE_300K_V",
    "thermal_voltage_V",
    "regime_drive_axis",
    "chit_max_predicted",
    "load_leds",
    "substrate_class_summary",
]
