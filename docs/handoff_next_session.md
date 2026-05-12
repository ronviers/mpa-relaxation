# Handoff — next session

## Current state (2026-05-12)

Phases A, B, C (steps 1–2), and D have substantially landed. Five substrate-classes characterized in the cross-substrate fingerprint; three driver profiles formalized with explicit mode-separation declaration. cdv1's substrate-conditional / substrate-neutral split now operationally tested and refined.

**Findings recorded in [docs/journey/FOOTING.md](journey/FOOTING.md):**

| Code | Title | Date |
|---|---|---|
| F-002-contrast | SOC attractor is substrate-conditional, not universal | 2026-05-12 |
| F-003-rlc | c→s→r recovery-tail walk confirmed in textbook substrate | 2026-05-12 |
| F-001-actuator-mdpi | chit_max bound from electromechanical coupling | 2026-05-12 |
| M-001 | F-003 algebraic-signature test has ~30 dB SNR floor | 2026-05-12 |
| F-002-restoration | Partial: controller pulls plant 1–2 decades toward s-boundary | 2026-05-12 |
| F-001-scope-limit | F-001 has substrate-class scope; F-003 more general | 2026-05-12 |
| F-003-viscoelastic | Regime structure stress test passes across material heterogeneity | 2026-05-12 |

**Substrate-class taxonomy refined:**

| Substrate-class type | F-001 applies | F-003 applies | Driver profile |
|---|---|---|---|
| Mode-separated (engine, speaker, actuator) | ✓ (with η_conversion) | ✓ | [voice-coil-actuator.md](../reference-driver/voice-coil-actuator.md) |
| Pure-dissipative (viscoelastic damping, friction, RC) | ✗ vacuous | ✓ | [viscoelastic-damping-material.md](../reference-driver/viscoelastic-damping-material.md) |
| Use-case dependent (RLC) | conditional | ✓ | [rlc-circuit.md](../reference-driver/rlc-circuit.md) |

Each driver profile declares `substrate_class_type`, `drive_mode`, `useful_work_mode`, `f_001_applicability`, `f_003_applicability` in the header. Future substrate ingests use this template; mode-separation status determines which framework invariants are applicable.

**Cross-substrate fingerprint, 5 substrate-classes:**

| Substrate | Q at design operating point | Mechanism toward chit ≈ 0 |
|---|---|---|
| IC engine at idle (mpa-engine) | chit ≈ 0 exactly | Real-time ECU feedback |
| Loudspeaker driver (Phase E shelved) | chit ≈ 0.003–0.014 | Acoustic radiation cap |
| VCA open-loop ([data/pyhddbenchmark-vcm.json](../data/pyhddbenchmark-vcm.json)) | Q ≈ 12.5–71 (deep c) | Sharp resonances by design |
| VCA closed-loop ([F-002-restoration](journey/FOOTING.md)) | Q ≈ 1.4 | Bandwidth-damping tradeoff |
| Viscoelastic damping ([F-003-viscoelastic](journey/FOOTING.md)) | Q median 0.75, s-clustering | Polymer compositional engineering |
| RLC textbook (substrate-two) | Q tunable | Resistor selection |

## What's queued

### Phase E: unshelve loudspeakers (rhetorical-substrate closing)

1. **Read loudspeaker as configured instance of substrate-zero.** Voice coil actuator + cone load + cavity. Prior research in [shelved-loudspeaker-research.md](../data/sources/shelved-loudspeaker-research.md). Adds the audiophile c→s→r vocabulary back into the rhetorical surface for external publication.
2. **F-001-loudspeaker.** Compute chit_max bound from acoustic efficiency η_acoustic ≈ 0.5–3% across the 3 verified candidates (Scan-Speak Ellipticor 21WE, Scan-Speak Classic 15W/8534T00, B&C 6CXN36). Predicted chit_max ≈ 0.003–0.014. Confirms loudspeaker substrate-class fingerprint.
3. **Driver profile for loudspeaker.** Mode-separated (electrical → acoustic). F-001 applies. F-003 applies. Substrate-class instance of voice-coil-linear-actuator with the cone+cavity load.

### Phase F: substrate menagerie expansion

#### Phase F.1: LEDs (substrate-N, drive-axis) — scaffold landed 2026-05-12, data pending

LED substrate scaffolding committed:

- [reference-driver/led.md](../reference-driver/led.md) v0.1 — substrate-class declaration, mode-separation status (mode-separated electrical → optical), F-001 applicability (yes, via η_wpe), F-003 applicability (OPEN — drive-axis method research-pending)
- [mpa_relaxation_packs/led.py](../mpa_relaxation_packs/led.py) — kernel skeleton with `regime_drive_axis(V, V_th, T)` classifier, `chit_max_predicted(η_wpe)`, `LED` dataclass

**Phase F.1 step 2 landed 2026-05-12:**

- ✓ `data/leds.json` populated with 13 cross-source-converged LED candidates spanning chemistries (UV, blue, red, deep red, yellow-green, white), power classes (indicator through industrial high-power), and regions (Western USA, Western German, Japanese, Chinese, Korean, Taiwan).
- ✓ F-001-led result: substrate-class spans widest chit_max envelope characterized — 0.084 (UV) to 0.693 (Samsung LM301B premium white). FOOTING F-001-led entry recorded.
- ✓ **PR-001 pre-registration filed 2026-05-12** — drive-axis F-003 test protocol committed BEFORE running. Key pre-registrations:
  - chit = 0 locus attaches to **L_opt** (not I-V — I-V would rederive Shockley)
  - Slow resource: **junction temperature T_j** (ms-to-s thermal feedback, not ns carrier dynamics)
  - Predicted s-window width: **n·kT/q** (30–60 mV at 300 K for n ∈ [1.2, 2.4]) — corrected from kT/q
  - Predicted ratio_minimum_value: **non-zero** floor; falsifier = sharp zero at V_th would mean drive-axis-with-thermal-smearing fails
  - Substrate-conditional parameters required before test: ideality factor n, thermal coefficient dV_th/dT_j, thermal time constant τ_th, L_opt absolute calibration

