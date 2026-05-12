# Reference driver — light-emitting diode (substrate-N, drive-axis)

**Substrate-class:** `light-emitting-diode`
**Substrate-class type:** `mode-separated` + `drive-axis` (regime walks via drive level, not damping)
**F-001 applicability:** YES — η_wpe = optical_power_out / electrical_power_in; chit_max ≤ -ln(1 - η_wpe)
**F-003 applicability:** PRE-REGISTERED (PR-001 in FOOTING) — protocol committed before test runs. The chit = 0 locus attaches to **L_opt (optical output)**, not I-V. Slow resource is **junction temperature T_j** (ms-to-s), not carrier dynamics (ns). Predicted s-window width: **n·kT/q** (≈ 30–60 mV at 300 K, where n is the ideality factor ∈ [1.2, 2.4]).
**chit = 0 observable:** L_opt (radiated optical power). The I-V curve is monotone exponential with no sharp electrical knee; using I-V alone would rederive the Shockley equation. L_opt has a real regime transition: ≈ 0 below threshold (r-regime), scales with I above threshold (c-regime).
**Slow resource for F-003:** junction temperature T_j. Self-heating feedback (more I → more T_j → V_th drops → more I) provides the ms-to-s timescale that makes drive-axis-with-thermal-smearing distinguishable from "diodes are exponential."
**Status:** v0.2 — substrate-N of mpa-relaxation. Pre-registration filed 2026-05-12 in [FOOTING PR-001](../docs/journey/FOOTING.md). v0.1 to v0.2 changes: ideality factor n added as substrate-conditional parameter; junction temperature declared as slow resource; L_opt declared as chit = 0 attachment observable; predicted s-window width corrected from kT/q to nkT/q.
**Targets:** [cdv1 (compressed)](https://github.com/ronviers/mpa-atlas/blob/main/framework/cdv1_compressed.md).
**Shape:** [RFC-S §4 driver profile](https://github.com/ronviers/mpa-atlas/blob/main/rfcs/MPA-RFC-S_Scale-Management.md#4-driver-profile).

---

## 1. Substrate-class declaration

A light-emitting diode (LED): a semiconductor p-n junction biased in forward direction such that electron-hole pair recombination emits incoherent photons. The substrate's identifying observable is a **threshold forward voltage V_th** (typically 1.7 V red, 2.1 V green, 3.3 V blue/white, 4 V UV) below which essentially no current flows. Above V_th, current rises exponentially per the Shockley diode equation, and photon emission scales with the recombination rate.

The substrate-class spans indicator LEDs (mW power range), smartphone-flash LEDs (1–2 W), automotive LEDs (2–10 W), illumination LEDs in bulbs/luminaires (5–20 W), and high-power industrial LEDs (>20 W). All read through the same cdv1 primitives.

**Mode-separation status: mode-separated.** Drive mode: electrical (forward voltage × forward current). Useful-work mode: optical (radiated photon power, measurable as luminous flux or radiometric watts). The two modes share no overlap by substrate construction — electrical power injection produces emission, electrical loss (resistive drop across series resistance) is dissipated as junction heat. F-001 applies with η_wpe (wall-plug efficiency); chit_max ≤ -ln(1 - η_wpe).

**Drive-axis substrate.** Unlike voice coil actuators, RLC circuits, and viscoelastic damping materials — where the c/s/r regime is determined by **Q (damping)** — LEDs determine regime by **drive level relative to threshold V_th**:

| Regime | Drive condition | Substrate state (observable on L_opt) |
|---|---|---|
| r-regime | V_drive < V_th − n·kT/q | L_opt ≈ 0 (sub-threshold spontaneous emission only). No sustained NESS. |
| s-region | V_drive ≈ V_th ± n·kT/q | L_opt transitions from ≈ 0 to scaling with I. Thermal-feedback-smeared. |
| c-regime | V_drive > V_th + n·kT/q | L_opt scales with I. NESS at chit ≈ 0 by power balance. |

**The s-region is smeared** with width **n·kT/q** where n is the ideality factor ∈ [1, 2] typical. At 300 K with n ∈ [1.2, 2.4]: width 30–60 mV. The kT/q-only framing in v0.1 was incomplete — n must be characterized per LED instance. The "chit-slope universality" dchit/dV = q/kT is exact only for n = 1; n > 1 widens the smearing.

**The chit = 0 locus attaches to L_opt, not I-V.** Critical methodological point. The I-V curve is monotone exponential with no sharp electrical knee — there is no "regime transition" in I-V; using it would rederive the Shockley equation and add nothing. The L_opt curve has a real regime transition: ≈ 0 below threshold, scales with I above. The optical threshold is set by photon energy / charge, not by junction barrier; it differs from the electrical-current onset. **Pick L_opt upfront and stay on it** (PR-001).

**Slow resource: junction temperature T_j.** Damping-axis substrates carry their slow resource intrinsically (the RLC mode IS the slow resource). LEDs at DC are nearly slow-resource-free; carrier dynamics are nanoseconds. The natural slow resource is T_j, which gives ms-to-s feedback: more I → more dissipated power → T_j rises → V_th drops (negative thermal coefficient) → more I. Without this thermal-feedback coupling in the test protocol, the s-window will look like a smooth I-V curve and we can't tell drive-axis smearing apart from "diodes are exponential."

Substrate excludes: laser diodes (have a *second* threshold beyond the LED I-V threshold — the lasing threshold — at which coherent emission emerges; mathematically richer substrate-class with both drive-axis and damping-axis structure). Photodiodes (reverse-biased; different substrate-class). LED lighting systems with drivers and thermal management are *configured instances* of the LED substrate plus auxiliary substrates.

## 2. Header

| Field | Value |
|---|---|
| `profile_version` | 0.2 |
| `target_rfc_versions` | RFC-S v0.2, RFC-C v0.2, cdv1 (compressed) |
| `substrate_class` | `light-emitting-diode` |
| `substrate_class_type` | `mode-separated` + `drive-axis` |
| `drive_mode` | electrical (V_forward × I_forward) |
| `useful_work_mode` | optical (radiated photon power, L_opt) |
| `chit_zero_attachment_observable` | L_opt (NOT I-V — I-V is monotone exponential with no regime transition) |
| `slow_resource` | junction temperature T_j (ms-to-s thermal feedback) |
| `f_001_applicability` | yes (η_wpe = optical_out / electrical_in; chit_max ≤ -ln(1 - η_wpe)) |
| `f_003_applicability` | PRE-REGISTERED (FOOTING PR-001) — protocol committed before run; predicted s-window width n·kT/q (30–60 mV at 300 K); predicted ratio_minimum_value > 0 (non-zero floor); falsifier: sharp zero at V = V_th |
| `regime_classifier_axis` | drive-level (V vs V_th) — distinguished from damping-axis substrates that classify by Q |
| `substrate_conditional_parameter_n` | ideality factor n ∈ [1, 2]; must be measured per instance (semilog I-V fit) |
| `substrate_conditional_parameter_thermal_coefficient` | dV_th/dT_j (mV/°C); vendor-published |
| `substrate_conditional_parameter_thermal_time_constant` | τ_th (ms); thermal resistance × heat capacity |
| `characterization_date` | 2026-05-12 (v0.2) |
| `authority` | mpa-relaxation v0 scaffold; PR-001 pre-registration 2026-05-12 |
| `validation_history` | F-001-led bound test 2026-05-12 (chit_max range 0.084 to 0.693 across 13 instances). F-003-led pending step-response data; PR-001 protocol committed in advance. |

## 3. Operating envelope

Substrate-class-conditional. Per-LED specifics declared in the calibration record.

- **Forward voltage range:** [0, V_max] where V_max is the absolute maximum forward voltage rating. Useful operating range typically [V_th, V_th + 1 V].
- **Forward current range:** [I_th, I_max]. I_th typically μA-range; I_max typically 100 mA (indicator) to 5 A (high-power industrial).
- **Junction temperature range:** Typical [-40°C, 125°C]. V_th drops ~2 mV/°C with temperature; η_wpe drops with temperature (efficiency droop).
- **Useful drive region:** the c-regime, V > V_th + a few kT/q. Outside this region, the substrate is either subthreshold (r) or beyond max ratings.

## 4. Gamut

| Axis | Substrate-declared content |
|---|---|
| Drive axis (G₀) | Electrical power input = V_forward × I_forward. Below V_th, G₀ ≈ 0. Above V_th, G₀ ≈ V × I_design, typically 100 mW to 20 W per device. |
| Loss axis (L) | Sum of: (a) series resistance loss I²·R_s (junction + bond wires), (b) non-radiative recombination (heat in junction), (c) optical losses in package (absorption, total internal reflection). L = G₀ - P_optical. |
| Observer scale τ_obs | Free-carrier lifetime (nanoseconds) to thermal time constant (milliseconds). Canonical τ_obs for cdv1 reading: many free-carrier lifetimes, well below thermal time constant. |
| Reachable regimes | r (V < V_th − kT/q), s-region (V ≈ V_th ± kT/q), c (V > V_th + kT/q). All three reachable by sweeping drive voltage. |
| Persistence depth | Single-level — LEDs do not tower in the cdv1 §Heat-tax sense. |

**F-001 applicability declaration:** YES. Mode-separated (electrical → optical). Wall-plug efficiency η_wpe is a well-defined substrate-class observable: optical power emitted divided by electrical power consumed. For typical LEDs at design operating point: η_wpe ranges 0.10 (low-end indicator) to 0.50 (high-efficiency white). chit_max ranges 0.105 to 0.693.

## 5. Translation field (substrate-native → canonical)

| Substrate-native observable | Canonical | Read |
|---|---|---|
| Forward voltage V(t) | Drive amplitude | Direct: V is the drive-axis position relative to V_th. |
| Forward current I(t) | Drive flow | Direct: above V_th, I is exponential in V (Shockley). |
| Threshold voltage V_th | Substrate s-boundary location | Substrate-class-conditional. Reading: regime classifier draws boundaries at V_th ± kT/q. |
| Wall-plug efficiency η_wpe | F-001 parameter | Direct: chit_max ≤ -ln(1 - η_wpe). |
| Junction temperature T_j | Substrate-thermal-state | Modulates V_th (negative TC) and η_wpe (negative TC). Calibration records declare T_j. |
| Optical power P_opt | Useful-work output | P_opt = η_wpe × P_electrical (at sustained operation). |

## 6. Intents

Per RFC-S §3, the five intents:

| Intent | Applies? | Notes |
|---|---|---|
| I1 regime-preserving | yes (with drive-axis adaptation) | Regime classification by V vs V_th instead of Q vs 0.5. |
| I2 drive-faithful | yes | Per-LED calibration records preserve V_th, V_f, I_design, η_wpe. |
| I3 capacity-preserving | partial | Single LED is single-mode. LED arrays (string + parallel configurations) read as multi-mode and may need substrate-class refinement. |
| I4 persistence-preserving | N/A | Single-level. |
| I5 signature-preserving | OPEN | Drive-axis F-003 signature is research-pending. The "algebraic factor at s-boundary" from RLC may correspond to the exponential I-V curvature peak at V_th — but this is a hypothesis, not a confirmed reading. |

## 7. Reference outputs

Canonical test inputs and expected substrate responses, for round-trip validation:

- **V_drive = V_th:** Substrate sits at the s-region center. I rises exponentially with curvature peak.
- **V_drive = V_th + 50 mV (~ 2 kT/q):** Substrate clearly in c-regime. Sustained current flow.
- **V_drive = V_th − 50 mV:** Substrate clearly in r-regime. Negligible current.
- **Substrate-class chit reading at sustained drive in c-regime:** chit ≈ 0 by power balance (G₀ = L + P_optical, and at steady state all incoming electrical power goes somewhere). The non-trivial chit_max bound is the optical-emission efficiency η_wpe.

## 8. Metadata

Methodology: vendor datasheets (Cree, Lumileds, Osram, Nichia, Citizen, Toshiba, Honglitronic, Refond, Everlight, MLS, Sanan, Samsung, LG Innotek, Seoul Semiconductor, Surya, Halonix, Epistar). Standardized measurement geometries: integrating sphere for optical power, Kelvin probes for V_f, controlled-temperature heat sink for junction temperature.

**Known limitations:**

- Single-point characterization (one I_design, one η_wpe) hides current-dependent efficiency (droop). Full characterization: η_wpe(I) sweep.
- Vendor methodology not always standardized — Chinese low-cost indicator LEDs often lack rigorous photometric data; cross-substrate calibration requires checking test conditions.
- Aging effects (lumen depreciation, LED-driver coupling drift) shift V_f and η_wpe over device lifetime. Calibration records should declare device-age state.
- LED arrays vs single LEDs: arrays in series add V_f values (and shift effective V_th); arrays in parallel share current. Substrate-class scope: single-LED here; arrays earn their own driver profile when characterized.

**Versioning:** v0.1 is the substrate-class scaffold. v0.2 lands when the first calibration record (one canonical LED from each of: indicator, smartphone-flash, automotive, bulb, high-power-industrial) populates the gamut. v0.3 unfolds the η_wpe(I, T_j) surface for at least one canonical LED. v1.0 lands when drive-axis F-003 method is settled and tested against substrate data.

## Drive-axis F-003 protocol (PR-001 pre-registered, 2026-05-12)

cdv1's c→s→r structure was confirmed in damping-axis substrates via the algebraic-exponential signature at Q = 0.5 (FOOTING F-003-rlc, 2026-05-12). For drive-axis substrates, the protocol is now pre-registered in [FOOTING PR-001](../docs/journey/FOOTING.md). Summary:

**Observable.** L_opt step response (NOT I-V).

**Drive variable.** Step V_drive through V_th. Plot ratio_minimum_value as function of (V_drive − V_th) / V_th.

**Slow resource.** Junction temperature T_j (ms-to-s feedback loop). Without thermal coupling in the protocol, drive-axis-with-thermal-smearing is indistinguishable from "diodes are exponential."

**Candidate envelopes.** "Pure thermal exp": L_opt(t) = L_steady · (1 − e^(−t/τ)). "Algebraic thermal": L_opt(t) = L_steady · (1 − (1 + t/τ)·e^(−t/τ)). Mirror F-003-rlc structure.

**Predicted s-window width.** n·kT/q ≈ 30–60 mV at 300 K for n ∈ [1.2, 2.4].

**Predicted ratio_minimum_value.** *Non-zero* minimum across the sweep, floor set by n·kT/q against substrate's natural drive scale. **Falsifier:** if ratio_minimum hits zero at V = V_th (sharp like RLC), drive-axis-with-thermal-smearing fails — cdv1 c→s→r doesn't extend cleanly to drive-axis substrates.

**Pre-registered actions on outcome.** Three branches: PASS (width 30–60 mV, ratio > 0), PARTIAL (width outside [20, 100] mV, record actual slow-resource), FAIL (sharp zero — record as scope-limit on framework).

**Substrate-conditional parameters needed before running test.** Ideality factor n per LED (from semilog I-V fit), thermal coefficient dV_th/dT_j (vendor-published), thermal time constant τ_th (R_th × C_th), L_opt absolute calibration. These must be in the LED calibration record before F-003-led can produce an interpretable result.
