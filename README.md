# mpa-relaxation

A finding-centric substrate characterization under the mpa framework. Tests cdv1's substrate-agnostic claim: the c→s→r damping regime structure should appear in any tunable driven-dissipative system whose recovery profile can be observed. Substrates are evidence; the *finding* is the repo's organising principle.

## What this repo is for

cdv1 ([mpa-atlas/framework/cdv1_compressed.md](https://github.com/ronviers/mpa-atlas/blob/main/framework/cdv1_compressed.md)) §Stability predicts a regime structure organised by the chit control parameter:

- chit > 0 → c-regime: underdamped, oscillatory return
- chit ≈ 0 → s-regime: critically damped, algebraic settling
- chit < 0 → r-regime: overdamped, sluggish

This repo collects substrate characterizations where the **damping parameter is tunable** and the **recovery profile is measurable**, then tests whether the same chit definition and same regime structure recur across substrates. Substrate zero: **loudspeakers** (canonical, abundant free measurement data, tuning parameter Q_ts is one number, three loss channels pre-decomposed in every datasheet). Substrate one: **gasoline IC engines** (cited from [mpa-engine](https://github.com/ronviers/mpa-engine), frozen). Future candidates: RLC circuits, tuning forks, piano strings, mechanical vibration isolators.

## Why finding-centric, not substrate-centric

Existing sibling repos (mpa-brain, mpa-engine, mpc-glass) follow one substrate per repo. This repo deviates: the load-bearing question is universality, not a single substrate's amplitudes. Engines are one data point; loudspeakers are another. Each substrate-class still earns its own driver profile and calibration records (per RFC-S §4 / RFC-C §2). The *finding* emerges from the cross-substrate comparison those records enable.

## Substrate zero: loudspeakers

A loudspeaker is a one-mode driven-dissipative oscillator with three pre-decomposed loss channels and a literature-standard target damping. Thiele/Small parameters split total Q (Q_ts) into Q_es (electrical, back-EMF), Q_ms (mechanical), and radiation losses. Audiophiles use the c→s→r vocabulary daily: *boomy* (underdamped), *tight/articulate* (critical), *dry/lifeless* (overdamped). The substrate is **pre-tuned to its SOC attractor** by engineering convention (Q_ts ≈ 0.707 Butterworth alignment) — a sharper F-002-class statement than engines provide.

cdv1 reads:

- Coherence: faithful cone displacement tracking the input voltage modulo a linear transfer function.
- G₀: electrical power delivered to the voice coil.
- L: Q_es + Q_ms + radiation losses. Substrate-decomposed.
- chit = ln(G₀ / L). Acoustic conversion efficiency ~1–3% → chit_max ≈ -ln(1 - 0.02) ≈ 0.02. Speakers live in a *very narrow* envelope near chit = 0 by physical construction.

## Substrate one: engines (cited)

[mpa-engine](https://github.com/ronviers/mpa-engine) carries the IC-engine substrate-class instance. F-001 confirmed: chit_max ≈ -ln(1 - η_thermal,max) on the Camry 2.4L 2AZ-FE. F-002 provisional. That repo is frozen at v0; this one cites it.

## Run

(Scaffold only — no kernel yet. See [docs/handoff_next_session.md](docs/handoff_next_session.md) for what's queued.)

## Discipline

See [CLAUDE.md](CLAUDE.md) for the finding-centric carve-out (deviation from sibling pattern). Per-substrate driver profiles and calibration records follow mpa-atlas thin-RFC discipline; kernel code is normal engineering.

## Coordinates

| Document | Where |
|---|---|
| Open work | [docs/handoff_next_session.md](docs/handoff_next_session.md) |
| Cross-substrate findings | [docs/journey/FOOTING.md](docs/journey/FOOTING.md) |
| Loudspeaker driver profile (forthcoming) | [reference-driver/loudspeaker.md](reference-driver/loudspeaker.md) |
| Engine instance (cited substrate, frozen) | [github.com/ronviers/mpa-engine](https://github.com/ronviers/mpa-engine) |
| cdv1 (framework being instanced) | [mpa-atlas/framework/cdv1_compressed.md](https://github.com/ronviers/mpa-atlas/blob/main/framework/cdv1_compressed.md) |
| RFC-S (driver profile shape) | [mpa-atlas/rfcs/MPA-RFC-S_Scale-Management.md](https://github.com/ronviers/mpa-atlas/blob/main/rfcs/MPA-RFC-S_Scale-Management.md) |
| RFC-C (calibration-record shape) | [mpa-atlas/rfcs/MPA-RFC-C-Calibration.md](https://github.com/ronviers/mpa-atlas/blob/main/rfcs/MPA-RFC-C-Calibration.md) |
