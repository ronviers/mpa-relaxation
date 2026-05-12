# Handoff — next session

## Current state (end of session 2026-05-12)

Six substrate-classes characterized end-to-end. cdv1's substrate-conditional/substrate-neutral split is operationally tested and refined. F-001 demoted from universal to substrate-conditional (applies only to mode-separated substrates). F-002 retracted as universal and replaced by F-002-contrast + F-002-restoration. F-003 elevated to substrate-neutral (passes across mode-separated, pure-dissipative, and pre-registered for drive-axis). The substrate-class API formalizes mode-separation declaration and F-001/F-003 applicability per driver profile.

**Findings recorded in [docs/journey/FOOTING.md](journey/FOOTING.md):**

| Code | Title | Verdict |
|---|---|---|
| F-002-contrast | SOC attractor is substrate-conditional, not universal | confirmed |
| F-003-rlc | c→s→r recovery-tail walk confirmed in textbook substrate | PASS (exact zero at Q=0.5) |
| F-001-actuator-mdpi | chit_max bound from electromechanical coupling | confirmed (bound; not measured) |
| M-001 | F-003 algebraic-signature test has ~30 dB SNR floor | methodological |
| F-002-restoration | Partial: controller pulls plant 1–2 decades toward s-boundary | PARTIAL (Q_cl ≈ 1.4, not 0.5) |
| F-001-scope-limit | F-001 has substrate-class scope; F-003 more general | confirmed |
| F-003-viscoelastic | Regime structure passes substrate-class heterogeneity | PASS (all 3 regimes within single substrate-class) |
| F-001-led | LEDs span widest chit_max envelope of any substrate-class | confirmed (0.084 to 0.693) |
| PR-001 | Drive-axis F-003 protocol pre-registration | committed; test pending data |

**Substrate-class taxonomy (formalized in driver profiles):**

| Substrate-class | Type | F-001 | F-003 | Driver profile |
|---|---|---|---|---|
| IC engines (cited mpa-engine) | mode-separated | ✓ | not tested | (cited from mpa-engine) |
| Voice coil actuators | mode-separated | ✓ confirmed | not tested directly | [voice-coil-actuator.md](../reference-driver/voice-coil-actuator.md) v0.2 |
| RLC | use-case dependent | conditional | ✓ confirmed (exact) | [rlc-circuit.md](../reference-driver/rlc-circuit.md) v0.1 |
| Viscoelastic damping | pure-dissipative | ✗ scope-limit | ✓ stress-test PASS | [viscoelastic-damping-material.md](../reference-driver/viscoelastic-damping-material.md) v0.1 |
| LEDs (drive-axis) | mode-separated + drive-axis | ✓ confirmed (widest envelope) | PRE-REGISTERED (PR-001) | [led.md](../reference-driver/led.md) v0.2 |
| Loudspeakers | mode-separated | shelved | shelved | [shelved-loudspeaker-research.md](../data/sources/shelved-loudspeaker-research.md) |

**Cross-substrate fingerprint, 6 substrate-classes:**

| Substrate | Operating chit / Q at design | Mechanism toward chit ≈ 0 |
|---|---|---|
| IC engine at idle (mpa-engine) | chit ≈ 0 exactly | Real-time ECU feedback |
| Loudspeaker (shelved) | chit ≈ 0.003–0.014 | Acoustic radiation cap |
| Voice coil actuator open-loop | Q ≈ 12.5–71 | None — externally damped |
| Voice coil actuator closed-loop | Q ≈ 1.4 | Bandwidth-damping tradeoff |
| Viscoelastic damping | Q median 0.75, s-cluster | Polymer compositional engineering |
| RLC | Q tunable | Resistor selection |
| **LEDs (drive-axis)** | **chit_max ≤ 0.084–0.693** | **chemistry + carrier injection physics** |

## What's queued

### Phase F.1 step 3 — drive-axis F-003 test (PR-001 protocol)

**Prerequisites done:** substrate-conditional parameters (ideality factor n, thermal coefficient dV_th/dT_j, thermal time constant τ_th) populated for all 13 LEDs in [data/leds.json](../data/leds.json). Substrate-class predicted s-window width range: 41.4–77.6 mV at 300 K (typical InGaN/AlGaInP cluster 41–52 mV; Toyoda UV outlier at 77.6 mV with n=3.0).

**Remaining gate:** L_opt step-response data. The pre-registered protocol requires measured L_opt(t) under V_drive step input across the V_th window with thermal-feedback loop closed. Path forward:

