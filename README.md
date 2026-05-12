# mpa-relaxation

A finding-centric substrate characterization under the mpa framework. Tests cdv1's substrate-agnostic claim: the c→s→r damping regime structure should appear in any tunable driven-dissipative system whose recovery profile can be observed. Substrates are evidence; the *finding* is the repo's organising principle.

## What this repo is for

cdv1 ([mpa-atlas/framework/cdv1_compressed.md](https://github.com/ronviers/mpa-atlas/blob/main/framework/cdv1_compressed.md)) §Stability predicts a regime structure organised by the chit control parameter:

- chit > 0 → c-regime: underdamped, oscillatory return
- chit ≈ 0 → s-regime: critically damped, algebraic settling
- chit < 0 → r-regime: overdamped, sluggish

This repo collects substrate characterizations where the **damping parameter is tunable** and the **recovery profile is measurable**, then tests whether the same chit definition and same regime structure recur across substrates. The *finding* emerges from the cross-substrate comparison.

## Substrate roadmap

| Substrate | Status | Role |
|---|---|---|
| **0. Voice coil linear actuator** | active | Substrate zero — bare coil-magnet-flexure-load. Cleanest single-mode driven-dissipative oscillator with a knob-tunable Q. Abundant open-data archives (Zenodo, Mendeley, IEEE DataPort, MDPI Actuators). |
| **1. IC engines** | cited, frozen | F-001 confirmed on Camry (chit_max ≈ 0.41). See [mpa-engine](https://github.com/ronviers/mpa-engine). |
| **2. RLC circuit** | queued | Textbook null check — framework should clearly work in a second-order linear system with no substrate complications. |
| **3. Viscoelastic damping materials (via MatWeb / ASTM E756)** | queued | Real-world heterogeneity stress test — does the framework still work across hundreds of materials with vendor-claimed loss factors? |
| **Loudspeaker (cone + cavity)** | **shelved** | Loudspeaker = voice coil actuator with cone load + cavity. Same substrate-class as substrate-zero with an *added configured instance*. Shelved temporarily — return after substrate-zero lands. The audiophile c→s→r vocabulary and carb-tuning analogy make this the strongest rhetorical substrate for eventual external publication. |

## Substrate zero: voice coil linear actuator

A linear voice coil actuator is a coil moving in a magnetic field, generating force F = BL·i under electrical drive, mechanically constrained by a suspension and load. The substrate strips out the loudspeaker's cone and cavity — leaving the bare driven-dissipative oscillator:

- Coherence: sustained position-tracking under drive.
- G₀: electrical power delivered to the coil = V·I = I²·R + BL·v·I.
- L: mechanical (suspension damping + load damping) + electrical resistive (I²·R thermal) + electromagnetic eddy/back-EMF losses. Substrate-decomposed.
- chit = ln(G₀ / L). Load-dependent: chit envelope sits in ~0.1–0.5 range depending on load mass and damping — between engines (~0.4) and loudspeakers (~0.02).

The c→s→r tuning practice for voice coil actuators is the engineering practice of settling-time tuning: hard disk drive head positioning, camera optical image stabilization (OIS), semiconductor lithography stage control, haptic linear resonant actuators (LRAs), inertial actuators for active vibration control. Q is walked across the c→s→r range routinely; per-Q step-response data is industry-standard.

## Substrate one: engines (cited)

[mpa-engine](https://github.com/ronviers/mpa-engine) carries the IC-engine substrate-class instance. F-001 confirmed: chit_max ≈ -ln(1 - η_thermal,max) on the Camry 2.4L 2AZ-FE. Frozen at v0; this repo cites it.

## Run

(Scaffold only — no kernel yet. See [docs/handoff_next_session.md](docs/handoff_next_session.md) for what's queued.)

## Discipline

See [CLAUDE.md](CLAUDE.md) for the finding-centric carve-out (deviation from sibling pattern). Per-substrate driver profiles and calibration records follow mpa-atlas thin-RFC discipline; kernel code is normal engineering.

## Coordinates

| Document | Where |
|---|---|
| Open work | [docs/handoff_next_session.md](docs/handoff_next_session.md) |
| Cross-substrate findings | [docs/journey/FOOTING.md](docs/journey/FOOTING.md) |
| Voice coil actuator driver profile | [reference-driver/voice-coil-actuator.md](reference-driver/voice-coil-actuator.md) |
| Engine instance (cited, frozen) | [github.com/ronviers/mpa-engine](https://github.com/ronviers/mpa-engine) |
| cdv1 (framework being instanced) | [mpa-atlas/framework/cdv1_compressed.md](https://github.com/ronviers/mpa-atlas/blob/main/framework/cdv1_compressed.md) |
| RFC-S (driver profile shape) | [mpa-atlas/rfcs/MPA-RFC-S_Scale-Management.md](https://github.com/ronviers/mpa-atlas/blob/main/rfcs/MPA-RFC-S_Scale-Management.md) |
| RFC-C (calibration-record shape) | [mpa-atlas/rfcs/MPA-RFC-C-Calibration.md](https://github.com/ronviers/mpa-atlas/blob/main/rfcs/MPA-RFC-C-Calibration.md) |
