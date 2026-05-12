# Shelved: loudspeaker research — extraction summary

**Status:** Loudspeakers shelved 2026-05-12 in favor of voice coil linear actuator as substrate zero (cleaner physics, wider chit envelope, more abundant open-data archives). Loudspeakers will be re-engaged in Phase E as a *configured instance* of substrate-zero (voice coil actuator + cone + cavity load), at which point the audiophile c→s→r vocabulary and carb-tuning everyman analogy become rhetorical assets for external publication. See [docs/handoff_next_session.md](../../docs/handoff_next_session.md) Phase E.

**This file:** distilled signal from the first outside-research run (2026-05-11, prompt scoped to canonical loudspeakers, Q_ts↔γ mapping, tunable testbed, acoustic efficiency). The original 47 KB model output had 13 base64-encoded PNGs rendering the Q2 formulas — unreadable as text and ~95% of the file size. Stripped during shelving. Source URLs and tabular content preserved verbatim. Q2 derivation captured cleanly in [docs/handoff_next_session.md](../../docs/handoff_next_session.md) Gotchas section.

---

## Canonical raw-driver candidates (8)

All sourced from Voice Coil magazine — the model didn't surface ASR, Stereophile, Erin's Audio Corner, or Klippel as requested. Voice Coil reviews contain both Thiele/Small parameters and CSD measurements in the same article, so the T/S source URL and CSD source URL are the same per row.

| Driver | Source |
|---|---|
| Scan-Speak Ellipticor 21WE/4542T00 | [Scan-Speak Voice Coil review (Oct 2020)](https://www.scan-speak.dk/datasheet/reviews/21WE-4542T00_VoiceCoil_2020-10.pdf) |
| Scan-Speak Classic 15W/8534T00 | [Scan-Speak Voice Coil review (Jul 2024)](https://www.scan-speak.dk/datasheet/reviews/15W-8534T00_VoiceCoil_2024-7.pdf) |
| Wavecor WF152BD03-04 | [audioXpress test bench](https://www.audioxpress.com/article/test-bench-the-wavecor-wf152bd03-04-paper-cone-midbass-woofer) |
| B&C Speakers 6CXN36 | [Voice Coil Nov 2022](https://www.scribd.com/document/665911535/Voice-Coil-November-2022) |
| Celestion AN2075 | [Celestion Voice Coil](https://celestion.com/wp-content/uploads/2019/10/121.pdf) |
| B&C Speakers DE111-8 | [Voice Coil Aug 2022](https://piratelogic.nl/data/docs/voicecoil/VC-August-2022.pdf) |
| Purifi PTT5.25X-NFA-01 | [Voice Coil Oct 2022](https://www.scribd.com/document/665911562/Voice-Coil-October-2022) |
| Beyma 12CXA400Nd | [Beyma Voice Coil](https://www.beyma.com/wp-content/uploads/VoiceCoil_Octubre_12CXA400Nd_ok.pdf) |

## Q_ts ↔ damping-rate mapping

Formulas in original were rendered as base64 PNG images, unreadable. Standard textbook result captured directly in handoff Gotchas section:

```
γ      = ω₀ / (2 Q_ts)
ω_d    = ω₀ √(1 - 1/(4 Q_ts²))
```

Regime boundaries: Q_ts > 0.5 → c (underdamped), Q_ts = 0.5 → s (critical), Q_ts < 0.5 → r (overdamped). Q = 0.707 is *Butterworth*, not critical.

Note: this Q is identically the actuator-control Q used in substrate zero. Same formulas apply.

## Tunable loudspeaker testbed (Phase C / E candidate)

| Parameter | Value |
|---|---|
| Design | SEAS A26 / Dynaco A25 kit |
| Alignment | Aperiodic vent / Variovent |
| Tuning mechanism | Adjusting damping material (0g to 50g) in the vent |
| Q walk | Decreasing stuffing → lower Q; increasing stuffing → higher Q |
| Per-tuning CSD measurements | No source (would need to be measured) |
| Documentation | [SEAS A26 Kit](https://www.seas.no/index.php?option=com_content&view=article&id=475:seas-a26-kit&catid=66:seas-diy-kits&Itemid=365) |

## Acoustic efficiency (3 of 8 candidates)

Formula: η ≈ 10^((sensitivity − 112) / 10).

| Driver | Sensitivity (dB/W/m) | η | chit_max = -ln(1-η) |
|---|---|---|---|
| Scan-Speak Ellipticor 21WE/4542T00 | 93.5 | 0.0141 | 0.0142 |
| Scan-Speak Classic 15W/8534T00 | 86.0 | 0.0025 | 0.0025 |
| B&C 6CXN36 | 88.7 | 0.0047 | 0.0047 |
| Other 5 candidates | no source | — | — |

**Substrate-class signature already supported by these three data points:** chit envelope ~0.0025–0.0142, two orders of magnitude narrower than engines (~0.41). Loudspeakers radiate into half-space; physics caps efficiency; the chit envelope is structurally near-zero. The F-002-loudspeaker claim ("substrate pre-tuned to its SOC attractor by construction") looks confirmable before any experiment runs. Worth picking back up in Phase E.

## What to revisit when unshelving (Phase E)

- Run the second-pass prompt against ASR / Stereophile / Erin's Audio Corner / Klippel directly — the Voice Coil monoculture in this first pass missed independent CSD measurements.
- SEAS A26 + Variovent stays the canonical Phase C testbed candidate.
- Connect to actuator substrate-zero results: a loudspeaker is a voice coil actuator + cone + cavity. The F-001 relationship across actuator → loudspeaker should be predictable from adding the cone/cavity load to the bare actuator's chit reading.