1. **Verify Bath ABC-recombination dataset** ([researchdata.bath.ac.uk](https://researchdata.bath.ac.uk)). Excel format; commercial InGaN LEDs across 0–500 mA L-I + I-V. Direct test candidate.
2. **Verify NBSDC China LED Optoelectronic Characteristics** ([nbsdc.cn](https://www.nbsdc.cn)). 4.42 MB downloadable; full I-V, EQE, spectral curves.
3. **Run F-003-led per PR-001 protocol** when data lands. Mirror F-003-rlc step-by-step (sweep variable swapped from Q to (V−V_th)/V_th, observable swapped from capacitor voltage to L_opt). Predicted outcomes (pre-registered):
   - **PASS**: ratio_minimum > 0, width 30–60 mV (typical) or up to 78 mV (UV with high n). Drive-axis-with-thermal-smearing confirmed; cdv1 c→s→r extends to drive-axis substrates.
   - **PARTIAL**: width outside [20, 100] mV. Record actual slow-resource in calibration record.
   - **FAIL**: sharp zero at V = V_th (like RLC). Drive-axis-with-thermal-smearing fails; record as scope-limit on framework.

### Phase E — unshelve loudspeakers (rhetorical closure)

Read loudspeaker as configured instance of substrate-zero (voice coil actuator + cone + cavity load). Prior research at [shelved-loudspeaker-research.md](../data/sources/shelved-loudspeaker-research.md): 8 raw-driver candidates from Voice Coil magazine, SEAS A26 + Variovent tunable testbed, 3 efficiency values giving chit_max ≈ 0.003–0.014. Adds audiophile c→s→r vocabulary and carb-tuning everyman analogy back into the rhetorical surface for external publication.

### Phase F.2 — substrate menagerie expansion

Substrate backlog in [SOURCES.md §7](../data/sources/SOURCES.md):

- **§7.1 Stepper motors** — multi-stable actuator configuration; inter-step ringing as F-003 read.
- **§7.2 Mechanical switches / debounce** — universal microelectronics-scale tuning problem.
- **§7.3 RC circuits** — first-order endpoint of substrate-two; r-regime limit reading.
- **Lasers** — both drive-axis (pump threshold) AND damping-axis (cavity Q). Tests whether cdv1 universality holds across simultaneous axis-stacking. Original substrate cdv1 was derived from; recovery, not reach.

## Gotchas surfaced (carry forward)

- **Multimodal substrates.** PyHDDBenchmark VCM is 16-mode + PZT 8-mode. Per-mode Q, per-mode chit. Kernel handles modal sums.
- **Q definition.** Q = ω₀/(2γ) is canonical second-order quality factor. For viscoelastic damping: Q = 1/tan δ. Critical damping at Q = 0.5.
- **chit ↔ Q axes.** Q is structural (recovery profile). chit is operating-point order parameter. Different axes; F-001 is chit-axis bound, F-003 is Q-axis (or drive-level-axis) regime classifier.
- **Mode-separation precondition for F-001.** Driver profile declares drive_mode and useful_work_mode. If they share a channel (pure-dissipative), F-001 vacuous.
- **Open-loop vs closed-loop.** PyHDDBenchmark exposes both. F-002 partial restoration at closed-loop level.
- **Phase units in FRF data.** PyHDDBenchmark Fre_Resp.json phases are in **radians**, not degrees. Future FRF ingests: check units.
- **F-003 SNR floor.** ~30 dB for 2σ-rule detection of algebraic signature in noisy data (M-001).
- **Drive-axis-vs-damping-axis distinction.** cdv1 c→s→r holds on both, but the *observable* differs. Damping-axis: Q at structural resonance. Drive-axis: drive level relative to threshold V_th, with s-region smeared by n·kT/q (NOT kT/q — ideality factor n matters).
- **Pre-registration discipline.** PR-series in FOOTING is parallel to F-series. PR entries lock in protocols before runs. PR-001 commits drive-axis F-003 predictions and falsifier; future-Claude cannot move the goalpost.
- **LED η_wpe in datasheets.** Commonly conflated with luminous efficacy. Real white-LED η_wpe at peak is typically 0.40–0.55 for premium 2026 parts; numbers >0.55 in datasheets typically reflect luminous-efficacy not divided by LER.
- **LED substrate-class is internally heterogeneous in F-001.** Chemistry sets η_wpe more than power class does. v0.2 RFC-S refinement could add a chemistry-subclass field below substrate-class.

## Coordinates

- Upstream framework: [mpa-atlas/framework/cdv1_compressed.md](https://github.com/ronviers/mpa-atlas/blob/main/framework/cdv1_compressed.md)
- Validator tool: [mpa-bridge](https://github.com/ronviers/mpa-bridge)
- Substrate-one (cited, frozen): [mpa-engine](https://github.com/ronviers/mpa-engine)
- Sibling substrate repos: [mpa-brain](https://github.com/ronviers/mpa-brain), [mpc-glass](https://github.com/ronviers/mpc-glass)
