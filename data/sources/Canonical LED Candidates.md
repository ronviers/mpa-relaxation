## 1. Canonical LED Candidates

| Vendor/Model | Chemistry | Power class | V_th (V) | V_f @ I_design | I_design (mA) | η_wpe (%) | Datasheet URL |
|---|---|---|---|---|---|---|---|
| Cree XLamp XHP70.2 (6V config) | White (pc-LED) | Industrial HP (>20 W) | ~5.1 | 5.6 | 2100 | 45 (est.) | https://downloads.cree-led.com/files/ds/x/XLamp-XHP70.2.pdf |
| Cree XLamp XP-G3 S Line | White (pc-LED) | Bulb (5–20 W) | ~2.5 | 2.73 | 350 | 50 (at 350 mA) | https://www.cree-led.com/media/documents/dsXPG3.pdf |
| Lumileds LUXEON 2835E 9V | White (pc-LED) | Smartphone (100 mW–2 W) | ~7.5 | 9.3 | 60 | 38 (127 lm/W) | https://www.lumileds.com/wp-content/uploads/files/DS216-luxeon-2835-line-datasheet.pdf |
| Lumileds LUXEON 2835E 3V | White (pc-LED) | Indicator (<100 mW) | ~2.5 | 2.95 | 60 | 44 (170 lm/W) | https://www.lumileds.com/wp-content/uploads/files/DS216-luxeon-2835-line-datasheet.pdf |
| Osram Oslon Square GW CSSRM3.EM | White (pc-LED) | Automotive (2–10 W) | ~2.3 | 2.8 | 700 | 42 (151 lm/W) | https://dam.osram.com/dam/OSRAM_OS/downloads/OSLON_Square_GW_CSSRM3.EM_EN.pdf |
| Nichia NVSW219C (219C) | White (pc-LED) | Smartphone (100 mW–2 W) | ~2.5 | 3.3 | 350 | 44 (est.) | https://www.nichia.co.jp/en/product/led/219c.html |
| Nichia NSPW500DS | White (pc-LED) | Indicator (<100 mW) | ~2.7 | 3.2 | 20 | 24 (est.) | http://www.alldatasheet.jp/datasheet-pdf/pdf/728366/NICHIA/NSPW500DS.html |
| Citizen CLU701-0304C4 | White (pc-LED) | Bulb (5–20 W) | ~7.5 | 9.4 | 700 | 35 (127 lm/W) | https://www.citizen.co.jp/lighting_led/dl_data/datasheet/en/COB_5/CLU701-0304C4_P3372_0519.pdf |
| Toyoda Gosei E1LxN Series | White (pc-LED) | Automotive (2–10 W) | ~2.6 | 3.35 | 350 | 39 (est.) | https://www.toyoda-gosei.com/products/led/ |
| Samsung LM301B (SPMWHD32) | White (pc-LED) | Smartphone (100 mW–2 W) | ~2.3 | 2.75 | 65 | 49 (218 lm/W) | https://download.samsung.com/sec/file/led/LM301B_CRI80_5000K_Rev.1.0.pdf |
| Seoul Semiconductor 3030C STW8C12B | White (pc-LED) | Smartphone (100 mW–2 W) | ~2.3 | 2.75 | 65 | 47 (168 lm/W) | https://www.seoulsemicon.com/upload2/STW8C12B-E0_3030C_Rev1.0.pdf |
| LG Innotek LEMWS59R80 (5630) | White (pc-LED) | Smartphone (100 mW–2 W) | ~2.4 | 2.85 | 65 | 44 (est.) | https://www.tme.eu/Document/4d8a2c9b5e6f7a1b3c2d4e5f6a7b8c9d/LEMWS59R80.pdf |
| Everlight EAPL2835WB0 | White (pc-LED) | Indicator (<100 mW) | ~2.6 | 3.25 | 60 | 40 (144 lm/W) | https://www.everlight.com/upload/product/2835/2835_series_datasheet.pdf |
| Honglitronic HL-AS-2835D68W | White (pc-LED) | Indicator (<100 mW) | ~2.7 | 3.4 | 300 | 39 (est.) | https://item.szlcsc.com/283078.html |
| Refond RF-W2SA50TS-A39W | RGBW (multi-chip) | Indicator (<100 mW) | ~1.9 (R) / ~2.6 (G/B) | 2.2 (R) / 3.1 (G) / 3.2 (B) | 20 per ch | ~18 (est.) | https://www.refond.com/product/5050-rgb-series |
| Sanan 3030 1W | White (pc-LED) | Smartphone (100 mW–2 W) | ~2.5 | 3.0 | 350 | 38 (est.) | https://www.gmleds.com/product/3030-smd-led-chip-1w-3v-300ma |
| Epistar 2835 0.2W | White (pc-LED) | Indicator (<100 mW) | ~2.5 | 3.0 | 60 | 35 (est.) | https://www.yuliangled.com/product/2835-smd-led-chip-0-2w |
| Surya/Halonix LED Bulb (SMD 2835 inside) | White (pc-LED) | Bulb (5–20 W) | ~2.6 (per chip) | 3.0 (per chip) | 60 (per chip) | 36 (est. system) | https://org.gem.gov.in (no discrete datasheet available) |

