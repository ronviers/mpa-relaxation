"""cdv1 reading on light-emitting diode substrate (substrate-N, drive-axis).

v0.2 update (2026-05-12, per PR-001 pre-registration in FOOTING):
- Smearing width corrected from kT/q to **n·kT/q** where n is ideality factor.
- Slow resource declared: **junction temperature T_j** (ms-to-s feedback).
- chit = 0 locus attaches to **L_opt** (optical output), NOT I-V.

LEDs are the first **drive-axis substrate** in mpa-relaxation. Unlike voice
coil actuators, RLC circuits, and viscoelastic damping materials — where
c/s/r regime is determined by Q (damping) — LEDs are classified by drive
level relative to threshold V_th, with the s-region smeared by thermal
noise weighted by ideality factor n:

    V_drive < V_th - n·kT/q  → r (subthreshold, L_opt ≈ 0)
    V_drive ≈ V_th           → s-region (smeared transition zone, width n·kT/q)
    V_drive > V_th + n·kT/q  → c (sustained current and L_opt, NESS at chit ≈ 0)

**Ideality factor n** is substrate-conditional. n = 1 for ideal diffusion-
limited diode (Shockley); n = 2 for recombination-current-limited; real
LEDs sit in n ∈ [1, 2]. At 300 K with n ∈ [1.2, 2.4]: smearing width 30–60
mV. The "chit-slope universality" framing dchit/dV = q/kT is exact ONLY
for n = 1; n > 1 widens the smearing to n·kT/q. n must be measured per
LED instance (semilog I-V fit).

**Slow resource for F-003: junction temperature T_j.** Damping-axis
substrates carry their slow resource intrinsically (the RLC mode IS the
slow resource at ω_0). LEDs at DC are nearly slow-resource-free; carrier
dynamics are nanoseconds. The natural slow resource is T_j, giving ms-to-s
feedback: more I → more dissipated power → T_j rises → V_th drops → more
I. Without time-resolved thermal coupling in the test protocol, the
s-window will look like a smooth I-V curve and the test cannot distinguish
"drive-axis-with-thermal-smearing" from "diodes are exponential."

**chit = 0 attachment: L_opt (optical output), NOT I-V.** The I-V curve
is monotone exponential with no sharp electrical knee. The optical output
has a real regime transition: ≈ 0 below threshold (r), scales with I
above threshold (c). Using I-V alone would rederive the Shockley equation
and add nothing — pick L_opt upfront and stay on it.

**F-001 applies** via wall-plug efficiency:

    chit_max ≤ -ln(1 - η_wpe)

where η_wpe = P_optical / P_electrical at the design operating point.
LEDs are mode-separated (electrical drive → optical useful-work).

**F-003 PRE-REGISTERED (PR-001 in FOOTING).** The protocol mirrors
F-003-rlc with sweep variable swapped from Q to (V − V_th)/V_th and
observable swapped from capacitor voltage to L_opt. Predicted: non-zero
ratio_minimum_value across the sweep, floor set by n·kT/q. Falsifier:
sharp zero at V = V_th (like RLC) would mean drive-axis-with-thermal-
smearing fails as a framework extension.
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
    """One LED instance characterized at its design operating point.

    v0.2 fields added 2026-05-12 (PR-001 pre-registration):
    - ideality_factor_n: dimensionless n in nkT/q smearing-width prediction
    - thermal_coefficient_V_th_mV_per_C: dV_th/dT_j
    - thermal_time_constant_ms: τ_th = R_th × C_th
    """
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
    # PR-001 substrate-conditional parameters (None if not yet characterized):
    ideality_factor_n: Optional[float] = None
    thermal_coefficient_V_th_mV_per_C: Optional[float] = None
    thermal_time_constant_ms: Optional[float] = None


def thermal_voltage_V(temperature_C: float = 25.0) -> float:
    """Thermal voltage kT/q in volts at a given temperature."""
    return 1.380649e-23 * (273.15 + temperature_C) / 1.602176634e-19


def regime_drive_axis(V_drive: float, V_th: float, temperature_C: float = 25.0,
                       ideality_factor_n: float = 1.0,
                       smearing_factor: float = 1.0) -> str:
    """Classify drive-axis substrate regime from drive voltage and threshold.

    Per PR-001 pre-registration: smearing width is **n·kT/q**, not kT/q.
    The ideality_factor_n parameter sets the substrate-conditional smearing
    width. n = 1 is the Shockley-ideal limit; real LEDs have n ∈ [1, 2].

    smearing_factor: additional half-width multiplier on n·kT/q. Default 1.0 →
    s-region is [V_th - n·kT/q, V_th + n·kT/q]. Increase for substrates with
    additional smearing sources beyond ideality-factor thermal noise.

    Returns "c", "s", or "r".
    """
    Vt = thermal_voltage_V(temperature_C)
    delta = smearing_factor * ideality_factor_n * Vt
    if V_drive > V_th + delta:
        return "c"
    if V_drive < V_th - delta:
        return "r"
    return "s"


def smearing_width_nkT_q(ideality_factor_n: float, temperature_C: float = 25.0) -> float:
    """Predicted s-window half-width on drive-axis substrate, in volts.

    Per PR-001 pre-registration: s-window width = n·kT/q where n is the
    ideality factor. At 300 K (27°C) with n = 1: 25.85 mV. With n = 2: 51.7 mV.
    Real LEDs at room temp with n ∈ [1.2, 2.4]: predicted width 30–60 mV.

    This is the substrate-conditional drive-axis analog of RLC's
    s-band-around-Q=0.5 width (typically 0.02 in Q space).
    """
    return ideality_factor_n * thermal_voltage_V(temperature_C)


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
            ideality_factor_n=entry.get("ideality_factor_n"),
            thermal_coefficient_V_th_mV_per_C=entry.get("thermal_coefficient_V_th_mV_per_C"),
            thermal_time_constant_ms=entry.get("thermal_time_constant_ms"),
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
    "smearing_width_nkT_q",
    "chit_max_predicted",
    "load_leds",
    "substrate_class_summary",
]
