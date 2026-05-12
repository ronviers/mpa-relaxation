# Sources

Pointers to substrate-data archives used in this repo. Finding-centric repo, so multiple substrates appear here. Each substrate gets a section.

## §1 Voice coil linear actuators (substrate zero)

### §1.0 Research outputs (2026-05-12)

Three outside-model research runs against the actuator-targeted prompt landed 2026-05-12. Distilled cross-reference at [actuator-research-cross-reference.md](actuator-research-cross-reference.md); raw outputs preserved:

- [actuator candidates.md](actuator%20candidates.md)
- [Canonical actuator candidates.md](Canonical%20actuator%20candidates.md)
- [Linear Voice Coil Actuator Data Search.md](Linear%20Voice%20Coil%20Actuator%20Data%20Search.md) — cleaned in-place, ~42 KB of unreadable PNG-rendered formulas stripped

**Top-ranked candidate (verified):** [Effect of Electromagnetic Damping on System Performance of Voice-Coil Actuator Applied to Balancing-Type Scale](https://www.mdpi.com/2076-0825/9/1/8) (MDPI Actuators 2020, 9(1):8). Bare cantilever + bobbin + magnet VCA. Full electromagnetic and mechanical parameters in Table 2. Step responses in Figures 12–13. Two configured instances (Al bobbin, plastic bobbin) demonstrating eddy-current damping tuning. Caveat: both Q values land in r-regime; Phase C supplementation needed for c→s→r walk.

**Empirical update to §1.1 below:** systematic open-data scan returned essentially null for bare-VCA step-response time-series. The archives listed below remain authoritative entry points, but the *expected* presence of machine-readable datasets was optimistic. Bias toward paper PDFs with embedded figures rather than supplementary `.csv` / `.mat` files.

### §1.1 Open-data archives

- **Zenodo** — [zenodo.org](https://zenodo.org). CERN-funded open-science catch-all. Search keys: "voice coil actuator", "linear actuator dataset", "VCM characterization". Common upload: raw `.csv` / `.mat` time-series from university test rigs (position, current, force, displacement).
- **Mendeley Data** — [data.mendeley.com](https://data.mendeley.com). Elsevier-operated. Search keys: "voice coil motor", "electromagnetic actuator hysteresis", "linear actuator dynamic performance". Engineering-researcher heavy.
- **IEEE DataPort** — [ieee-dataport.org](https://ieee-dataport.org). Gold standard for electrical-engineering datasets. Some require IEEE subscription; thousands open-access. Linear actuator, motor control, magnetic field analysis datasets.
- **DSpace@MIT** — [dspace.mit.edu](https://dspace.mit.edu). MIT theses and dissertations with embedded experimental data; aerospace and precision mechanical engineering bias.
- **ePrints Soton** — [eprints.soton.ac.uk](https://eprints.soton.ac.uk). University of Southampton; strong mechanical research presence. Notable: Dal Borgo et al. 2019, *Identification and analysis of nonlinear dynamics of inertial actuators* (Mech. Sys. Sig. Proc. 115, 338–360, [doi:10.1016/j.ymssp.2018.05.044](https://doi.org/10.1016/j.ymssp.2018.05.044)) — broadband white-noise and sine-sweep test rig for coil-magnet transducers, back-EMF identification, linear parameter extraction.
- **MDPI Actuators** — [mdpi.com/journal/actuators](https://www.mdpi.com/journal/actuators). Open-access journal; supplementary data files commonly attached. Notable candidates: Tran & Hwang 2020 (*Design and Simulation of Electromagnetic Linear Actuators for Jet Dispensers*, Applied Sciences 10(5):1653, [doi:10.3390/app10051653](https://doi.org/10.3390/app10051653)); Preechayasomboon & Rombokas 2021 (*Sensuator: A Hybrid Sensor–Actuator Approach to Soft Robotic Proprioception*, Actuators 10(2):30, [doi:10.3390/act10020030](https://doi.org/10.3390/act10020030)).
- **Frontiers** — [frontiersin.org](https://www.frontiersin.org). Open-access publisher with empirical actuator data common in robotics and haptics journals. Notable: Paisa et al. 2023 on tactile displays (*Front. Comput. Sci.*, [doi:10.3389/fcomp.2023.1085539](https://doi.org/10.3389/fcomp.2023.1085539)).

### §1.2 Industrial reference designs

- **Hard drive VCM datasheets** — Western Digital, Seagate, Toshiba. BL product, R, L, M, K commonly published in seek-time engineering papers. The HDD industry has decades of per-firmware-version seek profile data (under NDA mostly, but academic characterizations exist).
- **Camera OIS actuators** — Smartphone camera modules (e.g., LG Innotek, Mitsumi). VCM-based optical image stabilization; bandwidth and settling specs in white papers.
- **Haptic LRAs** — Linear resonant actuators in phones / haptic feedback devices. Q ≈ 50–100, narrow-band by design; settling profile published in motor control literature.
- **Semiconductor lithography stages** — ASML, Nikon, Canon. Voice coil + magnetic-bearing stages with sub-nm settling; characterized to extreme precision. Open-access papers exist on the control architectures, less on raw substrate data.

### §1.3 Substrate-class theory

- Standard second-order linear system: ẍ + 2γẋ + ω₀²x = (BL/M)·i. Q = ω₀/(2γ). Settling time and damping in any control engineering text.
- Klippel large-signal extensions (also used in actuator characterization, not just speakers): [klippel.de/know-how/literature/application-notes.html](https://www.klippel.de/know-how/literature/application-notes.html).

## §2 Engines (substrate one, cited)

See [mpa-engine/data/sources/SOURCES.md](https://github.com/ronviers/mpa-engine/blob/main/data/sources/SOURCES.md). F-001 confirmed at chit_max ≈ 0.41 on the Camry 2.4L 2AZ-FE. Cross-substrate use here is read-only from that record; no new engine data lands in this repo.

## §3 RLC circuits (substrate-two queued)

Textbook substrate. No archive needed — measurements or SPICE simulations are reproducible from first principles. Standard reference: Sedra & Smith *Microelectronic Circuits*, or any introductory electrical engineering text. Closed-form damped sinusoidal step response: x(t) = e^(-γt)·[A·cos(ω_d·t) + B·sin(ω_d·t)] for Q > 0.5; over-damped form (sum of two real exponentials) for Q < 0.5. NIST electrical metrology (volt, ohm, farad) traceability available but not required.

## §4 Viscoelastic damping materials (substrate-three queued)

- **MatWeb** — [matweb.com](https://www.matweb.com). Aggregator of vendor datasheets. Search for damping / loss factor / tan δ. Free tier; provenance is vendor-claimed (often via ASTM E756).
- **MakeItFrom** — [makeitfrom.com](https://www.makeitfrom.com). Engineering-property comparison.
- **Vendor data sheets** — 3M VHB (constrained-layer damping films), Roush (automotive viscoelastics), SoundCoat (acoustic damping), McMaster-Carr damping product catalog. Loss factor vs. frequency curves common.
- **ASTM E756** — [astm.org/e0756-05r17.html](https://www.astm.org/e0756-05r17.html). Vibrating-beam damping measurement standard. Standard paywalled; results published by vendors / labs are typically free.
- **Granta EduPack** (was CES Selector) — [ansys.com/products/materials/granta-edupack](https://www.ansys.com/products/materials/granta-edupack). Cambridge materials database with damping section; free for academics.

## §5 Shelved: loudspeakers

A loudspeaker is a voice coil actuator (substrate zero) with a cone + cavity bolted on as load. Will be characterized later as a *configured instance* of substrate-zero, not as a separate substrate. Prior research:

- [shelved-loudspeaker-research.md](shelved-loudspeaker-research.md) — first outside-model research run, 2026-05-11. Eight raw-driver candidates from Voice Coil magazine (Scan-Speak, Wavecor, B&C, Celestion, Beyma, Purifi); SEAS A26 / Dynaco A25 with Variovent as tunable testbed; acoustic efficiencies for three of the eight giving chit_max ≈ 0.003–0.014.
- Future archive sources to revisit when unshelving: [ASR](https://www.audiosciencereview.com), [Stereophile](https://www.stereophile.com), [Erin's Audio Corner](https://www.erinsaudiocorner.com), [Klippel R&D](https://www.klippel.de/r-d.html).

## §6 Adjacent literature (cross-substrate framing)

- The engine-transient research dump from mpa-engine ([Engine Transient Data Research Sources](https://github.com/ronviers/mpa-engine/blob/main/data/sources/Engine%20Transient%20Data%20Research%20Sources.md)) frames IC engines as canonical multi-timescale dissipators where the natural physical decay tail is slower-than-exponential, partly erased by ECU dashpot algorithms. That framing motivates the substrate-pivot to bare voice coil actuators: no engineered exponential overlay, natural physical c→s→r structure shows up clean.
