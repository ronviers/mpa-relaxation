# Handoff — next session

## Current state (2026-05-12, substrate-zero stacked: MDPI 2020 + PyHDDBenchmark)

Substrate-zero pivot from loudspeakers to voice coil linear actuators landed 2026-05-11. Three outside-model research runs ingested 2026-05-12. Top candidate (MDPI 2020) verified. Second candidate (PyHDDBenchmark / IEEJ HDD positioning benchmark) verified via GitHub. **Substrate zero now stacked across two complementary instances:**

| Instance | Q range | Regime | Provides |
|---|---|---|---|
| MDPI Actuators 2020, 9(1):8 (bare cantilever VCA, Al + plastic bobbin) | ≈ 0.033 and 0.39 | r (overdamped) | Full EM/mechanical parameters, two configured instances with eddy-current damping tuning, step responses in Figures 12–13 |
| PyHDDBenchmark / IEEJ HDD plant | 12.5 to 71 (VCM, 16 modes); 1.67 to 62.5 (PZT, 8 modes) | c (underdamped) | Modal plant model from real HDD measurements, `Fre_Resp.json` frequency-response data, `Data_RRO.txt` time-domain disturbance. Open source ([macs-lab/PyHDDBenchmark](https://github.com/macs-lab/PyHDDBenchmark)) |

Combined: ~26 (Q, ω) data points across the substrate-class spanning r-regime and c-regime, two physical substrates. Distilled signal in [data/sources/actuator-research-cross-reference.md](../data/sources/actuator-research-cross-reference.md).

**Substrate roadmap restructure:** RLC (was Phase D substrate-two) is **pulled forward to Phase B** to handle the F-003 c→s→r walk. Reasoning: PyHDDBenchmark is a fixed plant (not tunable), MDPI 2020 spans only r-regime, and neither substrate gives a continuous Q walk. RLC delivers a clean tunable Q (vary R) and the closed-form textbook step response. Treating RLC as both the substrate-2 null check AND the F-003 walk vehicle doubles its work without compromising either role.

Loudspeakers shelved with explicit commitment to return in Phase F as a *configured instance* of substrate-zero. Prior research at [data/sources/shelved-loudspeaker-research.md](../data/sources/shelved-loudspeaker-research.md).

## What's queued

### Phase A: substrate-zero stack end-to-end (MDPI 2020 + PyHDDBenchmark)

1. **Driver profile already drafted.** [reference-driver/voice-coil-actuator.md](../reference-driver/voice-coil-actuator.md) v0.1. Updates when first calibration record lands.
2. **Extract MDPI 2020 data to JSON.** `data/mdpi-2020-cantilever-vca.json`: parameters from Table 2 (m, c (Al/plastic), k, R, L, BL), step-response traces digitized from Figures 12–13. Two configured instances → two calibration records.
3. **Extract PyHDDBenchmark data to JSON.** `data/pyhddbenchmark-vcm.json` and `data/pyhddbenchmark-pzt.json`: modal parameters (ω_modal, ζ_modal, kappa_modal) from `plant.py`; `Fre_Resp.json` ingested directly. PyHDDBenchmark is multimodal — per-mode Q values, per-mode chit treatments.
4. **Implement `mpa_relaxation_packs.voice_coil`.** Loader + chit reading: G₀ = V·I or I²·R + BL·v·I, L = sum of decomposed losses, chit = ln(G₀/L). Regime classification from Q (γ = ω₀/(2Q), ω_d = ω₀·√(1-1/(4Q²)) — c-regime if Q > 0.5, s at Q = 0.5, r if Q < 0.5). Per-mode chit for multimodal substrates.
5. **Calibration records.** `reference-driver/mdpi-2020-{al,plastic}-bobbin-calibration.json` and `reference-driver/pyhddbenchmark-{vcm,pzt}-calibration.json` per RFC-C §2.
6. **Smoke experiment.** `experiments/chit_actuators.py` computes chit at each instance's operating points, classifies per-mode regime, stacks the 26-point chit envelope.
7. **F-001-actuator.** Predicted: chit_max ≈ -ln(1 - η) where η is electromechanical conversion efficiency. Test the bound against observed chit_max in the substrate-zero stack.
8. **F-002-contrast (new finding from PyHDDBenchmark verification).** Record in FOOTING: the SOC-attractor reading of F-002 is substrate-conditional, not universal. HDD VCMs are deliberately engineered for c-regime (sharp resonances + external controller), NOT operated near chit ≈ 0. Engines tune to chit ≈ 0 by SOC self-tuning; loudspeakers sit at chit ≈ 0 by radiation efficiency cap; HDDs live far from chit ≈ 0. cdv1 §Active modulation handles the plant+controller decomposition; this is the first substrate where it lands materially.

### Phase B: substrate-two RLC for F-003 c→s→r walk (pulled forward from old Phase D)

9. **Implement `mpa_relaxation_packs.rlc`.** Closed-form: Q = (1/R)·√(L/C). Step response is the textbook damped sinusoid e^(-γt)·[A·cos(ω_d·t) + B·sin(ω_d·t)] for Q > 0.5; over-damped form (sum of two real exponentials) for Q < 0.5. No external data needed — substrate is fully analytical.
10. **F-003-rlc.** Sweep Q from ~0.1 (r) through 0.5 (s) to ~5 (c) by varying R at fixed L, C. For each Q, the step-response settling profile. cdv1 §Stability prediction: algebraic settling at Q = 0.5 (chit ≈ 0); exponential elsewhere. Algebraic-vs-exponential fit is the F-003 test. RLC is synthetic but it's the cleanest substrate to verify the fit machinery before applying it to real-substrate data.
11. **Substrate-two null check.** Stack chit values from RLC across the Q sweep alongside substrate-zero actuator data. Substrate-two should look "clean" (analytical); substrate-zero should look "noisy" (real measurements). Disagreement on regime classification reveals substrate-conditional artefacts.

### Phase C: cross-substrate F-001 fingerprint (was old Phase B)

12. **F-cross-001.** Stack F-001-engine (chit_max ≈ 0.41), F-001-actuator (MDPI 2020 r-regime + PyHDDBenchmark c-regime, chit_max varies by instance), F-001-rlc (synthetic, η→1 limit). Three substrate-classes minimum. The universality claim is chit_max bounded by -ln(1 - η_substrate-class).

### Phase D: substrate-three viscoelastic materials (stress test, was substrate-three queued)

13. **Viscoelastic damping materials substrate-three.** MatWeb / vendor datasheets (3M VHB, Roush, SoundCoat). Loss factor η_loss → Q = 1/η_loss → regime classification. Real-world heterogeneity across hundreds of materials = stress test for the universality claim. F-001-materials.

### Phase E: unshelve loudspeakers

14. **Unshelve loudspeakers.** Read as a *configured instance* of substrate-zero (voice coil actuator + cone + cavity load). Prior research at [data/sources/shelved-loudspeaker-research.md](../data/sources/shelved-loudspeaker-research.md). Adds audiophile c→s→r vocabulary and carb-tuning everyman analogy back into the rhetorical surface for external publication.

### Phase F: substrate menagerie expansion (substrate backlog from [SOURCES.md §7](../data/sources/SOURCES.md))

Stepper motors (multi-stable actuator configurations, inter-step ringing), mechanical switches / debounce (universal microelectronics-scale tuning problem), RC circuits (first-order purely-r-regime endpoint), TeachSpin torsional oscillator (real-apparatus c→s→r if RLC feels synthetic). Each one earns activation when there's a specific finding to test. Don't accumulate substrate menagerie for its own sake.

## Gotchas surfaced

- **Multimodal substrates.** PyHDDBenchmark is multimodal — 16 VCM modes + 8 PZT modes, each with its own (ω, ζ, modal residue). chit reading is per-mode, not aggregate. Substrate-zero kernel must handle modal sums cleanly. Modal residue signs (kappa) encode anti-resonance / anti-phase coupling; chit per mode still well-defined.
- **Q definition matters.** Thiele/Small Q_ts (loudspeaker) and actuator-control Q (settling-time literature) both use the canonical second-order Q = ω₀/(2γ), but: small-signal vs large-signal Q can drift (Klippel-type nonlinearity), and "system Q" with load differs from "driver Q" in free air. Calibration record must declare drive level and load configuration.
- **chit ↔ Q is not an identity.** Q is structural (controls recovery profile after perturbation). chit is the order parameter (varies across operating points, lives at 0 by SOC self-tuning at steady-state NESS). They sit on different axes. Q determines the c→s→r regime; chit determines whether a sustained NESS exists at all. **PyHDDBenchmark adds:** some substrates have plants that live far from chit ≈ 0 by design, with external controllers closing the gap. cdv1 §Active modulation handles plant+controller decomposition; calibration records declare which.
- **Open-loop vs closed-loop data.** Industrial servo data is often buried under closed-loop control — only the *commanded* response is exposed, not the open-loop substrate. PyHDDBenchmark exposes the open-loop plant explicitly (the controllers are in `Data_Cd.mat`, the plant is in `plant.py` / `Fre_Resp.json`). Calibration record must specify open-loop test, or explicitly decompose controller from plant per cdv1 §Active modulation.
- **Settling-time conventions differ.** "2% settling time" vs "5% settling time" vs "first zero-crossing time" — actuator literature uses several. The chit-fit takes the raw time-series, but cross-comparison against literature Q values must align conventions.

## Coordinates

- Upstream framework: [mpa-atlas/framework/cdv1_compressed.md](https://github.com/ronviers/mpa-atlas/blob/main/framework/cdv1_compressed.md)
- Validator tool: [mpa-bridge](https://github.com/ronviers/mpa-bridge)
- Substrate-one (cited, frozen): [mpa-engine](https://github.com/ronviers/mpa-engine)
- Sibling substrate repos: [mpa-brain](https://github.com/ronviers/mpa-brain), [mpc-glass](https://github.com/ronviers/mpc-glass)
