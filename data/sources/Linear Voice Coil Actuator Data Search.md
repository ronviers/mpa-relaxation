# **Cross-Substrate Universality in Linear Voice Coil Actuators**

## **1\. Canonical Actuator Candidates**

| Actuator Model & Context | Electromagnetic Parameters URL (BL, R, L, M, K) | Step-Response Data URL |
| :---- | :---- | :---- |
| **Macro-Micro VCM Stage** Dual-stage linear positioner (480 turns, 10N/A force constant).1 | https://www.mdpi.com/2076-0825/12/3/132 | https://www.mdpi.com/2076-0825/12/3/132 |
| **Expiratory Valve VCA** Moticont LVCM-025-022-01 / BEI Kimco LA152600A (4-40g mass).2 | https://www.diva-portal.org/smash/get/diva2:998717/FULLTEXT01.pdf | https://www.diva-portal.org/smash/get/diva2:998717/FULLTEXT01.pdf |
| **POD Tribometer VCA** Box-Jenkins identified 2nd-order transfer function (![][image1]).3 | https://www.diva-portal.org/smash/get/diva2:1954209/FULLTEXT01.pdf | https://www.diva-portal.org/smash/get/diva2:1954209/FULLTEXT01.pdf |
| **H2W NCM02-10-008-2JBA** Haptic/Vibrotactile VCA (11.2N peak force).4 | https://www.researchgate.net/publication/335354953\_Vibrotactile\_Quality\_Assessment\_Hybrid\_Metric\_Design\_Based\_on\_SNR\_and\_SSIM | https://pmc.ncbi.nlm.nih.gov/articles/PMC10611303/ |
| **PMD C10-100 LRA** Bare linear resonant actuator (![][image2], Q, impedance).7 | https://www.precisionmicrodrives.com/ab-003 | https://www.precisionmicrodrives.com/new-testing-for-the-precision-haptic-erms |

## **2\. Q ↔ Damping-Rate Mapping**

| Stage | Algebraic Expression |
| :---- | :---- |
| **Base Equation** | **![][image3]** |
| **Kinematic Form** | **![][image4]** |
| **Standard Form** | **![][image5]** |
| **Base Parameters** | **![][image6]**, ![][image7] |
| **Q to ![][image8] Mapping** | **![][image9]** |
| **Damping Rate (![][image10])** | **![][image11]** |
| **Damped Frequency (![][image12])** | **![][image13]** |

| Q Value | Damping Rate (γ) | Damped Frequency (ωd​) | Regime |
| :---- | :---- | :---- | :---- |
| **0.5** | **![][image14]** | **![][image15]** | Critically Damped (![][image16]) |
| **0.707** | **![][image17]** | **![][image18]** | Butterworth / Maximally Flat |
| **1.0** | **![][image19]** | **![][image20]** | Underdamped (![][image21]) |

## **3\. Tunable Actuator Testbeds**

| Target Criteria | Status / Source | URL / Context |
| :---- | :---- | :---- |
| **Continuous Q-Walking Linear Testbed** (![][image22]) | Null Source. | No published open-loop step-response dataset sweeping physical ![][image23] damping exists for linear VCMs/LRAs. |
| **Discrete Damping Linear Testbed** | Active Eddy Current Damper (AECD) VCM.10 | https://www.researchgate.net/publication/379522938\_A\_Novel\_Nanopositioning\_Stage\_Integrated\_With\_Voice\_Coil\_Motor\_and\_Active\_Eddy\_Current\_Damper |
| **Continuous Q-Walking Rotary Testbed** (Non-linear) | TeachSpin Torsional Oscillator (![][image24]).11 | https://www.teachspin.com/torsional-oscillator |

## **4\. Open-Data Archives**

| Repository | Dataset Name & Actuator Type | Download URL / DOI |
| :---- | :---- | :---- |
| **Mendeley Data** | "OPU force analyzer" (HD-DVD VCM / OIS-scale).12 | https://doi.org/10.17632/cnkd95kp65.1 |
| **Zenodo** | "Improving Texture Discrimination in Virtual Tasks" (Haptic Linear VCA).13 | https://doi.org/10.5281/zenodo.4813359 |
| **Zenodo** | "Diurnal and Seasonal Mapping of Martian Ices With EMIRS" (Dual linear VCM / 40kHz telemetry).15 | https://doi.org/10.5281/zenodo.7714205 |
| **MathWorks** (IEEE IEE Committee) | "Magnetic-head positioning control system in HDDs" (Dual-stage VCM \+ PZT time-series).16 | https://jp.mathworks.com/matlabcentral/fileexchange/111515-magnetic-headpositioning-control-system-in-hdds |

#### **Works cited**

