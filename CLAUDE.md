# Discipline: implementation, not protocol — finding-centric variant

This repo is a **cross-substrate finding characterization** under the mpa framework. It tests cdv1's ([mpa-atlas/framework/cdv1_compressed.md](https://github.com/ronviers/mpa-atlas/blob/main/framework/cdv1_compressed.md)) substrate-agnostic claim that the c→s→r damping regime structure recurs in every tunable driven-dissipative system whose recovery profile is observable.

## Deviation from sibling pattern

Existing mpa-* and mpc-* repos are substrate-centric: one substrate-class per repo (mpa-brain, mpa-engine, mpc-glass). This repo is **finding-centric**: one *finding* (c→s→r damping universality), with multiple substrates as evidence. Each substrate-class characterized here still earns its own driver profile (`reference-driver/<substrate>.md`) and calibration records, shaped per RFC-S §4 / RFC-C §2. The repo's purpose is the cross-substrate comparison those records enable, not the per-substrate amplitudes themselves.

## What thin-RFC discipline does and does not govern here

[mpa-atlas](https://github.com/ronviers/mpa-atlas) carries [thin-RFC discipline](https://github.com/ronviers/mpa-atlas/blob/main/CLAUDE.md). Same carve-out as siblings:

- **Protocol artifacts** (`reference-driver/*.md`, calibration record JSON, driver-profile shape) — thin-RFC discipline applies. Half-page targets, point at mpa-atlas RFCs for rigor.
- **Source code** (`mpa_relaxation_packs/**`) — normal engineering.
- **Experiments** (`experiments/**`) — normal engineering. Small scripts that compute chit, fit decay tails, and compare substrates.
- **Cross-substrate findings** (`docs/journey/FOOTING.md`) — append-only journey log. Each footing entry is one finding with its multi-substrate evidence.

## What this repo is for

- Test cdv1's c→s→r prediction across at least two substrates with shared formalism: a chit definition, a measurable recovery profile, a fit of exponential vs. algebraic decay.
- **Substrate zero: voice coil linear actuator.** Coil-magnet-flexure-load. Q is knob-tunable (load mass, damping coefficient, eddy-current braking). Open-data archives abundant: Zenodo, Mendeley Data, IEEE DataPort, MDPI Actuators, DSpace@MIT, ePrints Soton. The c→s→r tuning practice is industry-standard (HDD seek, OIS, lithography, haptics).
- **Substrate one: IC engines**, cited from [mpa-engine](https://github.com/ronviers/mpa-engine) (frozen; F-001 confirmed at chit_max ≈ 0.41 on Camry).
- **Substrate two queued: RLC circuit.** Textbook null check.
- **Substrate three queued: viscoelastic damping materials via MatWeb / ASTM E756.** Real-world heterogeneity stress test.
- **Shelved (commit to return): loudspeakers.** A loudspeaker is a voice coil actuator with cone + cavity load — same substrate-class as substrate-zero with an added configured instance. The audiophile c→s→r vocabulary and carb-tuning analogy make it the strongest *rhetorical* substrate for eventual external publication. Shelving now so substrate-zero work isn't slowed by audio-niche data hunting; returning once the bare-actuator substrate lands.

## What this repo is not for

- **Substrate physics derivations.** The voice coil's electromagnetic coupling, the engine's combustion chemistry, the piano string's wave equation — out of scope. We read each substrate's published measurement apparatus as its exchange surface.
- **mpa-atlas schema authoring.** Schemas live upstream.
- **Actuator design / engine tuning / loudspeaker design.** We observe outputs, we don't redesign substrates.

## Substrate-neutral content lives upstream

cdv1's c→s→r structure, the chit definition, and §Stability's algebraic-settling prediction are framework content in [mpa-atlas](https://github.com/ronviers/mpa-atlas/blob/main/framework/cdv1_compressed.md). This repo cites them and supplies per-substrate amplitudes plus the cross-substrate **demonstration** of universality.

If you find yourself encoding cdv1 universality content inside this repo, stop — that belongs in mpa-atlas. The cross-substrate evidence for that content lives here.

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
