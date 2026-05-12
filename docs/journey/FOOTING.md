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
