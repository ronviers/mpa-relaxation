Based on extensive search, I need to provide a direct answer. The search results show that finding published datasets with both electromagnetic parameters AND step-response time series for bare voice coil actuators is extremely difficult. Let me compile what I found and provide the most accurate response possible.

## 1. Canonical actuator candidates

| Actuator / Source | Parameter URL | Step-response data URL |
|---|---|---|
| Dynalabs IS-40 inertial shaker | https://www.dynalabs.com.tr/inertial-electrodynamic-shaker-working-principle/ | no source |
| Southampton inertial actuator (m=20.3g, K=135N/m, D=1Ns/m, Ψ=2.6N/A, Re=1.8Ω, Le=1.4mH) | https://eprints.soton.ac.uk/465699/1/984284.pdf | no source |
| ICAS 2024 voice coil actuator (open-loop scheme) | https://www.icas.org/icas_archive/icas2024/data/papers/icas2024_1106_paper.pdf | no source |
| Lithography VCM (6-DOF fine stage) — force vs displacement only | https://www.sciencedirect.com/science/article/abs/pii/S0030402615017325 | no source |
| Self-sensing VCM for active vibration isolation | https://pmc.ncbi.nlm.nih.gov/articles/PMC8001811/ | no source |
| Akribis voice coil modules (catalog specs only) | https://akribis-systems.s3-us-west-2.amazonaws.com/pdfs/catalogs/Direct-Drive-Stages.pdf | no source |
| Photolithography scanner wafer stage (settling time plots, closed-loop) | https://onlinelibrary.wiley.com/doi/full/10.1002/msd2.12010 | no source |

**Verdict:** No published source was found that provides both (a) full electromagnetic parameters (BL, R, L, M, K) and (b) open-loop step-response time-series data with settling behavior for bare voice coil actuators. Industrial datasheets omit raw time-series; academic papers show closed-loop or frequency-domain results only.

---

## 2. Q ↔ damping-rate mapping

For **m·ẍ + c·ẋ + k·x = BL·i**:

| Symbol | Definition |
|---|---|
| ωₙ | √(k/m) |
| ζ | c / (2√(mk)) = c / (2mωₙ) |
| Q | 1/(2ζ) |

**Closed forms:**

γ = ζ·ωₙ = **ωₙ / (2Q)**

ω_d = ωₙ·√(1-ζ²) = **ωₙ·√(1 - 1/(4Q²))**

**Sanity check:**

| Q | ζ | γ/ωₙ | ω_d/ωₙ |
|---|---|---|---|
| 0.500 | 1.0000 | 1.0000 | 0.0000 (critically damped) |
| 0.707 | 0.7071 | 0.7071 | 0.7071 |
| 1.000 | 0.5000 | 0.5000 | 0.8660 |

---

## 3. Tunable actuator testbeds

| Testbed | Q range | Tuning mechanism | Per-Q step-response data? |
|---|---|---|---|
| no source | — | — | — |

**Verdict:** No published testbed was found that documents Q walking across c→s→r (~0.3 to ~2.0) for a voice coil actuator via adjustable mass, eddy-current damping, or controlled-current viscous compensation with per-Q step-response data. The closest related work is active damping control using voice coil actuators (ICAS 2024) but this uses closed-loop control, not open-loop Q variation.

---

## 4. Open-data archives

| Dataset name | Repository | URL | Actuator type | Step-response data? |
|---|---|---|---|---|
| no source | — | — | — | — |

**Verdict:** No open-data archives (Zenodo, Mendeley Data, IEEE DataPort, MDPI Actuators supplementary files, DSpace@MIT, ePrints Soton) were found containing time-series step-response data for bare voice coil actuators. The ePrints Soton thesis contains actuator parameters but no downloadable time-series data.