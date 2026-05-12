# Actuator research — cross-reference (2026-05-12)

Distilled signal from three outside-model research runs against the actuator-targeted prompt in [docs/handoff_next_session.md](../../docs/handoff_next_session.md). Source files preserved for audit trail:

- [actuator candidates.md](actuator%20candidates.md) — File A. Compact, honest, mostly nulls.
- [Canonical actuator candidates.md](Canonical%20actuator%20candidates.md) — File B. One high-quality verified hit.
- [Linear Voice Coil Actuator Data Search.md](Linear%20Voice%20Coil%20Actuator%20Data%20Search.md) — File C. Broadest, originally bloated with PNG-rendered formulas; cleaned in-place.

## Convergence pattern

| Item | File A | File B | File C |
|---|---|---|---|
| Q↔γ derivation (γ = ω₀/(2Q), ω_d = ω₀√(1-1/(4Q²))) | ✓ text | ✓ text | (in stripped images) |
| Sanity check Q=0.5 critical, Q=0.707 Butterworth, Q=1.0 underdamped | ✓ | ✓ | (in stripped images) |
| Open-data archives have step-response data | null | null | 4 entries |
| Tunable testbed candidates | null | 1 (MDPI 2020) | 3 (AECD, TeachSpin, null on continuous) |
| Specific verified bare-VCA candidate | 0 | 1 | 0–5 (unverified) |

**Near-zero overlap on specific candidates; full convergence on the textbook derivation.** Each model fished a different pond. Cumulative breadth ≈ 14 candidates across three models, but cross-source confirmation is rare.

## Q ↔ damping-rate mapping (consensus)

For voice-coil-driven second-order system m·ẍ + c·ẋ + k·x = (BL)·i(t):

```
ω₀     = √(k/m)
ζ      = c / (2·√(m·k))
Q      = 1 / (2·ζ)             [mechanical quality factor]
γ      = ζ·ω₀ = ω₀ / (2Q)      [exponential decay rate]
ω_d    = ω₀·√(1 - ζ²) = ω₀·√(1 - 1/(4Q²))   [damped oscillation frequency]
```

Regime mapping:

| Q | ζ | γ/ω₀ | ω_d/ω₀ | Regime |
|---|---|---|---|---|
| 0.5 | 1.0 | 1.0 | 0.0 | s (critically damped) |
| 0.707 | 0.707 | 0.707 | 0.707 | c (Butterworth — *underdamped, not critical*) |
| 1.0 | 0.5 | 0.5 | 0.866 | c (underdamped) |
| < 0.5 | > 1.0 | > ω₀ | imaginary (two real exponentials) | r (overdamped) |

## Canonical actuator candidates (ranked)

### Tier 1 — verified, full data

