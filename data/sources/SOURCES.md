# Sources

Pointers to substrate-data archives used in this repo. Finding-centric repo, so multiple substrates appear here. Each substrate gets a section.

## §1 Voice coil linear actuators (substrate zero)

### §1.0 Research outputs (2026-05-12)

Three outside-model research runs against the actuator-targeted prompt landed 2026-05-12. Distilled cross-reference at [actuator-research-cross-reference.md](actuator-research-cross-reference.md); raw outputs preserved:

- [actuator candidates.md](actuator%20candidates.md)
- [Canonical actuator candidates.md](Canonical%20actuator%20candidates.md)
- [Linear Voice Coil Actuator Data Search.md](Linear%20Voice%20Coil%20Actuator%20Data%20Search.md) — cleaned in-place, ~42 KB of unreadable PNG-rendered formulas stripped

**Substrate-zero stack (both verified 2026-05-12):**

1. **[MDPI Actuators 2020, 9(1):8](https://www.mdpi.com/2076-0825/9/1/8)** — *Effect of Electromagnetic Damping on System Performance of Voice-Coil Actuator Applied to Balancing-Type Scale*. Bare cantilever + bobbin + magnet VCA. Full EM/mechanical parameters in Table 2. Step responses in Figures 12–13. Two configured instances (Al / plastic bobbin) — **Q ≈ 0.033 and 0.39, both r-regime**.
2. **[PyHDDBenchmark](https://github.com/macs-lab/PyHDDBenchmark)** (open-source Python port of IEEJ HDD positioning benchmark by Atsumi & Yabui 2020). Real HDD plant measurement data: **16 VCM modes** with **Q ∈ [12.5, 71], all c-regime**, plus 8 PZT modes. `plant.py` has modal parameters; `Fre_Resp.json` is the frequency-response data; `Data_RRO.txt` is time-domain RRO (Repeatable Run-Out) disturbance.

**PyHDDBenchmark local clone instructions** (used by F-002-restoration experiment; not committed to this repo per `.gitignore`):

```
git clone https://github.com/macs-lab/PyHDDBenchmark.git data/external/PyHDDBenchmark
```

Phase data in `Fre_Resp.json` is in **radians**, not degrees. (First-pass ingest applied an erroneous deg→rad conversion; corrected 2026-05-12. Future ingests of similar FRF datasets: check phase units before computing complex transfer functions.)

Together: ~26 (Q, ω) data points spanning r-regime and c-regime in the voice-coil-actuator substrate-class. F-002 contrast finding: HDD VCMs are deliberately engineered for c-regime (sharp resonances + external controller), NOT chit ≈ 0 — substrate-class fingerprint divergence vs engines/loudspeakers.

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

## §7 Substrate backlog

Substrate candidates flagged for later, not pulled into the current roadmap. Each one earns activation when a specific finding wants it or when a previously-planned substrate stalls.

### §7.1 Stepper motors

Stepper motors are voice coil actuators in a *configuration with discrete equilibria* — periodic-impulse-driven multi-stable substrate. The inter-step settling oscillation is a damped second-order response we'd want to read. Q of bounce/ring around each step is well-characterized in motor literature (every datasheet specifies "step settling time"). Substrate complexity higher than substrate-zero because of the multi-stable structure — adds an analytical layer that bare voice coil actuators don't have. Strong candidate for stress-testing the framework against more complex configurations. Data abundance: high (every stepper datasheet, lots of academic motor-control literature).

### §7.2 Mechanical switches / debounce

Switch contact bounce is a damped oscillation of the contact mass-spring system. Every digital input on every circuit board ever made has this exact tuning problem; debounce filters (RC, software, or Schmitt-trigger) are downstream band-aids for underdamped mechanical switches. Q values typically 1–20 for snap-action switches. Both r-regime (heavy contact, oil-filled, gold-plated) and c-regime (cheap dome-switch, membrane) substrates exist commercially.

Rhetorical appeal high: switch debounce is a universally-familiar engineering problem at microelectronics scale, paralleling the carb-tuning scenario at engine scale. The tunable parameter is contact design (mass, spring stiffness, dome shape). Data: every switch datasheet has bounce-time numbers; oscilloscope traces are ubiquitous in electronics textbooks and YouTube videos.

Subtlety same as engines' return-to-idle: substrate's steady-state is "switch open" or "switch closed," not a sustained NESS at chit ≈ 0. The c→s→r read is on the bounce *recovery profile*, which is the F-003 test. Fits naturally.

### §7.3 RC circuits (first-order, r-regime endpoint)

RC is a *first-order* driven-dissipative system (single timescale τ = RC; only exponential relaxation, no oscillation). Unlike RLC, an RC circuit doesn't have a c-regime at all because there's no energy-storage-back mechanism — capacitor charges/discharges monotonically toward the source voltage.

**Useful but not for the c→s→r walk.** Ron flagged "capacitors as forced relaxation" — sharp framing. A driven RC circuit is exactly cdv1's driven-dissipative setup with the oscillation pole stripped. chit reading is well-defined: G₀ = V_source²/R during charging, L = I²R, chit > 0 while charging, → 0 at equilibrium. RC sits at the *purely-overdamped extreme* of the substrate-class. Useful as a data point at the far r-regime end of the F-001 universality test; useless for the c→s→r walk because it only has one regime.

Pairing note: substrate-two RLC (already in roadmap) reduces to RC in the limit L → 0. The substrate-zero / RLC / RC chain is a continuum of second-order-with-decreasing-storage substrates.

### §7.4 TeachSpin Torsional Oscillator (pocket fallback)

Pedagogical apparatus designed for demonstrating c→s→r damping regimes via tunable eddy-current damping. Rotary geometry, mathematically identical second-order oscillator. Held as the substrate to fall through to if the c→s→r walk via RLC feels too synthetic and we want real-apparatus data. [teachspin.com/torsional-oscillator](https://www.teachspin.com/torsional-oscillator).

### §7.5 LEDs — threshold without coherence

Light-emitting diodes have a sharp forward-voltage threshold (~1.7V red, ~3.3V blue/white) below which essentially no current flows. Above threshold, current rises exponentially and photons emit incoherently. **The threshold IS the c→s→r-style regime transition** — below = r-regime (no sustained NESS), at = s-boundary, above = c-regime (sustained current and emission) — *but without the coherence emergence that lasers have at their lasing threshold.* Lasers have the same threshold structure *plus* a coherence symmetry-breaking; LEDs have the threshold without the coherence; plasma/discharge tubes have the threshold plus multi-component nonequilibrium dynamics ("messy"). LEDs are the cleanest substrate-class for testing the regime-structure part of cdv1 *without* the order-parameter-emergence complication.

**Taxonomy insight worth recording:** the c→s→r structure shows up via at least two distinct axes across substrates:
- **Damping-axis substrates** (voice coil actuators, RLC, loudspeakers, tuning forks): c/s/r walks via Q (damping ratio). Drive level just shifts amplitude.
- **Drive-axis substrates** (LEDs, lasers, plasma tubes, semiconductor lasers, neural firing thresholds): c/s/r walks via drive level (voltage / pump / input current relative to threshold). "Damping" is a different parameter and doesn't walk regimes.

Lasers carry *both* axes (cavity Q is one substrate parameter; pump level above lasing threshold is the regime-walk drive). cdv1's universality claim is sharper if it holds across both axis types — and LEDs are the cleanest single-axis drive-substrate to test, with abundant datasheet data (I-V curves, photometric efficiency, thermal characteristics) standardized across the industry.

Data: every LED datasheet has forward voltage, current vs voltage curves, luminous efficacy. Across LED chemistries (red, green, blue, white, IR, UV), threshold varies — multiple "configured instances" of the substrate-class trivially available.

Holds for substrate-N as the drive-axis exemplar. The actuator/RLC/materials chain is all damping-axis; LEDs (then eventually lasers) are the drive-axis arm of the universality test.

## §8 Data acquisition channels (notes for future research)

### §8.1 Chinese manufacturer B2B data

Chinese manufacturers (electronics, MEMS, actuators, motors, sensors, LEDs) routinely publish empirical measurement data directly to wholesale buyers as a form of remote quality control. Substantial raw signal — Q values, settling-time data, step-response oscilloscope screenshots, aging test results, batch-level reliability characterizations — circulates in this ecosystem.

Where it lives:

- Alibaba / 1688 / Made-in-China.com supplier QC report sections.
- Direct OEM B2B channels (buyer-supplier per-shipment test reports, sample-batch characterizations).
- WeChat industry channels (公众号 public accounts, 微信群 trade groups) for verticals like voice coil motors, MEMS, LEDs, haptic LRAs.
- [CNKI (China National Knowledge Infrastructure)](https://www.cnki.net) Chinese-language academic literature — partly indexed in Western databases but mostly Mandarin-only.

Substrates with the richest Chinese manufacturer ecosystems:

- Voice coil actuators / VCMs / LRAs — camera OIS, smartphone haptics (AAC Technologies, Goertek dominate)
- Stepper motors — Leadshine, Wantai
- LEDs — China is the world's largest LED manufacturing base; massive datasheet volume
- Mechanical switches — enormous consumer electronics switch market with detailed bounce-time specs

Practical caveats:

- Mandarin-language access. Multiplies LLM token cost or requires a Chinese-speaking collaborator.
- Methodology variability — measurement standards aren't always declared.
- Fragmentation — scattered across hundreds of supplier portals, not centrally indexed.
- Provenance opacity — hard to verify which standard (if any) was followed.

When to draw on this channel: when Western open-data channels hit a wall on a specific substrate (especially LRAs, OIS actuators, consumer LEDs, custom motors, micro-switches). Outside-model research runs with Mandarin search capability would surface this kind of data more efficiently than English-only searches. Not for immediate use; banked for future-Claude.
