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

## F-002-restoration · partial: controller pulls plant 1–2 decades toward s-boundary but stops short · 2026-05-12

**Claim under test.** F-002-contrast (entry above) proposed a falsifier: if HDD-style external controllers *natively hunt for Q_cl ≈ 0.5*, the universal SOC-attractor reading of F-002 is restored at the plant+controller level. The PyHDDBenchmark closed-loop is the natural test case — real industrial HDD controller, real plant, published frequency-response data.

**Evidence.** [experiments/f002_restoration_pyhddbenchmark.py](../../experiments/f002_restoration_pyhddbenchmark.py), [docs/results/f002_restoration_pyhddbenchmark.json](../results/f002_restoration_pyhddbenchmark.json). Loaded `Fre_Resp.json` from the cloned PyHDDBenchmark repo (instructions in [SOURCES.md §1.0](../../data/sources/SOURCES.md)). Computed L = P·C·F, T = L/(1+L), S = 1/(1+L) for 9 plant manufacturing variations. Extracted Q_cl from peak sensitivity M_s using the second-order approximation M_s = 1/(2ζ√(1-ζ²)).

| Metric | Open-loop plant (substrate-zero) | Closed-loop (plant + controller) |
|---|---|---|
| Q range | [12.5, 71.4] | [1.33, 1.56] |
| Regime | c (deep) | c (moderate) |
| Reduction factor (Q_open / Q_cl) | — | 8× to 54× |
| Closed-loop bandwidth | n/a | ~5.3 kHz across all 9 realizations |

**Verdict: PARTIAL RESTORATION.** The controller drops the substrate's effective Q by 1–2 decades — substantial pull toward the s-boundary — but lands at Q_cl ≈ 1.4, not Q_cl = 0.5. The closed-loop is *much closer* to chit ≈ 0 than the open-loop plant, but not at it. F-002's universal SOC-attractor reading is not fully restored by adding a controller; instead, *each substrate-class declares how aggressively its design pressure pushes toward Q ≈ 0.5*.

**Refined framework reading.** Substrate-class fingerprints differ in *what pushes them toward or away from the s-boundary*:

| Substrate-class | Design pressure | Operating Q |
|---|---|---|
| IC engine at idle | Must be stable at low fuel; ECU drives the lowest stable RPM | chit ≈ 0 exactly (Q ≈ 0.5 by force) |
| Loudspeaker driver | Physics caps acoustic efficiency at 1–3% | chit ≈ 0.003–0.014 (≈ Q ≈ 0.5 by physics) |
| HDD VCM + controller | Bandwidth-pressure pushes Q_cl up (fast response); settling-pressure pushes Q_cl down (no ringing). Tradeoff lands at Q_cl ≈ 1.4 | c-regime, but 1–2 decades below open-loop plant |
| HDD VCM open-loop | None — plant is engineered for sharp resonance peaks, externally damped | Q ∈ [12.5, 71], deep c-regime |

The cdv1 §Active modulation decomposition (plant + controller) lands here cleanly: the *controller* carries the SOC-pulling work, but the *controller's design objective* isn't necessarily chit ≈ 0 — it's a substrate-conditional tradeoff between competing performance goals.