| Candidate | Source | Verified | Provides |
|---|---|---|---|
| **MDPI Actuators 2020, 9(1):8** — *Effect of Electromagnetic Damping on System Performance of Voice-Coil Actuator Applied to Balancing-Type Scale* | File B | ✓ open access, paper exists, setup matches | Bare cantilever + bobbin + magnet (no cone/cavity). Full EM/mechanical parameters (m=0.0652 kg, k=1.485 N/mm, R=28.9 Ω, L=24.535 mH, BL=28.46 N/A). Two configured instances (Al bobbin Q≈0.033, plastic bobbin Q≈0.39). Step responses in Figures 12–13. [PDF mirror](https://www.researchgate.net/publication/339014719) |

**Caveat:** both Q values land in r-regime (overdamped). Excellent for F-001-actuator and F-002-actuator (chit reading at steady state); insufficient for full F-003 c→s→r walk. Needs a supplement to reach c-regime.

### Tier 2 — verified open-source benchmark (promoted 2026-05-12)

| Candidate | Source | Verified | Provides |
|---|---|---|---|
| **IEEJ HDD positioning benchmark (PyHDDBenchmark)** | File C → verified via GitHub | ✓ open source ([macs-lab/PyHDDBenchmark](https://github.com/macs-lab/PyHDDBenchmark)), real HDD plant measurement data | Plant model derived from real HDD measurements (Atsumi & Yabui 2020 IEEE TIE 67(11):9184). **VCM: 16 modes**, ω ∈ [0, 44800] rad/s, ζ ∈ [0.007, 0.04] → **Q ∈ [12.5, 71], all c-regime**. **PZT: 8 modes**, Q ∈ [1.67, 62.5]. `Fre_Resp.json` frequency-response data + `Data_RRO.txt` time-series. Industry-standard, IEEJ-supported, IEEE-cited. |

**The c-regime contrast finding:** MDPI 2020 cantilever VCA sits in r-regime (Q ≈ 0.033–0.39). PyHDDBenchmark HDD VCM sits deeply in c-regime (Q ≈ 12.5–71). Combined chit-envelope range across two substrate-zero instances spans the c/r boundary but skips the s-boundary. F-001-actuator gets ~26 data points across two physical substrates of the same class.

**F-002 contrast finding worth recording in FOOTING:** HDD VCMs are *deliberately engineered for c-regime* — sharp resonance peaks closed externally by feedback control, NOT operated near chit ≈ 0. This contrasts engines (chit ≈ 0 by SOC self-tuning at idle) and loudspeakers (chit ≈ 0 by half-space radiation efficiency cap). **The SOC-attractor reading of F-002 is substrate-conditional**, not universal — some substrates live near chit ≈ 0 by construction; others live far and have external controllers close the gap. cdv1 §Active modulation handles the plant+controller decomposition.

### Tier 2b — other unverified candidates from File C

| Candidate | Source | URL | Why it might work |
|---|---|---|---|
| Mendeley OPU force analyzer | File C | [10.17632/cnkd95kp65.1](https://doi.org/10.17632/cnkd95kp65.1) | HD-DVD VCM / OIS-scale, Mendeley DOI suggests downloadable |
| Zenodo haptic texture VCA | File C | [10.5281/zenodo.4813359](https://doi.org/10.5281/zenodo.4813359) | Haptic linear VCA, Zenodo DOI suggests downloadable |
| MDPI Actuators 2023, 12(3):132 | File C | [mdpi.com/2076-0825/12/3/132](https://www.mdpi.com/2076-0825/12/3/132) | Macro-Micro VCM dual-stage positioner, open access |

### Tier 3 — Southampton inertial actuator family

| Candidate | Source | Note |
|---|---|---|
| Southampton inertial actuator (m=20.3g, K=135N/m, D=1Ns/m, Ψ=2.6N/A, Re=1.8Ω, Le=1.4mH) | File A | [eprints.soton.ac.uk/465699](https://eprints.soton.ac.uk/465699/1/984284.pdf). Parameters published but File A reports "no step-response source." Dal Borgo et al. 2019 (the original recommendation when we framed the actuator prompt) is in this family — worth re-checking for embedded step-response figures. |

## Tunable testbed candidates (Phase C)

### Bonus finding worth flagging: TeachSpin Torsional Oscillator

| Testbed | Source | Status |
|---|---|---|
| **TeachSpin Torsional Oscillator** | File C | [teachspin.com/torsional-oscillator](https://www.teachspin.com/torsional-oscillator). Pedagogical physics apparatus *designed for demonstrating c→s→r damping regimes* — eddy-current damping tunable across the full range. Rotary (torsion pendulum), not linear, but mathematically identical second-order system. Substrate-1.5 candidate. |

The TeachSpin is rotary geometry but a linear (mathematical) second-order damped oscillator — same ODE, same Q definition, same c→s→r structure. If linear-VCM data for the full Q walk remains scarce after Tier 2 verification, this is the cleanest substrate to use for F-003 directly — designed for the experiment we want to run.

### Other testbed candidates

- **MDPI Actuators 2020 Al/plastic bobbin** (Tier 1) — discrete Q points within r-regime, not a continuous walk.
- **Active Eddy Current Damper VCM** (File C, [ResearchGate](https://www.researchgate.net/publication/379522938)) — discrete linear, ResearchGate-only.
- **Continuous Q-walking linear actuator testbed** — *all three models converged on null source*. Strong signal that this kind of data isn't published anywhere accessible.

## Open-data archive scan (consensus)

Files A and B independently confirm: **systematic scan of Zenodo, Mendeley Data, IEEE DataPort, MDPI Actuators supplementary files, DSpace@MIT, ePrints Soton returns essentially no machine-readable time-series step-response datasets for bare linear voice coil actuators.** File C found 4 entries on the same archives — to be verified individually before relying on them. Three-model consensus says the open-data assumption from the SOURCES.md §1 list was optimistic.

## Recommendation for Phase A (updated 2026-05-12 after PyHDDBenchmark verification)

1. **Stack two substrate-zero instances: MDPI 2020 + PyHDDBenchmark.** Complementary regimes (r vs c), same substrate-class (linear voice coil actuator). F-001-actuator gets ~26 data points across two physical substrates. F-002-contrast finding lands directly in FOOTING.
2. **F-003 c→s→r walk: pull RLC (substrate-two) forward into Phase A.** PyHDDBenchmark is a fixed plant (not tunable); MDPI 2020 only spans r-regime. The c→s→r walk wants a substrate where Q is *continuously tunable*, and RLC delivers this trivially — vary R, walk c→s→r. Ron-confirmed mature; closed-form damped sinusoidal step response per textbook. Substrate-two was queued for "null check" anyway; pulling forward to handle F-003 doubles its work.
3. **Tier 3 (Southampton inertial) and TeachSpin torsional oscillator** held as backup substrates if either path stalls.

## What this assessment does NOT do

- Verify Tier 2b candidates beyond URL plausibility (Mendeley OPU, Zenodo haptic, MDPI 2023). Held as backup.
- Cover substrate-class extensions ron flagged for backlog (stepper motors, mechanical switches / debounce, RC circuits). See [SOURCES.md §7 Substrate backlog](SOURCES.md).
