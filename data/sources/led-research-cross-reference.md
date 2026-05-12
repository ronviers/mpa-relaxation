# LED research — cross-reference (2026-05-12)

Distilled signal from three outside-model research runs against the LED-targeted prompt with explicit regional/language casting. Source files preserved for audit:

- [LED candidates.md](LED%20candidates.md) — File A. Most populated table; 24 LEDs with full V_th/V_f/I_design/η_wpe.
- [Canonical LED Candidates.md](Canonical%20LED%20Candidates.md) — File B. 19 LEDs + supplementary thermal-coefficient and droop notes. Best downloadable-dataset signal.
- [LED Characterization Data Request.md](LED%20Characterization%20Data%20Request.md) — File C. Broader regional coverage but many "no source" entries. Cleaned in-place (~13 KB of PNG-rendered symbols stripped).

## Convergence pattern

Materially better than the earlier actuator and loudspeaker rounds. Three reasons: (1) explicit regional casting in the prompt surfaced Chinese/Japanese/Korean entries each model wouldn't have found alone; (2) LED datasheet content is heavily standardized; (3) η_wpe and V_th are well-defined observables across all vendors.

| Cross-source agreement | Models converged on |
|---|---|
| Samsung LM301B as canonical mid-power smartphone white LED | A + B + C (all three) |
| Lumileds LUXEON 2835 series | A + B + C |
| Nichia mid-power white LEDs (NVSW219C variants, NFSW757H-V1) | A + B + C |
| Honglitronic 2835 series (Chinese) | A + B + C |
| Seoul Semiconductor WICOP / 3030C | A + B + C |
| LG Innotek LEMWS59R | A + B |
| Cree XLamp XP-G3 / XHP70.2 | A + B |
| Refond 2835 / RGB variants | A + B + C |
| Citizen CL-L251-C4N / CLU048-1212C4 | A + C |

**Disagreement on Samsung LM301B η_wpe:** File A reports ~65%, File B reports 49% (218 lm/W), File C reports ~67%. The 49% number from File B is a stricter calculation (lm/W ÷ luminous efficacy of radiation, ~440 lm/W for ~80 CRI white). The 65–67% numbers conflate luminous efficacy with wall-plug efficiency. Real white-LED η_wpe at peak: typically 40–55% for premium parts at 2026 state-of-art. We use 0.50 for LM301B in our data file with this caveat noted.

## High-leverage downloadable datasets surfaced

**Promising, pending verification:**

| Dataset | Source | Format | Why high-leverage |
|---|---|---|---|
| **NBSDC LED Optoelectronic Characteristics** | [nbsdc.cn](https://www.nbsdc.cn) (China National Basic Science Data Center) | 4.42 MB downloadable | Full I-V curves, CIE, EQE, spectral curves. Public Chinese repository. If real, this is the gold standard. |
| **University of Bath ABC-recombination dataset** | [researchdata.bath.ac.uk](https://researchdata.bath.ac.uk) | Excel (.xlsx) | Raw L-I and I-V data for multiple commercial InGaN LEDs across 0–500 mA. Used for ABC recombination model curve-fitting — this is *directly* the substrate-conditional content for drive-axis F-003. |
| **Keithley 2450 community LED I-V sweep** | [community.element14.com](https://community.element14.com/technologies/internet-of-things/b/blog/posts/led-characterization-with-a-keithley-2450-sourcemeter) | CSV (6 groups × 8 LEDs) | User-generated dataset, 0–3.5 V, with Python sweep script. Low-volume but verified format. |
| **Hiroshima University LED Multispectral 2014** | 広島市立大学 | Spectral data | 400–800 nm at 5 nm step for multiple commercial LEDs + tabulated Vf and max If. |
| **Tunable-White-LED MATLAB** | [github.com/jaakkopasanen/Tunable-White-LED](https://github.com/jaakkopasanen/Tunable-White-LED) | MATLAB | Generic empirical I-V/L-I scaling coefficient matrices. Useful as a synthesis/calibration baseline. |

## Drive-axis F-003 hypothesis (sharpened by this research)

The original Phase F.1 driver profile flagged drive-axis F-003 as an OPEN research question, with the s-region "smeared" by thermal noise kT/q. The research returned **two complementary phenomena that may both be the drive-axis F-003 signature**:

1. **V_th threshold itself, smeared by kT/q.** Sub-threshold leakage (Shockley-Read-Hall recombination) vs. exponential turn-on at V ≈ V_th. The transition zone is ~kT/q wide. This is the *static-I-V* read.

2. **η_wpe efficiency droop with peak structure.** The ABC recombination model: R = A·n + B·n² + C·n³ where A is SRH, B is radiative, C is Auger. η_wpe peaks at intermediate carrier density where B·n²/(A·n + B·n² + C·n³) is maximized. **The peak position and curvature are the substrate-conditional drive-axis signatures** — analogous to RLC's algebraic-exp factor at Q = 0.5 being the damping-axis signature.

The Bath ABC-recombination dataset is the most direct path to test hypothesis (2): published Excel data of L-I curves with already-validated A-B-C fits. We can compute the efficiency droop curvature at the peak across multiple commercial LEDs and look for substrate-class universality.

## Region-specific deep cuts (catalog)

Each file surfaced different regional sources. Aggregate list for future verification:

**Chinese (CNKI / 1688 / NBSDC):**
- 微纳电子技术 — ICP etching effect on GaN LED I-V (Figure-only)
- 中国照明电器 — High-power LED current aging characteristics (PDF with data tables)
- 硅酸盐学报 — UV photodetector with LED source I-V (Figure-only)
- 吉林大学学报 — High-power LED electrical parameter model (Figure, <1% error validated)
- 国家基础学科公共科学数据中心 (NBSDC) — LED optoelectronic characteristics dataset (4.42 MB, downloadable)
- 1688 supplier portals — 2835/5730 SMD bead datasheets with batch QC tolerances
- Refond / Honglitronic test reports — vendor PDFs with batch-level data

**Japanese (J-STAGE):**
- レーザー研究 39(8) — Ultra-compact LED lidar pulse I-V characterization
- 応用物理 85(11) — LED optical evaluation methodology, WPE vs current
- 映像情報メディア学会誌 — Near-UV LED applications, efficiency vs injection current
- 電気学会 — LED drive circuit static characteristics
- 広島市立大学 — LED Multispectral Data 2014 (Vf and max If tabulated)

**Korean (KISS):**
- 신뢰성응용연구 — LED degradation data reliability analysis
- Samsung LED datasheet portal — LM301B/LM301H EVO
- LG Innotek LED catalog — LEMWS59R series
- Seoul Semiconductor — WICOP automotive

**Indian:**
- GeM procurement portal — LED bulb technical compliance sheets (Vf range + efficacy, no raw curves)
- Surya / Halonix — finished bulbs only; no bare-LED datasheets publicly available

## Recommendation for Phase F.1 step-2 (this turn)

1. **Populate `data/leds.json` with 13 cross-referenced candidates** spanning chemistries (white, blue, red, UV, RGB), power classes (indicator through industrial), and regions (Western, Japanese, Chinese, Korean, Taiwan).
2. **Run F-001-led test.** Compute chit_max bounds across substrate-class. Predicted: 0.08 (low-efficiency UV) to 0.69 (high-efficiency Samsung LM301B). Test substrate-class fingerprint.
3. **Flag drive-axis F-003 hypothesis (ABC-recombination droop curvature).** Defer the actual fit to next turn pending NBSDC or Bath dataset verification.
4. **Strip image bloat from File C.** Done.