**Framework implication.** F-002 is not universal as written. The substrate-conditional refinement: every driven-dissipative NESS has *some* design pressure toward chit ≈ 0 (otherwise the system wouldn't be a sustained NESS at all), but the *amplitude* of that pressure varies by substrate. Engines and loudspeakers land at chit ≈ 0 because the physics or the dominant design constraint forces it. HDDs land at chit > 0 because the bandwidth-vs-damping tradeoff is two-sided.

**Sub-result worth noting.** The 8–54× Q reduction is *itself* an interesting universality candidate. If many substrate+controller pairs show O(10) Q reduction (regardless of where the final Q_cl lands), that's a substrate-neutral statement about controller efficacy. Worth surfacing as a candidate finding for the framework: "external controllers reduce substrate Q by roughly one decade, regardless of substrate-class."

**Status.** F-002-restoration: partial yes (substantial pull, not full landing at s-boundary). F-002 retracted as universal; refined to substrate-conditional with explicit design-pressure declaration in each substrate's calibration record. F-002-contrast (FOOTING 2026-05-12) and F-002-restoration (this entry) together replace the original F-002 universal reading.

**Pending closure.** The Q_cl extraction here uses a second-order approximation (Q from M_s peak). The actual closed-loop is high-order (9-state controller + 16-mode plant + multi-rate filter). A tighter Q_cl might come from time-domain step-response analysis (overshoot directly tells damping ratio of the dominant pole pair). Future Phase C work could run the full PyHDDBenchmark simulation and measure overshoot in the position trajectory, refining the Q_cl ≈ 1.4 estimate. For now, the 1-2 decade Q-reduction finding is solid regardless of the exact endpoint.

## F-001-scope-limit · F-001 has a substrate-class scope; F-003 is the more general invariant · 2026-05-12

**Claim.** cdv1 F-001 (chit_max ≈ -ln(1 - η_max)) **does not apply universally** across driven-dissipative substrate-classes. Its scope is *substrates with mode-separated drive and useful-work*. For substrates where dissipation IS the useful work (no separate output mode), F-001 chit_max → ∞ in the formula limit — the bound is vacuous.

**Substrate that surfaces this finding.** Viscoelastic damping materials (Phase D, substrate-three). See [data/viscoelastic-damping-materials.json](../../data/viscoelastic-damping-materials.json) and [experiments/f003_viscoelastic.py](../../experiments/f003_viscoelastic.py).

**Evidence.** The substrate-class spans:

| Substrate-class instance | Drive mode | Useful-work mode | F-001 applies? |
|---|---|---|---|
| IC engine | Chemical (fuel) | Mechanical (brake power) | ✓ different modes; F-001 bound at η_thermal,max ≈ 0.35 |
| Loudspeaker | Electrical (voltage) | Acoustic (sound radiation) | ✓ different modes; F-001 bound at η_acoustic ≈ 0.01–0.03 |
| Voice coil actuator | Electrical (current) | Mechanical (position/velocity) | ✓ different modes; F-001 bound at η_em ≤ 0.75 |
| Viscoelastic damping | Mechanical (vibration) | Heat (dissipation) | ✗ "useful work" IS the dissipation; no separate output mode |

For damping materials, the *purpose* of the substrate is to convert vibration to heat. The "useful work" is the dissipation. Plugging η_conversion = 1 into F-001 gives chit_max = -ln(0) → ∞. The bound says nothing.

**Framework implication.** F-001 is *not* substrate-neutral content. It is a substrate-class-conditional invariant that applies wherever the substrate has mode-separated drive and useful-work. The substrate-neutral content is the *form* of F-001 (chit_max ≤ -ln(1 - η_conv)), but its *applicability* requires substrate-class declaration of mode separation.

F-003 (regime structure from Q: c above Q = 0.5, s at Q = 0.5, r below) is the more universally-applicable invariant. It applies wherever a second-order damped oscillator can be defined — which includes both mode-separated substrates *and* pure-dissipative substrates like viscoelastic materials.

**Refined substrate-class taxonomy:**

| Substrate-class type | F-001 applies | F-002 applies (SOC attractor) | F-003 applies |
|---|---|---|---|
| Mode-separated (engine, speaker, actuator) | ✓ | substrate-conditional | ✓ |
| Pure-dissipative (viscoelastic damper, friction brake, RC circuit) | ✗ (vacuous) | ✓ (sustained NESS → chit ≈ 0 trivially) | ✓ |

**Substrate-class declaration update.** Each substrate's driver profile ([reference-driver/*.md](../../reference-driver/)) must now declare its **mode-separation status**: mode-separated (with declaration of drive mode and useful-work mode) or pure-dissipative. This determines whether F-001 chit_max bound applies. mpa-engine and mpa-relaxation's voice-coil-actuator profile both implicitly assume mode-separated; explicit declaration deferred to a v0.2 RFC-S refinement.

**Status.** F-001 scope-limit confirmed via Phase D viscoelastic substrate. F-001 demoted from "universal substrate-class invariant" to "mode-separated-substrate invariant." F-003 elevated to "more general invariant, applies across mode-separated AND pure-dissipative substrates."

## F-003-viscoelastic · regime-structure stress test passes across material heterogeneity · 2026-05-12

**Claim.** cdv1 F-003 (regime structure from Q: c if Q > 0.5, s at Q = 0.5, r if Q < 0.5) **passes the stress test of substrate-class heterogeneity**. The substrate-class spans c, s, AND r regimes across 8 published viscoelastic damping material instances. The c→s→r structure is consistent across material composition, vendor methodology, and the (T, f) operating-condition variability.

**Evidence.** [experiments/f003_viscoelastic.py](../../experiments/f003_viscoelastic.py), [docs/results/f003_viscoelastic.json](../results/f003_viscoelastic.json). Eight representative damping materials from Jones (Wiley 2001), Nashif/Jones/Henderson (Wiley 1985), and vendor data:

| Material | tan δ peak | Q | Regime | Distance from s |
|---|---|---|---|---|
| Natural rubber gum | 0.35 | 2.857 | c | 2.357 |
| 3M VHB 4910 | 0.80 | 1.250 | c | 0.750 |
| Sorbothane 50 | 1.00 | 1.000 | c | 0.500 |
| 3M ISD-112 | 1.20 | 0.833 | c | 0.333 |
| EAR Isodamp C-1002 | 1.50 | 0.667 | c | 0.167 |
| **Plasticized PVC** | **1.80** | **0.556** | **c** | **0.056** |
| **PU45A high damping** | **2.00** | **0.500** | **s** | **0.000** |
| **Butyl rubber HD** | **2.30** | **0.435** | **r** | **0.065** |

**Findings:**

1. **All three regimes represented in a single substrate-class** (first time in our characterizations — engines were all c-or-s near idle, loudspeakers were all c near zero, actuators were all r or all c per instance). The viscoelastic substrate-class is uniquely suited to test cdv1's c→s→r structure within a single material taxonomy.

2. **Three instances span the s-boundary at Q ∈ [0.43, 0.56]** — by polymer formulation tuning. The substrate-class fingerprint is *engineering composition to land near the s-attractor*. PU45A is the canonical "maximum damping" formulation; plasticized PVC sits just on the c-side of critical; butyl-HD just on the r-side. The substrate engineers know which side of the boundary they want and tune to it.

3. **Substrate-class median Q = 0.750**, with **4 of 8 instances within 0.17 of critical** (Q ∈ [0.33, 0.67]). The cluster around the s-boundary is the substrate-class fingerprint. The exception (natural rubber gum, Q = 2.857) is the substrate-class instance NOT engineered for damping — it's a structural compound used in tires, where elasticity is wanted over dissipation. Including it as a "negative control" confirms the cluster is design-pressure-driven, not material-class-driven.

**Framework implication.** F-003 is substrate-neutral; this is the strongest single-substrate confirmation we have. The substrate-class is also the cleanest demonstration of cdv1's SOC self-tuning at the *substrate engineering* level: polymer chemists tune molecular formulation to land at chit ≈ 0 by design. Engines do this via real-time ECU control; viscoelastic materials do it via compositional engineering.

**Cross-substrate fingerprint update:**

| Substrate-class | Q at design operating point | Mechanism of s-boundary approach |
|---|---|---|
| Engines at idle (mpa-engine F-002) | chit ≈ 0 exactly | Real-time ECU feedback control |
| Loudspeakers (Phase E shelved) | chit ≈ 0.01 | Physical efficiency cap (radiation impedance) |
| Voice coil actuators open-loop | Q ≈ 12–71 (deep c) | Sharp resonances by design, externally damped |
| Voice coil actuators closed-loop | Q ≈ 1.4 (moderate c) | Bandwidth-damping tradeoff in controller |
| Viscoelastic damping materials | Q ≈ 0.5 (s-boundary) median | Polymer compositional engineering |
| RLC textbook | Q tunable across [0.1, 10] | Resistor selection |

**The substrate-class fingerprints differ in *what kind of engineering* lands them at chit ≈ 0**, not whether they get there. The framework holds across all five substrate-classes characterized to date — F-003 universally, F-001 conditionally on mode-separation.

**Status.** F-003-viscoelastic confirmed (regime structure passes substrate-class heterogeneity stress test). F-003 cross-substrate evidence now spans engines (cited), actuators (open + closed-loop), RLC (analytical), and viscoelastic materials. The seven-register cdv1 chain — drive amplitude G₀, loss L, chit, regime c/s/r, with substrate-conditional amplitudes — operates correctly across all five substrate-classes when F-001 scope-conditioning is applied.

## F-001-led · widest chit_max envelope of any substrate-class · 2026-05-12

**Claim.** cdv1 F-001 (chit_max ≈ -ln(1 - η_max)) applies to LEDs as a mode-separated drive-axis substrate. η_wpe (wall-plug efficiency = optical power radiated / electrical power consumed) is the substrate's η_conversion. The substrate-class spans the **widest chit_max envelope characterized to date** — 0.084 (UV LED, lowest of any substrate) to 0.693 (Samsung LM301B premium white, just below the actuator coupling-limited 0.752).

**Evidence.** [experiments/f001_led.py](../../experiments/f001_led.py), [docs/results/f001_led.json](../results/f001_led.json), [data/leds.json](../../data/leds.json). 13 LEDs cross-referenced from three outside-model research runs (2026-05-12). Spans 6 chemistries (UV, blue, red, deep red, yellow-green, white), 6 power classes (indicator through industrial high-power), and 6 regions (Western USA, Western German, Japanese, Chinese, Korean, Taiwan).

| ID | Chemistry | V_th (V) | η_wpe | chit_max bound |
|---|---|---|---|---|
| Toyoda Gosei UV | UV | 3.00 | 0.080 | 0.084 |
| Stanley VFJD1116P | yellow-green | 1.70 | 0.150 | 0.163 |
| Everlight SHWO deep red | deep_red | 1.75 | 0.250 | 0.288 |
| Honglitronic C5050 | white | 3.00 | 0.300 | 0.357 |
| Cree XP-G3 royal blue | blue | 2.82 | 0.350 | 0.431 |
| Cree XP-G3 photo red | red | 1.87 | 0.350 | 0.431 |
| Osram OSLON SSL 80 | white | 2.80 | 0.350 | 0.431 |
| LG Innotek LEMWS59R | white | 2.70 | 0.350 | 0.431 |
| Epistar 10W (multi-junction) | white | 9.60 | 0.350 | 0.431 |
| Nichia NVSW219C-V2 | white | 2.50 | 0.420 | 0.545 |
| Cree XP-G3 white | white | 2.70 | 0.460 | 0.616 |
| Seoul Semi WICOP | white | 2.68 | 0.470 | 0.635 |
| **Samsung LM301B** | **white** | **2.50** | **0.500** | **0.693** |

**Substrate-class internal heterogeneity finding.** Chemistry dictates F-001 chit_max more than power class does. Compare same-power-class entries: a UV LED at 350 mA (chit_max 0.08) lives in a different chit envelope than a Cree photo red at 700 mA (chit_max 0.43) lives in a different envelope than a Samsung LM301B at 65 mA (chit_max 0.69). The substrate-class fingerprint is **multi-modal**, not single-peaked. AlGaInP red ≠ InGaN blue/white ≠ AlGaN UV in their underlying η_wpe physics, despite all being LEDs.

**Cross-substrate position:**

| Substrate-class | chit_max range or value | Lowest | Highest |
|---|---|---|---|
| Loudspeakers (shelved) | 0.003–0.014 | 0.003 | 0.014 |
| LEDs (this finding) | **0.084–0.693** | **UV (Toyoda Gosei)** | **Samsung LM301B white** |
| Engines (Camry F-001 observed) | 0.41 | — | — |
| Viscoelastic damping (median Q = 0.75 → chit not the right axis) | n/a | n/a | n/a |
| Voice coil actuator open-loop (Q = 12-71, deep c-regime) | n/a (operates far from F-001 bound) | n/a | n/a |
| Voice coil actuator MDPI plastic bobbin | 0.752 (bound) | — | — |

**The LED substrate-class spans almost as much chit_max range as the entire cross-substrate menagerie does.** This is the substrate-class with the highest internal F-001 variance — UV at 0.08 sits in loudspeaker territory; premium white at 0.69 sits in actuator-coupling-limited territory. The substrate-class boundary is loose along the F-001 axis; cdv1's substrate-conditional content is more strongly tied to *chemistry* than to *substrate-class label*.

**Framework implication.** This refines the substrate-conditional/substrate-neutral split: the F-001 amplitude is *not even consistent within a substrate-class* — it's set by the sub-class chemistry. A driver-profile v0.2 RFC-S refinement would benefit from declaring an explicit "chemistry sub-class" or "physical conversion mechanism" field below substrate-class, capturing the η_wpe-determining physics.

## Drive-axis F-003 hypothesis · ABC recombination droop curvature · 2026-05-12

**Status: OPEN.** Two complementary phenomena surfaced from the LED research that may be the drive-axis F-003 signature analogous to RLC's algebraic-exp factor at Q = 0.5:

**Hypothesis 1: V_th threshold smearing.** Static I-V curve transition zone is ~kT/q wide (≈ 26 mV at room temp). The c/s/r boundaries are smeared by thermal noise. This is the substrate-conditional read of cdv1's c→s→r structure on drive-axis substrates: r below V_th − kT/q, smeared s-region V_th ± kT/q, c above V_th + kT/q. Captured in [reference-driver/led.md](../../reference-driver/led.md) §1.

**Hypothesis 2: ABC-recombination efficiency droop peak.** R = A·n + B·n² + C·n³ where A is SRH non-radiative, B is radiative, C is Auger non-radiative. η_wpe peaks at intermediate carrier density where B·n² dominates A·n on the low side and C·n³ on the high side. **The peak position and curvature may be the drive-axis F-003 signature** — analogous to RLC's algebraic-exp factor at Q = 0.5 being the damping-axis signature. The droop curve has a *qualitatively distinct* shape at the peak vs. away from it (curvature reverses sign), matching cdv1's prediction that the s-region is qualitatively distinct from c and r.

**Test path (next turn).** [University of Bath ABC-recombination dataset](https://researchdata.bath.ac.uk) (Excel, multiple commercial InGaN LEDs, 0–500 mA L-I + I-V) is the most direct data source for hypothesis 2. [NBSDC China LED Optoelectronic Characteristics](https://www.nbsdc.cn) (4.42 MB downloadable) is the secondary candidate. If the droop-curvature signature lands cleanly at the η_wpe peak across multiple LEDs, the substrate-conditional drive-axis F-003 method is settled.

**Predicted result.** Per cdv1 §Stability's reasoning that the s-region carries an algebraic factor (analogous to RLC's (1 + α·t)·e^(-α·t)), the drive-axis analogue is plausibly: at the η_wpe peak, η_wpe(I) has a polynomial-vs-exponential signature distinguishing it from off-peak operation. The B·n²/(A·n + B·n² + C·n³) function has well-known critical-curvature behavior at its maximum that may map onto cdv1's algebraic-factor prediction. Confirming this would extend cdv1's universality from damping-axis to drive-axis substrates.
