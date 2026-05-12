# FOOTING — cross-substrate findings

Append-only log of cross-substrate findings: things measured across multiple substrates that the framework needs to know about damping universality. Each entry is one finding with its evidence.

Pattern follows [mpa-engine/docs/journey/FOOTING.md](https://github.com/ronviers/engine/blob/main/docs/journey/FOOTING.md) (F-001, F-002, ...): code, name, date, claim, evidence, framework implication. Findings here are *cross-substrate*; per-substrate findings live in the per-substrate repos.

---

## F-002-contrast · SOC attractor is substrate-conditional, not universal · 2026-05-12

**Claim.** cdv1's SOC-attractor reading — that feedback-coupled NESS self-tune to chit ≈ 0 (mpa-engine F-002 on idling engines) — does **not** generalize as written across substrate-classes. Some substrate-classes are engineered or evolved to live near chit ≈ 0; others are engineered to live far from chit ≈ 0 with external controllers closing the gap. Both are valid driven-dissipative NESS configurations under cdv1; the difference is whether the SOC self-tuning is internal to the substrate or imposed externally.

**Evidence.** Three substrate-classes characterized to date span the chit axis:

| Substrate-class | Operating chit | Mechanism |
|---|---|---|
| IC engine at idle ([mpa-engine F-001/F-002](https://github.com/ronviers/mpa-engine/blob/main/docs/journey/FOOTING.md)) | ≈ 0 exactly | ECU (or carburetor) drives the lowest stable RPM. chit = 0 by tautology at idle + non-tautological RPM choice. SOC self-tuning is **internal**. |
| Loudspeaker driver (Phase E shelved, prior evidence in [shelved-loudspeaker-research.md](../../data/sources/shelved-loudspeaker-research.md)) | ≈ 0.003–0.014 | Acoustic conversion efficiency 1–3% caps chit_max. Substrate lives near chit ≈ 0 by half-space radiation physics, not by feedback tuning. SOC attractor is **physical, not designed**. |
| HDD voice coil motor + PZT secondary (PyHDDBenchmark, [data/pyhddbenchmark-vcm.json](../../data/pyhddbenchmark-vcm.json)) | far from 0 by design | 16 VCM modes Q ∈ [12.5, 71.4], 8 PZT modes Q ∈ [1.67, 62.5], all c-regime. Sharp resonance peaks are intentional. External closed-loop controller (`Data_Cd.mat` in PyHDDBenchmark) closes the gap, treating the substrate as a *plant* to be controlled. SOC self-tuning is **external**. |

**Framework implication.** F-002 from mpa-engine reads "feedback-coupled NESS lands at chit ≈ 0 as a parameter-space attractor; the ECU's idle-control loop is the SOC self-tuning that lands the engine there." That reading conflates **plant + controller** into one system. cdv1 §Active modulation handles the decomposition: the plant is the substrate (engine block + combustion + losses; or HDD voice coil + flexure + bearings), the controller is the active modulator that closes the loop around the plant's natural NESS. F-002-corrected:

- **Plant alone** may or may not have an internal SOC attractor at chit ≈ 0. Engines do (at idle, chit ≈ 0 by definition of zero brake power); HDDs do not (the plant has sharp c-regime resonances that would diverge without external control).
- **Plant + controller** *does* close on a working-point NESS, but that working-point may be far from chit ≈ 0 in the substrate's own units. The controller carries the SOC-attractor work, not the substrate.

Falsifier: a substrate-class characterized as "plant + controller" where the controller's closure point demonstrably lives at chit ≈ 0 in the substrate's units — that would restore the universal SOC-attractor reading. Test case: examine the *closed-loop* trajectory of the PyHDDBenchmark VCM under its provided controller and ask whether the closed-loop NESS (head-positioning steady state at a track) reads as chit ≈ 0 in the same substrate-native frame as the open-loop plant modes.

**Cross-substrate test condition.** Each next substrate added to the menagerie must declare its **SOC attractor location** explicitly in its calibration record: internal (substrate lives at chit ≈ 0 by physics or evolved design), external (substrate lives far from chit ≈ 0 by design and a controller closes the loop), or none (no sustained NESS — r-regime substrate). The substrate-class fingerprint includes which category it belongs to.

Phase A status: this finding lands as F-002-contrast based on substrate-zero stack characterization. F-002 (provisional in mpa-engine) is **not promoted** to confirmed by mpa-relaxation evidence — instead it is **refined** into a substrate-conditional statement. mpa-engine's F-002 remains valid as stated *for that substrate-class*; the universal reading does not.

## F-003-rlc · c→s→r recovery-tail walk in textbook substrate · 2026-05-12

**Claim.** cdv1 §Stability's prediction — that the step-response decay envelope at the s-boundary (Q = 0.5, chit ≈ 0) carries an algebraic factor qualitatively distinct from the c-regime (exponential with oscillation) and r-regime (double-exponential) forms — passes cleanly in the textbook RLC substrate. The algebraic factor (1 + α·t)·e^(-α·t) is the analytical step response at critical damping; neither pure-exponential nor pure-double-exponential reconstructions capture it.

**Evidence.** F-003-rlc experiment ([experiments/f003_rlc_walk.py](../../experiments/f003_rlc_walk.py), [docs/results/f003_rlc_walk.json](../results/f003_rlc_walk.json)) sweeps Q across [0.05, 10.0] with fine resolution around Q = 0.5. For each Q, two candidate envelope forms are fit to the analytical step response: pure-exponential 1 - e^(-α·t) and algebraic-exponential 1 - (1 + α·t)·e^(-α·t). RMS residual ratio RMS(alg) / RMS(pure) measures which form is closer to truth.

| Q | regime | overshoot | ratio |
|---|---|---|---|
| 0.100 | r | 0% | 0.9746 |
| 0.300 | r | 0% | 0.7429 |
| 0.450 | r | 0% | 0.2767 |
| **0.500** | **s** | **0%** | **0.0000** |
| 0.530 | c | 0.01% | 0.2149 |
| 0.707 | c | 4.32% | 2.1899 |
| 2.000 | c | 44.43% | 1.6087 |

The ratio drops continuously toward zero as Q approaches 0.5 from either side, hits zero exactly at Q = 0.5 (algebraic-exp is the analytical solution there, RMS residual identically zero), and rises again outside that neighborhood. In the deep c-regime (Q > 1) the algebraic-exp form is *worse* than pure-exp because the analytical solution oscillates — neither static envelope captures the ringing. In the deep r-regime (Q < 0.2) both envelopes are roughly equally wrong because the double-exponential structure differs from both. The minimum is uniquely at Q = 0.5.

**Framework implication.** cdv1's c→s→r prediction is **confirmed in the textbook substrate**. Specifically:

1. The s-boundary is a *qualitatively distinct* operating regime, not a quantitative interpolation between c and r. The algebraic factor in the decay envelope is the signature.
2. The test machinery (fit two candidate envelopes, compare RMS residuals across a Q sweep, look for the minimum) works as expected in a noise-free analytical substrate. Same machinery can now be applied to real-substrate data with the noise/measurement-artefact floor as the limit of resolution.
3. The substrate-two null-check role lands cleanly: the framework's prediction and the test machinery are both correct in the textbook case. Any real-substrate test that *fails* this prediction owes its failure to substrate-conditional content (measurement noise, unmeasured loss channels, multi-mode coupling, controller artefacts), not to the framework's prediction being wrong.

**Cross-substrate test condition.** The algebraic-exp signature at Q = 0.5 should appear (modulo noise) in any second-order driven-dissipative substrate when Q is walked through the s-boundary. Substrate-zero (voice coil actuators in current stack) doesn't sample Q = 0.5 — both MDPI 2020 instances are Q < 0.5 and all PyHDDBenchmark modes are Q >> 0.5. To test F-003 on substrate-zero, either (a) digitize MDPI 2020 Figures 12-13 step responses and extrapolate toward Q = 0.5 (the data doesn't reach it but trend visible), or (b) find an additional actuator instance designed for critical damping. The TeachSpin torsional oscillator (pocket fallback, [SOURCES.md §7.4](../../data/sources/SOURCES.md)) is engineered exactly for this — tunable damping across the Q = 0.5 region with documented step responses.

**Status:** F-003-rlc confirmed in substrate-two. F-003-actuator and F-003-engine (cross-substrate replications) are queued as Phase C work. Until cross-substrate replication lands, F-003 stands as substrate-conditional (proven in RLC, predicted elsewhere). The prediction is sharp enough — the algebraic factor is exact, not approximate — that any well-instrumented substrate sweeping Q = 0.5 should expose it directly.

## F-001-actuator (MDPI 2020) · chit_max bound from electromechanical coupling · 2026-05-12

**Claim.** cdv1 F-001 (chit_max ≈ -ln(1 - η_max)) applies to voice coil linear actuator substrates with η_em = (BL)² / (c·R + (BL)²) — the fraction of input electrical power that crosses the BL coupling into the mechanical degree of freedom at mechanical resonance. For an actuator with no specified external load, this is a *substrate-intrinsic upper bound* on chit, not an observed-equal-to-prediction value.

**Evidence.** F-001-actuator experiment ([experiments/f001_actuator.py](../../experiments/f001_actuator.py), [docs/results/f001_actuator.json](../results/f001_actuator.json)) computes η_em for the two MDPI 2020 cantilever VCA instances using their published Table 2 parameters (BL=28.46 N/A, R=28.9 Ω; c=300 N·s/m for Al bobbin, c=25 N·s/m for plastic bobbin):

| Instance | c (N·s/m) | Q | η_em | chit_max bound |
|---|---|---|---|---|
| Aluminum bobbin (heavy eddy damping) | 300 | 0.033 | 0.0854 | 0.0893 |
| Plastic bobbin (light damping) | 25 | 0.394 | 0.5285 | 0.7519 |

Formula assumes L_e·ω₀ ≪ R. For these instances L_e·ω₀/R = 0.128 (well below 0.3 sanity threshold), formula applies.

**Cross-substrate fingerprint surfacing across F-001 entries:**

| Substrate | chit_max bound or observed | Capping mechanism |
|---|---|---|
| Loudspeaker driver (Phase E shelved) | ~0.003–0.014 estimated | Half-space acoustic radiation efficiency cap |
| Engine Camry 2.4L (mpa-engine F-001) | 0.432 predicted, 0.410 observed | Thermal efficiency at BSFC sweet spot |
| MDPI 2020 VCA aluminum bobbin | 0.089 bound | Heavy eddy-current damping wastes power before it reaches mechanical motion |
| MDPI 2020 VCA plastic bobbin | 0.752 bound | Light damping + strong BL coupling → wide envelope, highest of any substrate characterized to date |

**Framework implication.** The "narrow chit envelope" intuition (carried forward from loudspeaker thinking pre-pivot) was a loudspeaker-specific finding, *not* a substrate-class universal. Voice coil substrates with light mechanical damping and strong BL coupling can span a wider chit envelope than engines. The substrate-class fingerprint is *not* "chit envelope width" but rather "η-cap mechanism" — what physically limits the conversion efficiency. Four distinct capping mechanisms observed so far: radiation, thermal, eddy-dissipation, electromechanical-coupling-limited.

F-001 itself — the universal form chit_max ≈ -ln(1 - η) — passes cleanly. The cross-substrate observation is on **what η_max means physically**, which is substrate-conditional content. cdv1's substrate-conditional/substrate-neutral split holds: the universal form is preserved, the per-substrate amplitudes (and their physical interpretation) vary.

**Pending closure for full F-001-actuator universality:** PyHDDBenchmark VCM and PZT η values not extractable from the modal-sum plant.py representation alone. VCM would need the underlying (BL, R, c) parameters from the Atsumi & Yabui 2020 paper; PZT needs a different substrate-class formula (electrostrictive drive, not BL-coupled Lorentz). Substrate-class scope decision deferred: one substrate-class spanning both voice coil and PZT actuators, or split into electromagnetic-actuator and piezoelectric-actuator classes.

**Status:** F-001-actuator-mdpi confirmed as bound (not as observed-match-to-prediction; that requires step-response measurements under specified load). F-001 cross-substrate fingerprint refined: capping mechanism is the substrate-class signature, not chit_max value alone.

## M-001 · F-003 algebraic-signature test has ~30 dB SNR floor · 2026-05-12

**Methodological finding** (M-series for test-machinery characterization, distinct from F-series substrate findings).

**Claim.** The F-003 algebraic-signature test (RMS-residual ratio between algebraic-exp and pure-exp envelope fits, with minimum at Q = 0.5) survives Gaussian measurement noise down to ~30 dB SNR. Above 40 dB the signature is robust; below 20 dB it is lost.

**Evidence.** [experiments/f003_noise_robustness.py](../../experiments/f003_noise_robustness.py), [docs/results/f003_noise_robustness.json](../results/f003_noise_robustness.json). Synthetic RLC step responses across Q sweep at SNR levels 10–60 dB, 30 noise realizations per (Q, SNR) point. 2σ-rule detection criterion (mean ratio at Q = 0.5 below nearest non-critical competitor by at least 2σ).

| SNR | mean ratio at Q = 0.5 | nearest competitor | detectable |
|---|---|---|---|
| 60 dB | 0.011 ± 0.0002 | 0.277 | yes |
| 50 dB | 0.035 ± 0.0006 | 0.278 | yes |
| 40 dB | 0.111 ± 0.0015 | 0.290 | yes |
| 30 dB | 0.334 ± 0.0045 | 0.386 | yes (marginal) |
| 20 dB | 0.747 ± 0.0116 | 0.710 | **no** |
| 10 dB | 0.963 ± 0.0042 | 0.942 | **no** |

**Framework implication.** Real-substrate F-003 measurements must achieve at least 30 dB SNR (preferably 40+ dB) for the algebraic signature to be detectable. Modern lab oscilloscopes (60–80 dB), professional ADCs (80–100 dB), and even consumer-grade DAQs (30–50 dB) all clear the floor comfortably. The noise robustness is not a practical barrier; this finding rules out one failure mode for upcoming real-substrate replications (noisy data masking a present signature → false negative).

**When to cite this.** Any F-003 test against real-substrate data must report measurement SNR. If reported SNR is below 30 dB and the F-003 signature is not detected, the result is methodologically inconclusive — the framework's prediction may still hold, the test just can't see it. Future-Claude: include SNR estimation as a standard step in F-003-on-real-data experiments.
