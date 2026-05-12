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

Substrate backlog entries in [SOURCES.md §7](../data/sources/SOURCES.md), ranked by activation criteria:

- **§7.5 LEDs (drive-axis substrate).** First drive-axis substrate in the menagerie (vs damping-axis: actuators, RLC, materials). Tests cdv1 universality across axis types. cdv1's c→s→r might mean different things on the drive-axis vs damping-axis — the LED test reveals whether the framework is universal or axis-specific.
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
