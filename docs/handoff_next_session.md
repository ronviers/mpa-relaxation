# Handoff — next session

## Current state (2026-05-11, v0 scaffold)

Repo stood up with sibling treatment (README, CLAUDE.md, .gitignore, package skeleton, RFC-S / RFC-C coordinates pointed at mpa-atlas). No data, no experiments, no findings yet. Substrate zero (loudspeakers) queued; substrate one (engines) cited from [mpa-engine](https://github.com/ronviers/mpa-engine).

## Why this repo exists

cdv1's c→s→r damping structure should appear in any tunable driven-dissipative system. mpa-engine validated F-001 (chit_max ≈ -ln(1 - η_thermal,max)) on IC engines. Natural next step: test whether the *same chit definition* and *same regime structure* hold on a second, much more accessible substrate. Loudspeakers chosen first because the damping parameter (Q_ts) is one number, the loss decomposition (Q_es electrical / Q_ms mechanical / radiation) is in every datasheet, and free measurement data is abundant. The cross-substrate comparison is the load-bearing finding.

## What's queued

### Phase A: loudspeaker substrate-zero end-to-end

1. **Write the loudspeaker driver profile.** `reference-driver/loudspeaker.md`, shaped per RFC-S §4. Substrate-class declaration, gamut, translation field (Q_ts → chit, CSD → recovery profile), intents, reference outputs.
2. **Pick a canonical loudspeaker.** Candidates: well-measured studio monitors (Genelec 8030, Neumann KH80) or classic sealed-box references (KEF LS50, original Wharfedale Diamond). Selection criterion: published Thiele/Small parameters **plus** published CSD measurement from a reputable source (ASR, Stereophile, Klippel public data, AudioXpress).
3. **Extract substrate data to JSON.** `data/<speaker-id>.json`: Thiele/Small parameters (Q_ts, Q_es, Q_ms, Fs, Vas, Re, BL, Mms), CSD waterfall (frequency × time × dB), impulse response if available.
4. **Implement `mpa_relaxation_packs.loudspeaker`.** Loader + chit reading: G₀ = electrical power into voice coil, L = sum of decomposed losses, chit = ln(G₀ / L). Regime classification from Q_ts.
5. **Calibration record.** `reference-driver/<speaker-id>-calibration.json` per RFC-C §2.
6. **Smoke experiment.** `experiments/chit_<speaker-id>.py` computes chit at the fundamental resonance, classifies regime from Q_ts, fits the CSD decay tail (exponential vs. algebraic).
7. **F-001-loudspeaker.** Predicted: chit_max ≈ -ln(1 - η_acoustic), giving chit_max ~0.01–0.03 for typical loudspeakers. Test against observed chit at the system's resonance peak. Same form as F-001-engine; much narrower envelope.

### Phase B: cross-substrate F-001 fingerprint

8. **F-cross-001.** Stack F-001-engine (Camry, chit_max ≈ 0.41) and F-001-loudspeaker (chit_max ≈ 0.02) on the same axis: chit_max bounded by -ln(1 - η) as a substrate-class universality. Two data points is the minimum; an RLC circuit as substrate-two would make it three.

### Phase C: c→s→r recovery-tail test (the original F-003 goal, finally landable)

9. **Pick a tunable speaker.** Vented-box or sealed-box where port-tuning + damping material let us walk Q_ts across the c → s → r range. DIY/audiophile community publishes thousands of such tunings.
10. **Per-tuning CSD measurements.** For each Q_ts value, CSD tail shape tests exponential vs. algebraic decay.
11. **F-003-loudspeaker.** Recovery profile is algebraic at Q_ts ≈ 0.707 (chit ≈ 0); exponential elsewhere. cdv1 §Stability prediction. The carb-tuning scenario realized in a substrate where data is free and the tunable parameter is one number.

### Phase D: substrate-two

12. **RLC circuit** is the cleanest substrate-two candidate: tunable R, free SPICE-simulatable or breadboard-measurable, three regimes mappable one-to-one via standard textbook formulae. Validates that the cross-substrate test isn't a two-substrate fluke.

## Gotchas to surface as work proceeds

- CSD measurements have **windowing artefacts** at short times. Fitting the decay tail must start past the windowing region.
- Loudspeaker measurements are commonly **gated to remove room reflections**. Gate length sets the lower frequency limit of the CSD. For low-frequency-resonance speakers, this caps how cleanly we can read the dominant mode.
- Q_ts is **frequency-domain**, chit is **thermodynamic**. The mapping is monotonic but not identity. Establishing the precise relationship (probably chit ≈ ln(2Q) at resonance, or similar) is a Phase A sub-task worth writing down.
- Manufacturer-published Thiele/Small is often **small-signal**. Real chit at audible playback level may drift via Klippel-type nonlinearities. Substrate-state matters; the calibration record should declare drive level.

## Coordinates

- Upstream framework: [mpa-atlas/framework/cdv1_compressed.md](https://github.com/ronviers/mpa-atlas/blob/main/framework/cdv1_compressed.md)
- Validator tool: [mpa-bridge](https://github.com/ronviers/mpa-bridge)
- Substrate-one (cited, frozen): [mpa-engine](https://github.com/ronviers/mpa-engine)
- Sibling substrate repos: [mpa-brain](https://github.com/ronviers/mpa-brain), [mpc-glass](https://github.com/ronviers/mpc-glass)
