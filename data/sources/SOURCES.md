# Sources

Pointers to substrate-data archives used in this repo. Finding-centric repo, so multiple substrates appear here. Each substrate gets a section.

## §1 Loudspeakers (substrate zero)

### §1.1 Measurement archives

- **ASR (Audio Science Review)** — [audiosciencereview.com](https://www.audiosciencereview.com/forum/index.php?forums/reviews-by-amirm.27/). Thousands of speaker measurements with Klippel NFS: impulse response, CSD waterfall, distortion, frequency response. Free, well-organised, methodologically rigorous. Primary candidate source for substrate-zero canonical speaker.
- **Stereophile measurements archive** — [stereophile.com](https://www.stereophile.com/category/loudspeaker-measurements). Decades of CSD waterfalls, impulse responses, frequency response. John Atkinson's MLSSA-based measurements are the historical reference.
- **AudioXpress / Voice Coil magazine** — DIY-focused measurements, frequently with Klippel data.
- **Klippel R&D** — [klippel.de/r-d](https://www.klippel.de/r-d.html). Large-signal nonlinear measurement; the industry-standard apparatus. Public application notes contain canonical measurement examples.
- **Erin's Audio Corner** — [erinsaudiocorner.com](https://www.erinsaudiocorner.com/). Klippel NFS measurements, similar to ASR. Independent third source.

### §1.2 Substrate-class theory

- **Thiele, A.N. (1971).** "Loudspeakers in Vented Boxes" parts I/II. JAES 19(5/6). Foundational Q_ts decomposition.
- **Small, R.H. (1972–1973).** Vented-box / sealed-box analyses series. JAES.
- **Beranek, L.L. (1954).** *Acoustics.* MIT Press. The reference for electromechanical analogues. Re-issued by AIP.
- **Klippel, W.** *Loudspeaker Nonlinearities — Causes, Parameters, Symptoms.* AES paper series. The large-signal extension of T/S.

### §1.3 Candidate canonical speakers

(To be selected in Phase A step 2.) Selection criterion: published Thiele/Small parameters **plus** independent CSD measurement from at least one of §1.1 archives.

## §2 Engines (substrate one, cited)

See [mpa-engine/data/sources/SOURCES.md](https://github.com/ronviers/mpa-engine/blob/main/data/sources/SOURCES.md). F-001 confirmed at chit_max ≈ 0.41 on the Camry 2.4L 2AZ-FE. Cross-substrate use here is read-only from that record; no new engine data lands in this repo.

## §3 RLC circuits (substrate-two candidate)

Provisional. RLC step-response is in every undergraduate electrical engineering text. No archive needed — measurements or SPICE simulations are reproducible from first principles. Selection deferred until substrate zero lands.

## §4 Adjacent literature (cross-substrate framing)

- The engine-transient research dump from mpa-engine ([Engine Transient Data Research Sources](https://github.com/ronviers/mpa-engine/blob/main/data/sources/Engine%20Transient%20Data%20Research%20Sources.md)) frames IC engines as canonical multi-timescale dissipators where the natural physical decay tail is slower-than-exponential, but is partly erased by ECU dashpot algorithms. That framing motivates the substrate-pivot: loudspeakers don't have an "ECU" overlaying engineered exponential decay, so the natural physical c→s→r structure shows up cleaner.
