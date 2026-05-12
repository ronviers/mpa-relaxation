# Reference driver — series RLC circuit (substrate-two, analytical null check)

**Substrate-class:** `series-rlc-circuit`
**Substrate-class type:** `mode-separated-or-pure-dissipative` (use-case dependent)
**F-001 applicability:** conditional — depends on declared use case (see §1)
**F-003 applicability:** YES — Q = (1/R)·√(L/C); analytical step response with closed-form algebraic factor at Q = 0.5
**Status:** v0.1 — substrate-two of mpa-relaxation. Textbook-analytical null check; F-003-rlc confirmed clean at Q = 0.5 (FOOTING entry 2026-05-12).
**Targets:** [cdv1 (compressed)](https://github.com/ronviers/mpa-atlas/blob/main/framework/cdv1_compressed.md).
**Shape:** [RFC-S §4 driver profile](https://github.com/ronviers/mpa-atlas/blob/main/rfcs/MPA-RFC-S_Scale-Management.md#4-driver-profile).

---

## 1. Substrate-class declaration

A series RLC circuit: resistor (R), inductor (L), and capacitor (C) in series, driven by a voltage source. The substrate-class is the canonical analytical second-order driven-dissipative system. Same ODE as a damped mechanical oscillator (L↔m, R↔c, 1/C↔k); used in this repo as the textbook null check for cdv1's c→s→r regime structure before applying the test machinery to noisy real-substrate data.

**Mode-separation status: use-case dependent.** Same substrate, different applications, different mode-separation status:

| Use case | Drive mode | Useful-work mode | Mode-sep status | F-001 applies? |
|---|---|---|---|---|
| LC filter / signal-processing | Electrical (input signal) | Electrical (filtered output signal) | mode-separated (different signals) | yes, but trivially η ≈ 1 in pass band |
| Tuned RLC oscillator | Electrical (drive) | Electrical (sustained oscillation at ω₀) | mode-separated | yes, η = output amplitude / input amplitude |
| Damped element (pure dissipation) | Electrical (drive) | Heat (resistor dissipation) | pure-dissipative | no — F-001 vacuous (same as viscoelastic damping) |
| F-003 null-check (this repo's use) | Step input | Step response shape | testing regime structure only | not tested; F-003 only |

Calibration records must declare the use case before F-001 applicability is determined. The default in this repo (F-003 null-check use case) does not test F-001.

## 2. Header

| Field | Value |
|---|---|
| `profile_version` | 0.1 |
| `target_rfc_versions` | RFC-S v0.2, RFC-C v0.2, cdv1 (compressed) |
| `substrate_class` | `series-rlc-circuit` |
| `substrate_class_type` | `mode-separated-or-pure-dissipative` (declared per use case) |
| `drive_mode` | electrical (voltage source) |
| `useful_work_mode` | declared per use case — see §1 |
| `f_001_applicability` | conditional on use-case declaration |
| `f_003_applicability` | yes (substrate-neutral; works under any use case) |
| `characterization_date` | 2026-05-12 |
| `authority` | mpa-relaxation v0 scaffold |
| `validation_history` | F-003-rlc confirmed 2026-05-12 (algebraic signature at Q = 0.5 exact, ratio_minimum = 0.000000). M-001 noise robustness 2026-05-12 (SNR floor 30 dB for 2σ-rule detection). |

## 3. Operating envelope

Substrate-class-conditional. Per-instance specifics declared in the calibration record.

- **Q range:** [0, ∞) in principle; physical resistor / inductor / capacitor combinations span Q ∈ [10⁻², 10⁴]. Q = 0.5 is the s-boundary; Q > 0.5 is c-regime; Q < 0.5 is r-regime.
- **Frequency range:** Natural frequency ω₀ = 1/√(LC); driven response across [0, ∞) for sinusoidal drive. Step response on time scale 1/α to 10/α where α = R/(2L).
- **Amplitude:** Linear regime assumed (passive components in linear range). Nonlinearity (saturable inductor, voltage-dependent capacitor) is out of substrate-class — those would be variants with their own profiles.

## 4. Gamut

| Axis | Substrate-declared content |
|---|---|
| Drive axis (G₀) | Voltage source × instantaneous current. Sinusoidal at ω: G₀_avg = V_rms · I_rms · cos(φ). |
| Loss axis (L) | Resistor dissipation I²·R. In pure-dissipative use case, all dissipation goes here (no useful-work). |
| Observer scale τ_obs | One period of natural oscillation (2π/ω₀) to step-response settling time (~5/α). |
| Reachable regimes | c (Q > 0.5), s (Q = 0.5), r (Q < 0.5). All reachable by varying R at fixed L, C. |
| Persistence depth | Single-mode oscillator. No persistence tower. |

**Useful-work definition (use-case dependent):**

- *LC filter*: useful_work = output power across load resistor at desired frequency.
- *Tuned oscillator*: useful_work = power delivered to load at resonance.
- *Pure damper*: no useful-work (heat is not useful); F-001 vacuous.

## 5. Translation field (substrate-native → canonical)

| Substrate-native observable | Canonical | Read |
|---|---|---|
| Capacitor voltage v_C(t) | ρ (coherence amplitude) | Direct: oscillation amplitude IS the substrate's coherent state. |
| Current I(t) | Drive ↔ loss flow | I²·R is electrical dissipation; I is the current through L's reactance. |
| R, L, C parameters | Substrate-structural parameters | ω₀ = 1/√(LC), Q = (1/R)·√(L/C). Closed-form. |
| Step response x(t) | Recovery profile, c/s/r diagnostic | Closed-form: e^(-αt)·cos(ω_d·t + φ) for Q > 0.5; (1 + αt)·e^(-αt) for Q = 0.5; double-exponential for Q < 0.5. |

## 6. Intents

Per RFC-S §3, the five intents:

| Intent | Applies? | Notes |
|---|---|---|
| I1 regime-preserving | yes | Q range spans c, s, r; regime preservation across implementations trivial. |
| I2 drive-faithful | yes | Closed-form analytical relationship between drive and response. |
| I3 capacity-preserving | N/A | Single-mode; capacity is trivial. |
| I4 persistence-preserving | N/A | Single-level. |
| I5 signature-preserving | yes | F-003-rlc confirmed the algebraic-exponential signature at Q = 0.5 exactly. |

## 7. Reference outputs

- **Step input at Q > 0.5:** exponential envelope × damped cosine. Overshoot = exp(-π/√(4Q²-1)).
- **Step input at Q = 0.5:** algebraic-exponential (1 + α·t)·e^(-α·t). No overshoot; this is the **F-003-rlc signature** that distinguishes the s-boundary qualitatively.
- **Step input at Q < 0.5:** sum of two real exponentials; slower mode dominates the long-time tail.

## 8. Metadata

Methodology: closed-form analytical, no measurement noise, no substrate-conditional artefacts. RLC's null-check role is to verify framework predictions and test machinery before applying to real-substrate data. Real circuits add: thermal noise, component tolerance (R, L, C drift), nonlinearity at large signal, parasitic capacitance/inductance, ADC quantization. None of these are in the substrate-class as characterized; they would be ingest-time corrections.

**Versioning:** v0.1 covers analytical substrate; v0.2 will land if and when a real measured RLC instance is characterized (with noise, drift, parasitics).
