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

### Tier 2 — unverified, plausible downloadable datasets

| Candidate | Source | URL | Why it might work |
|---|---|---|---|
| MathWorks/IEEJ HDD benchmark | File C | [fileexchange/111515](https://jp.mathworks.com/matlabcentral/fileexchange/111515-magnetic-headpositioning-control-system-in-hdds) | Dual-stage VCM + PZT magnetic head positioning, industry-standard benchmark from IEEJ Japan; likely has open-loop plant data |
| Mendeley OPU force analyzer | File C | [10.17632/cnkd95kp65.1](https://doi.org/10.17632/cnkd95kp65.1) | HD-DVD VCM / OIS-scale, has Mendeley DOI suggesting downloadable dataset |
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

## Recommendation for Phase A

1. **Canonical actuator: MDPI Actuators 2020, 9(1):8.** Run F-001-actuator and F-002-actuator end-to-end against this paper. Two Q points means we get two data points on the chit envelope. Substrate-zero v0.1 driver profile populates with concrete amplitudes.
2. **Phase C supplementation in priority order:**
   a. Verify MathWorks/IEEJ HDD benchmark — if open-loop step-response across firmware tunings is downloadable, F-003-actuator lands here.
   b. If (a) fails, fall through to TeachSpin torsional oscillator as the c→s→r testbed. Reframe substrate-zero scope: from "linear voice coil actuator" to "single-mode second-order driven-dissipative oscillator," with the torsion pendulum and linear VCA as two instances of the same substrate-class.
3. **Tier 3 (Southampton inertial)** held as backup if Tier 1 stalls on the r-only constraint.

## What this assessment does NOT do

- Select a canonical actuator (user decision). This document presents the ranked options.
- Verify Tier 2 candidates beyond URL plausibility. Each one needs a fetch + parameter-presence check before commitment.
- Resolve the "Q values in MDPI 2020 are both r-regime" gap. Decision deferred to user: accept r-only and supplement, or replace with a candidate (Southampton family, or another) that reaches c-regime.