**Phase F.1 step 3 — drive-axis F-003 test, gated on substrate-conditional parameters.** Before running the Bath ABC dataset analysis or NBSDC verification, the LED instances in `data/leds.json` need ideality factor n and thermal parameters filled in. Currently `ideality_factor_n` field exists in the LED dataclass but is None for all 13 entries.

1. **Ingest ideality factor for 3-5 canonical LEDs** (Samsung LM301B, Cree XP-G3, Nichia NVSW219C-V2). From vendor datasheet semilog I-V or from published characterization papers. Typical n values for InGaN white LEDs at room temp: 1.5–2.0; AlGaInP red: 1.8–2.5; AlGaN UV: 2.0–4.0 (often higher).
2. **Verify Bath ABC dataset** ([researchdata.bath.ac.uk](https://researchdata.bath.ac.uk)). Excel format expected; commercial InGaN LEDs across 0–500 mA L-I + I-V.
3. **Run F-003-led test per PR-001 protocol.** L_opt step response across V_drive sweep, with thermal-feedback loop closed (steady-state operation, not transient pre-thermalization).
4. **Compare ratio_minimum_value behavior to pre-registered predictions.** Three branches: PASS (width 30–60 mV, ratio > 0), PARTIAL (width outside [20, 100] mV), FAIL (sharp zero — record as scope-limit on drive-axis substrates).
5. **F-003-cross-axis comparison** (if Phase F.1 step 3 lands). Does the s-region smearing generalize? Lasers have *two* drive-axis transitions (diode threshold + lasing threshold). Plasma tubes have ionization threshold. Comparing the smearing widths across these would test the substrate-class fingerprint.

#### Phase F.2: secondary substrate menagerie

Substrate backlog entries in [SOURCES.md §7](../data/sources/SOURCES.md), ranked by activation criteria:

- **§7.1 Stepper motors.** Multi-stable actuator configuration; inter-step ringing as F-003 read.
- **§7.2 Mechanical switches / debounce.** Universal microelectronics-scale tuning problem.
- **§7.3 RC circuits.** First-order endpoint of substrate-two; useful as r-regime limit reading.

### Phase A step 7 (deferred): PyHDDBenchmark η_em extraction

Modal plant parameters in plant.py don't expose (BL, R, c) per mode. To compute F-001-actuator-pyhdd, would need either (a) the underlying physical parameters from Atsumi & Yabui 2020 IEEE TIE 67(11):9184, or (b) back-computation from Fre_Resp.json under explicit assumptions. Defer unless a specific test requires it.

### Phase C step 3 (deferred, low leverage): time-domain Q_cl tightening

F-002-restoration found Q_cl ≈ 1.4 via 2nd-order M_s approximation. Tighter estimate via running PyHDDBenchmark's full simulation and measuring overshoot in position trajectory. Qualitative result is solid (Q_cl is definitively not 0.5); decimal-point tightening is low-leverage.

## Gotchas surfaced (carried forward)

- **Multimodal substrates.** PyHDDBenchmark VCM is 16-mode + PZT 8-mode. Per-mode Q, per-mode chit. Kernel handles modal sums (`mpa_relaxation_packs/voice_coil.py:Actuator.modes` list).
- **Q definition.** Q = ω₀/(2γ) is the canonical second-order quality factor. For viscoelastic damping: Q = 1/tan δ at resonance. Both consistent: Q = 0.5 is critical damping (s-boundary).
- **chit ↔ Q axes.** Q is structural (recovery profile). chit is operating-point order parameter (lives at 0 at SOC attractor). Different axes; F-001 is a chit-axis bound, F-003 is a Q-axis regime classifier.
- **Mode-separation precondition for F-001.** Each substrate must declare drive_mode and useful_work_mode. If they share a channel (pure-dissipative substrates), F-001 chit_max bound is vacuous; F-003 still applies.
- **Open-loop vs closed-loop.** PyHDDBenchmark exposes both. Open-loop: substrate plant alone. Closed-loop: plant + controller. F-002 partial restoration at the closed-loop level; full restoration requires substrate-conditional design pressure (engines have it; HDDs don't because design tradeoff is two-sided).
- **Phase units in FRF data.** PyHDDBenchmark Fre_Resp.json phases are in **radians**, not degrees. Future FRF ingests: check units before computing complex transfer functions.
- **F-003 SNR floor.** ~30 dB for 2σ-rule detection of the algebraic signature in noisy data. Future F-003 tests on real-substrate data must report measurement SNR.

## Coordinates

- Upstream framework: [mpa-atlas/framework/cdv1_compressed.md](https://github.com/ronviers/mpa-atlas/blob/main/framework/cdv1_compressed.md)
- Validator tool: [mpa-bridge](https://github.com/ronviers/mpa-bridge)
- Substrate-one (cited, frozen): [mpa-engine](https://github.com/ronviers/mpa-engine)
- Sibling substrate repos: [mpa-brain](https://github.com/ronviers/mpa-brain), [mpc-glass](https://github.com/ronviers/mpc-glass)