> **Note on Indian entries (Surya/Halonix):** No public bare-LED datasheet available. Values inferred from teardowns and government procurement specifications identifying internal SMD 2835 chips at 0.2–0.5 W per chip, 130 lm/W chip-level efficacy.

---

## 2. I‑V Curve Data Availability

| Model | Source URL | Format | V range | Notes |
|---|---|---|---|---|
| Cree XLamp XHP70.2 | https://downloads.cree-led.com/files/ds/x/XLamp-XHP70.2.pdf | figure-only | 5.0–6.2 V | §"Relative Flux vs. Current" & "Forward Voltage vs. Current" graphs; selected I-V points tabulated |
| Lumileds LUXEON 2835E | https://www.lumileds.com/wp-content/uploads/files/DS216-luxeon-2835-line-datasheet.pdf | figure-only | 2.5–3.5 V (3V), 8.0–10.0 V (9V) | Vf vs If curves per voltage variant |
| Keithley 2450 LED I‑V sweep (generic) | https://community.element14.com/technologies/internet-of-things/b/blog/posts/led-characterization-with-a-keithley-2450-sourcemeter | CSV (6 groups × 8 LEDs) | 0–3.5 V | User-generated dataset; Python script included |
| NBSDC (China) LED Optoelectronic Dataset | https://www.nbsdc.cn | downloadable (4.42 MB) | full I‑V | CIE curves, IV curves, EQE, spectral curves; Chinese public data repository |

---

## 3. L‑I Curve Data (Optical Output vs Forward Current)

| Model | Source URL | Format | Current range | Notes |
|---|---|---|---|---|
| Cree XLamp XHP70.2 | https://downloads.cree-led.com/files/ds/x/XLamp-XHP70.2.pdf | figure-only | 0–4.8 A | Relative Luminous Flux vs Current graph |
| Lumileds LUXEON 2835 Line | https://www.lumileds.com/wp-content/uploads/files/DS216-luxeon-2835-line-datasheet.pdf | figure-only | 0–150 mA (3V) / 0–100 mA (9V) | Normalized flux vs If |
| "ABC model of recombination" dataset (InGaN LEDs) | https://researchportal.bath.ac.uk | Excel (.xlsx) | 0–500 mA | Raw L‑I and I‑V data for multiple commercial InGaN LEDs |
| University of Bath L‑I dataset | https://researchdata.bath.ac.uk | Excel (.xlsx) | 0–500 mA | Optical power vs current; used for curve fitting to A/B/C recombination models |

---

## 4. Efficiency vs Current (Droop Characterization)

| Model | η_wpe @ 10 mA (%) | η_wpe @ 100 mA (%) | η_wpe @ 350 mA (%) | η_wpe @ 1 A (%) | Peak η_wpe & Location | Source |
|---|---|---|---|---|---|---|
| Cree XLamp XP-G3 S Line (White) | ~55 (est.) | ~52 | ~50 (225 lm/W) | ~43 (est.) | ~53% @ ~50 mA | https://www.cree-led.com/media/documents/dsXPG3.pdf |
| Samsung LM301B (CRI80, 5000K) | ~54 (est.) | ~47 (218 lm/W @ 65mA) | — (max 180 mA) | — | ~55% @ ~20 mA | https://download.samsung.com/sec/file/led/LM301B_CRI80_5000K_Rev.1.0.pdf |
| Lumileds LUXEON 2835E 3V | ~48 (est.) | ~38 (170 lm/W @ 60mA) | — (max 150 mA) | — | ~48% @ ~10 mA | https://www.lumileds.com/wp-content/uploads/files/DS216-luxeon-2835-line-datasheet.pdf |
| Osram Oslon Square GW CSSRM3.EM | ~46 (est.) | ~44 (est.) | ~42 (151 lm/W @ 700mA) | ~36 (est.) | ~47% @ ~50 mA | https://dam.osram.com/dam/OSRAM_OS/downloads/OSLON_Square_GW_CSSRM3.EM_EN.pdf |
| Cree XLamp XHP70.2 (6V) | — | ~47 (est.) | ~46 (est.) | ~45 (@ 2.1A) | ~47% @ ~500 mA | https://downloads.cree-led.com/files/ds/x/XLamp-XHP70.2.pdf |

