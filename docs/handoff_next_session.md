# Handoff — next session

## Current state (2026-05-12, substrate-zero pivot to voice coil actuators)

Substrate-zero pivoted from loudspeakers to **voice coil linear actuators** on 2026-05-12. Reasoning: a loudspeaker is a voice coil actuator with a cone + cavity bolted on — the cavity was never the substrate, it was the load configuration. Stripping the cone and cavity gives the bare driven-dissipative oscillator. Wins: cleaner physics (no acoustic radiation impedance, no room), knob-tunable Q (load mass + damping coefficient, not a different enclosure per tuning), wider chit envelope (~0.1–0.5 vs ~0.02), industrial-precision open-data archives (Zenodo, Mendeley, IEEE DataPort, MDPI Actuators, DSpace@MIT, ePrints Soton), and c→s→r tuning as standard engineering practice (HDD seek, OIS, lithography stages, haptic LRAs).

Three outside research models running data hunt (2026-05-12) using the actuator-targeted prompt. Phase A starts when results land.

Loudspeakers shelved with explicit commitment to return — same substrate-class, stronger rhetorical fit (audiophile c→s→r vocabulary, carb-tuning everyman analogy). Will be characterized as a *configured instance* of substrate-zero once the bare-actuator substrate lands. Prior loudspeaker research lives at [data/sources/shelved-loudspeaker-research.md](../data/sources/shelved-loudspeaker-research.md).

## What's queued

### Phase A: voice coil actuator substrate-zero end-to-end

1. **Driver profile already drafted.** [reference-driver/voice-coil-actuator.md](../reference-driver/voice-coil-actuator.md) v0.1 — substrate-class declaration, gamut, translation field, intents, reference outputs. Updates when first calibration record lands.
2. **Ingest research output from three outside models.** Cross-reference for overlap on (a) canonical actuator candidates, (b) tunable test rig pointers, (c) open-data archive datasets with download URLs. Overlap is the signal; divergence is hallucination filter.
3. **Pick a canonical actuator.** Selection criterion: published electromagnetic parameters (BL, R, L, M, K) **plus** time-series step-response data with settling behaviour. Bias toward (in order): a published HDD VCM characterization → inertial actuator from academic paper (e.g., Dal Borgo 2019 candidate) → MDPI Actuators supplementary dataset → IEEE DataPort entry → haptic LRA datasheet. Selection writes to FOOTING discussion.
4. **Extract substrate data to JSON.** `data/<actuator-id>.json`: electromagnetic parameters, suspension parameters, load configuration, step-response time-series (current command → position trace), frequency response if available.
5. **Implement `mpa_relaxation_packs.voice_coil`.** Loader + chit reading: G₀ = V·I or I²·R + BL·v·I, L = sum of decomposed losses, chit = ln(G₀ / L). Regime classification from Q (γ = ω₀/(2Q), ω_d = ω₀·√(1 - 1/(4Q²)) — c-regime if Q > 0.5, s at Q = 0.5, r if Q < 0.5).
6. **Calibration record.** `reference-driver/<actuator-id>-calibration.json` per RFC-C §2.
7. **Smoke experiment.** `experiments/chit_<actuator-id>.py` computes chit at the resonance, classifies regime from Q, fits the step-response settling profile (exponential vs algebraic).
8. **F-001-actuator.** Predicted: chit_max in 0.1–0.5 range, depending on load. Test against observed chit at sustained operating point. Same form as F-001-engine.

### Phase B: cross-substrate F-001 fingerprint

9. **F-cross-001.** Stack F-001-engine (chit_max ≈ 0.41), F-001-actuator (chit_max ~0.1–0.5, instance-dependent) on the same universality axis: chit_max bounded by -ln(1 - η) where η is the substrate's drive-to-useful-output efficiency. Two substrate-classes is the minimum; RLC adds a third when it lands.

### Phase C: c→s→r recovery-tail test (the original F-003 goal)

10. **Pick a tunable actuator testbed.** Either (a) an academic test rig where load mass / damping is documented to walk Q across c→s→r (Dal Borgo 2019 candidate per the actuator research prompt), or (b) a published HDD seek profile dataset that exposes per-Q step responses across firmware tunings.
11. **Per-Q step-response measurements.** For each Q value, settling profile tests exponential vs. algebraic decay.
12. **F-003-actuator.** Recovery profile is algebraic at Q ≈ 0.5 (chit ≈ 0); exponential elsewhere. cdv1 §Stability prediction. The carb-tuning scenario realized in a substrate where data is free, the tunable parameter is one number, and the engineering practice already routinely walks the regimes.

### Phase D: substrate-two (RLC) and substrate-three (materials)

13. **RLC circuit substrate-two.** Textbook formulae, SPICE-simulatable. Loader takes (R, L, C); chit = ln(input_power / total_dissipation); Q = (1/R)·√(L/C). Step response is the closed-form damped sinusoid. Null check that the cross-substrate test isn't a two-substrate fluke and that the chit-from-Q implementation is correct.
14. **Viscoelastic damping materials substrate-three.** MatWeb / vendor datasheets (3M VHB, Roush, SoundCoat). Loss factor η_loss → Q = 1/η_loss → regime classification. Real-world heterogeneity across hundreds of materials = stress test for the universality claim.

### Phase E: return to loudspeakers

15. **Unshelve loudspeakers.** Read as a *configured instance* of substrate-zero (voice coil actuator + cone + cavity load). Prior research at [data/sources/shelved-loudspeaker-research.md](../data/sources/shelved-loudspeaker-research.md). Adds the audiophile vocabulary back into the rhetorical surface for external publication.

## Gotchas surfaced

- **Q definition matters.** Thiele/Small Q_ts (loudspeaker) and actuator-control Q (settling-time literature) both use the canonical second-order Q = ω₀/(2γ), but: small-signal vs large-signal Q can drift (Klippel-type nonlinearity), and "system Q" with load differs from "driver Q" in free air. Calibration record must declare drive level and load configuration.
- **chit ↔ Q is not an identity.** Q is structural (controls recovery profile after perturbation). chit is the order parameter (varies across operating points, lives at 0 by SOC self-tuning at steady-state NESS). They sit on different axes. Q determines the c→s→r regime; chit determines whether a sustained NESS exists at all.
- **Open-loop vs closed-loop data.** Industrial servo data is often buried under closed-loop control — only the *commanded* response is exposed, not the open-loop substrate. Calibration record must specify open-loop test, or explicitly decompose controller from plant per cdv1 §Active modulation.
- **Settling-time conventions differ.** "2% settling time" vs "5% settling time" vs "first zero-crossing time" — actuator literature uses several. The chit-fit takes the raw time-series, but cross-comparison against literature Q values must align conventions.

## Coordinates

- Upstream framework: [mpa-atlas/framework/cdv1_compressed.md](https://github.com/ronviers/mpa-atlas/blob/main/framework/cdv1_compressed.md)
- Validator tool: [mpa-bridge](https://github.com/ronviers/mpa-bridge)
- Substrate-one (cited, frozen): [mpa-engine](https://github.com/ronviers/mpa-engine)
- Sibling substrate repos: [mpa-brain](https://github.com/ronviers/mpa-brain), [mpc-glass](https://github.com/ronviers/mpc-glass)
