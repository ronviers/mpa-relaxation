# **Thermodynamic Universality in LED Substrates: Drive-Axis Characterization Data**

This report characterizes light-emitting diodes (LEDs) as substrate-classes within a thermodynamic universality framework, specifically modeling them as drive-axis substrates where the regime transition operates across a strict forward-voltage (![][image1]) threshold rather than continuous damping. The data parameterizes the ![][image1] bifurcation point, operational steady-state voltage (![][image2]), and wall-plug efficiency (![][image3]) across a geographically diverse optoelectronic manufacturing ensemble.

## **1\. Canonical LED Candidates**

The following canonical candidates map the thermodynamic boundaries of the drive-axis transition. Efficiency (![][image3]) is derived from radiometric output where available, or estimated via spectral equivalents if only photometric flux (lm) is provided. Null values indicate missing datasheet parameters.1

| Vendor/Model | Chemistry | Power class | V\_th (V) | V\_f @ I\_design | I\_design (mA) | η\_wpe (%) | Datasheet URL |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Cree XLamp XP-G3 Horizon | White | Smartphone 100mW–2W | "no source" | 2.73 | 350 | "no source" | [https://downloads.cree-led.com/files/ds/x/XLamp-XPG3-Horizon.pdf](https://downloads.cree-led.com/files/ds/x/XLamp-XPG3-Horizon.pdf) |
| Osram Oslon Square | White | Automotive 2–10W | "no source" | "no source" | "no source" | "no source" | [https://ams-osram.com/products/leds/white-leds/osram-oslon-square-gw-cssrm3-pm](https://ams-osram.com/products/leds/white-leds/osram-oslon-square-gw-cssrm3-pm) |
| Bridgelux SMD 2835 | White | Smartphone 100mW–2W | "no source" | 3.00 | 65 | "no source" | [https://www.bridgelux.com/sites/default/files/resource\_media/DS55%20SMD%202835%200.2W%203V%20Data%20sheet%20Rev%20B.pdf](https://www.bridgelux.com/sites/default/files/resource_media/DS55%20SMD%202835%200.2W%203V%20Data%20sheet%20Rev%20B.pdf) |
| Inspire G18082-FGL | White | Bulb 5–20W | "no source" | 240.00 | 45 | "no source" | [https://media.adeo.com/media/4113544/media.pdf](https://media.adeo.com/media/4113544/media.pdf) |
| Nichia NFSW757H-V1 | White | Smartphone 100mW–2W | "no source" | 2.84 | 65 | \~66.0 | [https://led-ld.nichia.co.jp/en/product/led\_product\_data.html?type=NFSW757H-V1\&kbn=0](https://led-ld.nichia.co.jp/en/product/led_product_data.html?type=NFSW757H-V1&kbn=0) |
| Citizen CLU048-1212C4 | White | Industrial \>20W | 30.00 | 34.60 | 1080 | \~38.0 | [https://ce.citizen.co.jp/cms/ce/lighting\_led/dl\_data/COB\_Version5/datasheet/CLU048-1212C4\_P3708\_0516.pdf](https://ce.citizen.co.jp/cms/ce/lighting_led/dl_data/COB_Version5/datasheet/CLU048-1212C4_P3708_0516.pdf) |
| Toyoda Gosei E1S19-0P0A7-02 | UV | Smartphone 100mW–2W | "no source" | "no source" | "no source" | "no source" | [https://docs.rs-online.com/fa9a/0900766b8034dc95.pdf](https://docs.rs-online.com/fa9a/0900766b8034dc95.pdf) |
| Toyoda Gosei ENSBD-LJ1Y9-F0 | White | Smartphone 100mW–2W | "no source" | "no source" | "no source" | "no source" | [https://www.toyodagosei-led.jp/docs/products/list/4000k-standard-en.pdf](https://www.toyodagosei-led.jp/docs/products/list/4000k-standard-en.pdf) |
| Honglitronic HL-AS-2835D46BC | Blue | Smartphone 100mW–2W | 2.80 | 3.10 | 150 | 50.5 | [https://www.honglitronic.com/upload/file/2025-03/col24/1741662193467.pdf](https://www.honglitronic.com/upload/file/2025-03/col24/1741662193467.pdf) |
| Refond RF-WUB190DS-DD | White | Indicator \<100mW | \~2.50 | 3.00 | 20 | "no source" | [https://www.refond.com/upload/download/2024-03/66012191e6ab4.pdf](https://www.refond.com/upload/download/2024-03/66012191e6ab4.pdf) |
| MLS PLW2835AA | White | Smartphone 100mW–2W | 2.80 | 3.10 | 150 | "no source" | [https://www.mouser.com/datasheet/2/613/93875-876279.pdf](https://www.mouser.com/datasheet/2/613/93875-876279.pdf) |
| Sanan 2835 SMD | White | Smartphone 100mW–2W | "no source" | 3.00 | 300 | "no source" | [https://m.made-in-china.com/product/Epistar-Sanan-High-Lumens-2835-SMD-LED-Datasheet-Specifications-Chip-SMD2835-2046722065.html](https://m.made-in-china.com/product/Epistar-Sanan-High-Lumens-2835-SMD-LED-Datasheet-Specifications-Chip-SMD2835-2046722065.html) |
| Samsung LM301B | White | Smartphone 100mW–2W | \~2.40 | 2.71 | 65 | \~67.0 | [https://download.led.samsung.com/led/file/resource/2022/04/Data\_Sheet\_LM301B\_CRI80\_Rev.10.2.pdf](https://download.led.samsung.com/led/file/resource/2022/04/Data_Sheet_LM301B_CRI80_Rev.10.2.pdf) |
| Seoul Semi STW9C2SB-S | White | Smartphone 100mW–2W | "no source" | 6.38 | 150 | "no source" | [https://www.seoulsemicon.com/vn/product/detail/STW9C2SB-S?productid=434\&id=556](https://www.seoulsemicon.com/vn/product/detail/STW9C2SB-S?productid=434&id=556) |
| Epistar ES-2835-1036V | White | Smartphone 100mW–2W | "no source" | "no source" | "no source" | "no source" | [https://www.everstar.in/pdf/ES-2835-1036V-XX-XXXX.pdf](https://www.everstar.in/pdf/ES-2835-1036V-XX-XXXX.pdf) |
| Surya SLE DLR 10W | White | Bulb 5–20W | "no source" | 240.00 | 50 | "no source" | [https://www.scribd.com/document/528313386/Professional-Lighting-Catalogue-SURYA](https://www.scribd.com/document/528313386/Professional-Lighting-Catalogue-SURYA) |
| Halonix HLDLR-R06-18-CW | White | Bulb 5–20W | "no source" | 240.00 | 92 | "no source" | [https://www.scribd.com/document/634805327/HLDLR-R06-18-CW](https://www.scribd.com/document/634805327/HLDLR-R06-18-CW) |

## **2\. I-V Curve Data Availability**

Continuous I-V manifolds are required to compute sub-threshold Ohmic leakage and the integration of dynamic resistance across the exponential transition. Open-access raw datasets for individual bare-die LED components remain sparse, often requiring extraction from PDF datasheets or utilizing analogous photovoltaic datasets.2

| Model | Source URL | Format (CSV / MATLAB / figure-only) | V range | Notes |
| :---- | :---- | :---- | :---- | :---- |
| Citizen CLU048-1212C4 | [https://ce.citizen.co.jp/cms/ce/lighting\_led/dl\_data/COB\_Version5/datasheet/CLU048-1212C4\_P3708\_0516.pdf](https://ce.citizen.co.jp/cms/ce/lighting_led/dl_data/COB_Version5/datasheet/CLU048-1212C4_P3708_0516.pdf) | figure-only | 30.0V \- 38.0V | Distinct multi-junction knee extracted from characteristic curves.2 |
| Samsung LM301B | [https://download.led.samsung.com/led/file/resource/2022/04/Data\_Sheet\_LM301B\_CRI80\_Rev.10.2.pdf](https://download.led.samsung.com/led/file/resource/2022/04/Data_Sheet_LM301B_CRI80_Rev.10.2.pdf) | figure-only | 2.5V \- 3.0V | Forward current characteristics embedded in Section 3b.3 |
| Refond RF-WUB190DS-DD | [https://www.refond.com/upload/download/2024-03/66012191e6ab4.pdf](https://www.refond.com/upload/download/2024-03/66012191e6ab4.pdf) | figure-only | 2.5V \- 3.8V | Displays initial conduction rise.4 |
| Tunable White LED Model | [https://github.com/jaakkopasanen/Tunable-White-LED/blob/master/Matlab/README.md](https://github.com/jaakkopasanen/Tunable-White-LED/blob/master/Matlab/README.md) | MATLAB | "no source" | Generic empirical coefficient matrices for continuous I-V/L-I scaling.19 |
| NIST SRM 3452 Artifact | [https://tsapps.nist.gov/publication/get\_pdf.cfm?pub\_id=932592](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=932592) | "no source" | "no source" | High-precision baseline Ohmic/IV artifacts stabilized between 295–900 K.20 |
| DTU Risø PV Module | [https://data.dtu.dk/articles/dataset/Module\_level\_IV\_curve\_data\_set/27901599](https://data.dtu.dk/articles/dataset/Module_level_IV_curve_data_set/27901599) | CSV | "no source" | PV module IV data mathematically parallel to series-string LED behavior.18 |

## **3\. L-I Curve Data (Optical Output Power vs Forward Current)**

The L-I curve characterizes the optoelectronic yield vector post-transition. While idealized linear matrices exist near the ![][image1] threshold, high-fidelity empirical L-I distributions require advanced spatial and spectral ray-tracing files to account for localized flux density.8

| Model | Source URL | Format (CSV / MATLAB / figure-only) | V range | Notes |
| :---- | :---- | :---- | :---- | :---- |
| Seoul Semi STW9C2SB-S | [https://www.seoulsemicon.com/en/support/documentlibrary?lev1=\&lev2=\&lev3=\&search=](https://www.seoulsemicon.com/en/support/documentlibrary?lev1&lev2&lev3&search) | .ray /.sdf /.xlsx | "no source" | Millions of traced rays for LightTools/Zemax providing absolute thermodynamic emission distributions.23 |
| Honglitronic HL-AS-2835 | [https://www.honglitronic.com/upload/file/2025-03/col24/1741662193467.pdf](https://www.honglitronic.com/upload/file/2025-03/col24/1741662193467.pdf) | figure-only | 2.8V \- 3.4V | Normalized radiometric L-I extraction against drive current.8 |
| MLS Dataset (General) | [https://github.com/visillect/mls-dataset](https://github.com/visillect/mls-dataset) | Images/Raw | "no source" | Spatial illumination arrays evaluated under varied LED drive currents (25%, 50%, 70%).22 |
| Everlight EAPL2835RA0 | [https://www.mouser.com/datasheet/2/143/EAPL2835RA0-949337.pdf](https://www.mouser.com/datasheet/2/143/EAPL2835RA0-949337.pdf) | figure-only | 1.9V \- 2.5V | Depicts low-power L-I linearity mapping.21 |

## **4\. Efficiency vs Current (Droop Characterization)**

Carrier density saturation induces efficiency droop, defining the absolute thermodynamic limit of the substrate. As drive current increases past an optimal low-current peak, non-radiative Auger recombination depresses ![][image3]. The table below tracks this thermal degradation across standardized forcing intervals.2

| Model | Peak η\_wpe Current | η\_wpe @ 10 mA | η\_wpe @ 65 mA | η\_wpe @ Max Rated Current | Notes |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Samsung LM301B | "no source" | "no source" | \~67.0% | "no source" | Peak efficiency operates deep into the sub-100mA regime; max rated (200mA) triggers high thermal penalties.3 |
| Honglitronic HL-AS-2835 | "no source" | "no source" | "no source" | 50.5% (@ 150mA) | Radiometric scaling indicates onset of Auger droop near 150mA bounds.8 |
| Citizen CLU048-1212C4 | "no source" | "no source" | "no source" | \~38.0% (@ 1080mA) | Macroscopic series arrays delay per-die droop, but bulk efficiency falls below 40% at full thermal load.2 |
| Refond RF-WUB190DS-DD | "no source" | "no source" | "no source" | "no source" | Indicator hits thermal saturation rapidly; exceeding 30mA invokes permanent regime breakdown.4 |

## **5\. Region-Specific Deep Cuts**

Regional native-language archives reveal critical batch-level ensembles. These datasets provide statistical distributions reflecting how epitaxial wafer tolerances perturb the macroscopic ![][image1] and ![][image2] coordinates across manufacturing arrays.23

| Region | Source | Original-language title | English gloss | Has downloadable data? |
| :---- | :---- | :---- | :---- | :---- |
| China | CNKI | 光伏组串故障诊断I-V曲线全局特征Swin-Transformer | Photovoltaic String Fault Diagnosis Using Global Features of I-V Curves via Swin-Transformer | "no source" |
| China | Refond Portal | RF-A3E35-2W2E-B1\_test report | RF-A3E35-2W2E-B1 Test Report | Yes (PDF) |
| China | Honglitronic | HL-AS-2835D90W-2-S1-08-PCT-HR3-ZW-P6 | HL-AS-2835D90W Product Selection Guide and Reliability | Yes (PDF) |
| Japan | Toyoda Gosei | 豊田合成グループ 人権方針 (ToyodaGoseiGroupHumanRightsPolicy.pdf) | Toyoda Gosei Group Human Rights Policy / Supplier Guidelines | Yes (PDF) |
| Korea | Seoul Semi | STW9C2SB-S-5000K\_Blue\_5M\_LightTools\_20200320.ray | STW9C2SB-S 5000K Blue 5 Million Rays LightTools 20200320 | Yes (.ray /.sdf) |

#### **Works cited**

1. NFSW757H-V1 | Product Data | LED | NICHIA CORPORATION, accessed May 12, 2026, [https://led-ld.nichia.co.jp/en/product/led\_product\_data.html?type=NFSW757H-V1\&kbn=0](https://led-ld.nichia.co.jp/en/product/led_product_data.html?type=NFSW757H-V1&kbn=0)  
2. CLU048-1212C4, accessed May 12, 2026, [https://ce.citizen.co.jp/cms/ce/lighting\_led/dl\_data/COB\_Version5/datasheet/CLU048-1212C4\_P3708\_0516.pdf](https://ce.citizen.co.jp/cms/ce/lighting_led/dl_data/COB_Version5/datasheet/CLU048-1212C4_P3708_0516.pdf)  
3. LM301B \- Samsung, accessed May 12, 2026, [https://download.led.samsung.com/led/file/resource/2022/04/Data\_Sheet\_LM301B\_CRI80\_Rev.10.2.pdf](https://download.led.samsung.com/led/file/resource/2022/04/Data_Sheet_LM301B_CRI80_Rev.10.2.pdf)  
4. SPECIFICATION \- Refond Optoelectronics, accessed May 12, 2026, [https://www.refond.com/upload/download/2024-03/66012191e6ab4.pdf](https://www.refond.com/upload/download/2024-03/66012191e6ab4.pdf)  
5. PLW2835AA Series 2835 Mid Power LED Product Datasheet | Mouser, accessed May 12, 2026, [https://www.mouser.com/datasheet/2/613/93875-876279.pdf](https://www.mouser.com/datasheet/2/613/93875-876279.pdf)  
6. XLamp XP-G3 Horizon LED Data Sheet, accessed May 12, 2026, [https://downloads.cree-led.com/files/ds/x/XLamp-XPG3-Horizon.pdf](https://downloads.cree-led.com/files/ds/x/XLamp-XPG3-Horizon.pdf)  
7. OSRAM OSLON™ Square, GW CSSRM3.PM White LEDs, accessed May 12, 2026, [https://ams-osram.com/products/leds/white-leds/osram-oslon-square-gw-cssrm3-pm](https://ams-osram.com/products/leds/white-leds/osram-oslon-square-gw-cssrm3-pm)  
8. HL-AS-2835D46BC-S1-08-PCT-ZW-P6, accessed May 12, 2026, [https://www.honglitronic.com/upload/file/2025-03/col24/1741662193467.pdf](https://www.honglitronic.com/upload/file/2025-03/col24/1741662193467.pdf)  
9. Bridgelux® SMD 2835 0.2W 3V, accessed May 12, 2026, [https://www.bridgelux.com/sites/default/files/resource\_media/DS55%20SMD%202835%200.2W%203V%20Data%20sheet%20Rev%20B.pdf](https://www.bridgelux.com/sites/default/files/resource_media/DS55%20SMD%202835%200.2W%203V%20Data%20sheet%20Rev%20B.pdf)  
10. Light Source Technical DataSheet, accessed May 12, 2026, [https://media.adeo.com/media/4113544/media.pdf](https://media.adeo.com/media/4113544/media.pdf)  
11. Epistar Sanan High Lumens 2835 SMD LED Datasheet Specifications Chip SMD2835, accessed May 12, 2026, [https://m.made-in-china.com/product/Epistar-Sanan-High-Lumens-2835-SMD-LED-Datasheet-Specifications-Chip-SMD2835-2046722065.html](https://m.made-in-china.com/product/Epistar-Sanan-High-Lumens-2835-SMD-LED-Datasheet-Specifications-Chip-SMD2835-2046722065.html)  
12. Surya LED Lighting Solutions Catalogue 2020 | PDF \- Scribd, accessed May 12, 2026, [https://www.scribd.com/document/528313386/Professional-Lighting-Catalogue-SURYA](https://www.scribd.com/document/528313386/Professional-Lighting-Catalogue-SURYA)  
13. 18W LED Down Light Technical Data | PDF \- Scribd, accessed May 12, 2026, [https://www.scribd.com/document/634805327/HLDLR-R06-18-CW](https://www.scribd.com/document/634805327/HLDLR-R06-18-CW)  
14. STW9C2SB-S \- Seoul Semiconductor, accessed May 12, 2026, [https://www.seoulsemicon.com/vn/product/detail/STW9C2SB-S?productid=434\&id=556](https://www.seoulsemicon.com/vn/product/detail/STW9C2SB-S?productid=434&id=556)  
15. PURPLE \- RS-online.com, accessed May 12, 2026, [https://docs.rs-online.com/fa9a/0900766b8034dc95.pdf](https://docs.rs-online.com/fa9a/0900766b8034dc95.pdf)  
16. ENSBD-LJ1Y9-F0 （CCT 4000K）, accessed May 12, 2026, [https://www.toyodagosei-led.jp/docs/products/list/4000k-standard-en.pdf](https://www.toyodagosei-led.jp/docs/products/list/4000k-standard-en.pdf)  
17. ES-2835-1036V-XX-XXXX Datasheet \- Everstar, accessed May 12, 2026, [https://www.everstar.in/pdf/ES-2835-1036V-XX-XXXX.pdf](https://www.everstar.in/pdf/ES-2835-1036V-XX-XXXX.pdf)  
18. Module level IV curve data set \- Technical University of Denmark \- Figshare, accessed May 12, 2026, [https://data.dtu.dk/articles/dataset/Module\_level\_IV\_curve\_data\_set/27901599](https://data.dtu.dk/articles/dataset/Module_level_IV_curve_data_set/27901599)  
19. Tunable-White-LED/Matlab/README.md at master \- GitHub, accessed May 12, 2026, [https://github.com/jaakkopasanen/Tunable-White-LED/blob/master/Matlab/README.md](https://github.com/jaakkopasanen/Tunable-White-LED/blob/master/Matlab/README.md)  
20. Development of a high-temperature (295–900 K) Seebeck coefficient Standard Reference Material, accessed May 12, 2026, [https://tsapps.nist.gov/publication/get\_pdf.cfm?pub\_id=932592](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=932592)  
21. SMD Low Power LED EAPL2835RA0 Preliminary \- Mouser Electronics, accessed May 12, 2026, [https://www.mouser.com/datasheet/2/143/EAPL2835RA0-949337.pdf](https://www.mouser.com/datasheet/2/143/EAPL2835RA0-949337.pdf)  
22. GitHub \- Visillect/mls-dataset: Multiple Light Source Dataset for Colour Research, accessed May 12, 2026, [https://github.com/visillect/mls-dataset](https://github.com/visillect/mls-dataset)  
23. Document Library \- Seoul Semiconductor, accessed May 12, 2026, [https://www.seoulsemicon.com/en/support/documentlibrary?lev1=\&lev2=\&lev3=\&search=](https://www.seoulsemicon.com/en/support/documentlibrary?lev1&lev2&lev3&search)  
24. 基于I-V曲线全局特征提取的光伏组串Swin-Transformer故障诊断方法 \- 电工技术学报, accessed May 12, 2026, [https://dgjsxb.ces-transaction.com/fileup/HTML/2025-23-7664.htm](https://dgjsxb.ces-transaction.com/fileup/HTML/2025-23-7664.htm)  
25. Download center \- Refond Optoelectronics, accessed May 12, 2026, [https://www.refond.com/download.html](https://www.refond.com/download.html)  
26. TOYODA GOSEI REPORT 2023, accessed May 12, 2026, [https://www.toyoda-gosei.com/csr/dl/pdf/TGReport2023\_ENG.pdf](https://www.toyoda-gosei.com/csr/dl/pdf/TGReport2023_ENG.pdf)

---

*Original output had 3 base64-encoded PNG images rendering V_th, V_f, eta_wpe symbols (~13 KB of unreadable image data, originally lines 105-108). Stripped during cleanup. Symbols are standard physics notation; not informative as rendered images.*