1. A Compact Electromagnetic Dual Actuation Positioning System with ..., accessed May 12, 2026, [https://www.mdpi.com/2076-0825/12/3/132](https://www.mdpi.com/2076-0825/12/3/132)  
2. Model based design of an expiratory valve and voice-coil actuator \- Diva-Portal.org, accessed May 12, 2026, [https://www.diva-portal.org/smash/get/diva2:998717/FULLTEXT01.pdf](https://www.diva-portal.org/smash/get/diva2:998717/FULLTEXT01.pdf)  
3. System identification and development of a H-infinity Controller for a Pin-On-Disc Tribometer. \- Diva-Portal.org, accessed May 12, 2026, [https://www.diva-portal.org/smash/get/diva2:1954209/FULLTEXT01.pdf](https://www.diva-portal.org/smash/get/diva2:1954209/FULLTEXT01.pdf)  
4. A Hand-Held Device Presenting Haptic Directional Cues for the Visually Impaired \- PMC, accessed May 12, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC10611303/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10611303/)  
5. Vibrotactile Quality Assessment: Hybrid Metric Design Based on SNR and SSIM, accessed May 12, 2026, [https://www.researchgate.net/publication/335354953\_Vibrotactile\_Quality\_Assessment\_Hybrid\_Metric\_Design\_Based\_on\_SNR\_and\_SSIM](https://www.researchgate.net/publication/335354953_Vibrotactile_Quality_Assessment_Hybrid_Metric_Design_Based_on_SNR_and_SSIM)  
6. High Frequency Acceleration Feedback Signiﬁcantly Increases the Realism of Haptically Rendered Textured Surfaces, accessed May 12, 2026, [https://repository.upenn.edu/bitstreams/a6a3b798-a96e-484d-8721-4dd7bbc56efa/download](https://repository.upenn.edu/bitstreams/a6a3b798-a96e-484d-8721-4dd7bbc56efa/download)  
7. Linear Resonant Actuator (LRA) Design & Integration Guide \- INEED Motors, accessed May 12, 2026, [https://article.ineedmotors.com/linear-resonant-actuator-lra-design-integration-guide/](https://article.ineedmotors.com/linear-resonant-actuator-lra-design-integration-guide/)  
8. AB-003: Driving Linear Resonance Vibration Actuators \- Precision Microdrives, accessed May 12, 2026, [https://www.precisionmicrodrives.com/ab-003](https://www.precisionmicrodrives.com/ab-003)  
9. New Testing for the Precision Haptic™ ERMs, accessed May 12, 2026, [https://www.precisionmicrodrives.com/new-testing-for-the-precision-haptic-erms](https://www.precisionmicrodrives.com/new-testing-for-the-precision-haptic-erms)  
10. A Novel Nanopositioning Stage Integrated With Voice Coil Motor and Active Eddy Current Damper | Request PDF \- ResearchGate, accessed May 12, 2026, [https://www.researchgate.net/publication/379522938\_A\_Novel\_Nanopositioning\_Stage\_Integrated\_With\_Voice\_Coil\_Motor\_and\_Active\_Eddy\_Current\_Damper](https://www.researchgate.net/publication/379522938_A_Novel_Nanopositioning_Stage_Integrated_With_Voice_Coil_Motor_and_Active_Eddy_Current_Damper)  
11. Torsional Oscillator \- TeachSpin, accessed May 12, 2026, [https://www.teachspin.com/torsional-oscillator](https://www.teachspin.com/torsional-oscillator)  
12. 3D Printing of Microcontainers for Oral Delivery of Drugs and Probiotics \- DTU Inside, accessed May 12, 2026, [https://backend.orbit.dtu.dk/ws/files/273458374/Tien\_Jen\_Chang\_thesis.pdf](https://backend.orbit.dtu.dk/ws/files/273458374/Tien_Jen_Chang_thesis.pdf)  
13. Publications \- Interactions Lab \- University of Calgary, accessed May 12, 2026, [https://ilab.ucalgary.ca/publications/](https://ilab.ucalgary.ca/publications/)  
14. CyberDiver: an untethered robotic impactor for water-entry experiments \- arXiv, accessed May 12, 2026, [https://arxiv.org/html/2503.20702v1](https://arxiv.org/html/2503.20702v1)  
15. Diurnal and Seasonal Mapping of Martian Ices With EMIRS \- ResearchGate, accessed May 12, 2026, [https://www.researchgate.net/publication/371874531\_Diurnal\_and\_Seasonal\_Mapping\_of\_Martian\_Ices\_With\_EMIRS](https://www.researchgate.net/publication/371874531_Diurnal_and_Seasonal_Mapping_of_Martian_Ices_With_EMIRS)  
16. Benchmark problem for magnetic-head positioning control in HDD ..., accessed May 12, 2026, [http://www2.iee.or.jp/\~dmec/committee/DMEC1005/UserManual\_rev1.0.8.pdf](http://www2.iee.or.jp/~dmec/committee/DMEC1005/UserManual_rev1.0.8.pdf)


---

*Original output had 13 base64-encoded PNG images rendering the Q2 formulas and sanity-check table (~42 KB of unreadable data, originally lines 67-112). Stripped during cleanup. The textbook Q-to-gamma derivation is captured cleanly in [actuator-research-cross-reference.md](actuator-research-cross-reference.md) and the handoff Gotchas section.*