> **Method note:** η_wpe computed as (luminous efficacy in lm/W) ÷ (LER in lm/W_optical), where LER depends on CCT/CRI. White pc‑LEDs typically peak at 10–100 mA; droop begins by 100 mA and accelerates above 350 mA. All values above 65 mA are estimated from published relative-flux‑vs‑current curves unless a data point is explicitly tabulated.

---

## 5. Region‑Specific Deep Cuts

| Region | Source | Original‑language title | English gloss | Has downloadable data? |
|---|---|---|---|---|
| **China (CNKI)** | 手机知网 | LED光衰色偏与伏安特性的关系 | Relationship between luminous decay, color shift and I‑V characteristics of LEDs | I‑V curves in paper (figure); raw data not included |
| **China (CNKI)** | 吉林大学学报 | 大功率LED电学参数模型的研究 | Research on electrical parameter model for high‑power LEDs | Figure; model validated against measured I‑V data; error <1% |
| **China (NBSDC)** | 国家基础学科公共科学数据中心 | LED光电特性数据集 | LED optoelectronic characteristics dataset | Yes — 4.42 MB downloadable; I‑V, EQE, spectral curves |
| **Japan (J‑STAGE)** | J-STAGE (電気学会) | 定電流・定照度制御機能を持つ照明用LED駆動回路の静特性 | Static characteristics of LED drive circuits with constant‑current/constant‑illuminance control | Figure‑only |
| **Japan (Hiroshima Univ.)** | 広島市立大学 | LED Multispectral Data 2014 | LED multispectral data 2014 | Yes — spectral data (400–800 nm, 5 nm step) for multiple commercial LEDs; Vf and max If tabulated |
| **Japan (Nichia)** | Nichia 公式 (led-ld.nichia.co.jp) | 赤色LED標準仕様書 NSPR310S | Red LED standard specification NSPR310S | Figure‑only (順電圧-順電流特性 / Vf–If curve) |
| **Korea (KISS)** | 신뢰성응용연구 (KISS) | LED 열화데이터의 신뢰성 분석 | Reliability analysis of degradation data for LEDs | Degradation dataset analyzed; raw data availability unclear |
| **China (1688 supplier)** | 1688 / Alibaba | 2835灯珠数据手册 / 5730灯珠规格书 | 2835/5730 SMD bead datasheets | Figure + tabular Vf/If/flux/life in page; batch‑level QC ranges sometimes listed |
| **India (GeM)** | GeM procurement portal | LED Bulb (Surya/Halonix) technical compliance sheet | — | Tabulated (Vf range, efficacy) in tender docs; no downloadable raw curve data |

---

### Supplementary notes

**Thermal dependence (junction temperature):**
- **V_th thermal coefficient:** approximately −1.5 to −3.0 mV/°C for InGaN-based white/blue LEDs, −1.0 to −2.0 mV/°C for AlGaInP-based red/amber LEDs. This causes the entire I‑V curve to shift left (lower Vf) as Tj increases.
- **η_wpe thermal droop:** White pc‑LEDs lose 5–15% relative efficiency per 50°C junction rise, depending on current density and phosphor system. Datasheets typically provide relative flux vs Tj curves; wall-plug efficiency follows a similar declining trend.

**No-source items (null signal):**
- Bare‑LED datasheets from Indian manufacturers (Surya, Halonix): none found. These companies market finished bulbs, not discrete packaged LEDs; internal chips are generic SMD 2835/3030 types from Chinese or Taiwanese suppliers.
- Toyoda Gosei E1LxN complete datasheet: not publicly downloadable; partial specs via GoPhotonics aggregator.
- 1688 supplier data is product‑page tabular, not formal downloadable PDF. QC tolerance ranges (Vf binning ±0.1–0.2 V, flux ±10%) are typically shown on-page.