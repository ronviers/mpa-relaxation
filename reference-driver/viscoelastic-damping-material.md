# Reference driver — viscoelastic damping material (substrate-three)

**Substrate-class:** `viscoelastic-damping-material`
**Substrate-class type:** `pure-dissipative` (drive and "useful work" share the same mode)
**F-001 applicability:** NO — dissipation IS the useful work; chit_max bound is vacuous
**F-003 applicability:** YES — Q = 1/tan δ; regime structure holds across material heterogeneity
**Status:** v0.1 — substrate-three of mpa-relaxation. First substrate where F-001 hits a scope limit (FOOTING F-001-scope-limit entry 2026-05-12). Stress-test substrate for substrate-class diversity (FOOTING F-003-viscoelastic entry 2026-05-12).
**Targets:** [cdv1 (compressed)](https://github.com/ronviers/mpa-atlas/blob/main/framework/cdv1_compressed.md).
**Shape:** [RFC-S §4 driver profile](https://github.com/ronviers/mpa-atlas/blob/main/rfcs/MPA-RFC-S_Scale-Management.md#4-driver-profile).

---

## 1. Substrate-class declaration

A viscoelastic damping material: a polymeric medium with frequency- and temperature-dependent complex modulus E*(ω, T) = E'(ω, T) + i·E''(ω, T). The substrate-class characterization observable is the loss tangent η = tan δ = E''/E'. Materials in this class are designed to convert mechanical vibration energy into heat — that conversion IS the substrate's purpose. The substrate-class spans constrained-layer damping films (3M ISD-112), urethane elastomers (Sorbothane, EAR Isodamp), acrylic foams (3M VHB), natural and synthetic rubbers (natural rubber gum, butyl rubber), plasticized polymers (PVC vinyl damping sheets), and high-damping polyurethanes (PU45A).

**Mode-separation status: pure-dissipative.** Drive mode: mechanical vibration (input strain ε(t)). "Useful work" mode: heat (dissipation rate ε₀²·E''·ω·π per cycle). **Drive and useful-work share the mechanical-dissipation channel.** There is no separate output mode through which power flows. This breaks F-001's mode-separation precondition: η_conversion = 1 by construction (all input becomes dissipation), so F-001 chit_max = -ln(0) → ∞, the bound is vacuous.

F-003 (regime structure from Q = 1/tan δ) applies cleanly. Different material formulations give different tan δ; the substrate-class spans c (tan δ < 2), s (tan δ = 2), and r (tan δ > 2) regimes by polymer composition tuning.

Substrate excludes: structural polymers (used for stiffness, not damping — different design intent and tan δ regime); elastic compounds with negligible loss; damping treatments where the damping material is one component of a multi-mode structure (constrained-layer damping in a vibrating plate is a *system*, not a substrate-class instance).

## 2. Header

| Field | Value |
|---|---|
| `profile_version` | 0.1 |
| `target_rfc_versions` | RFC-S v0.2, RFC-C v0.2, cdv1 (compressed) |
| `substrate_class` | `viscoelastic-damping-material` |
| `substrate_class_type` | `pure-dissipative` |
| `drive_mode` | mechanical vibration (input strain) |
| `useful_work_mode` | heat (same channel as dissipation; no mode separation) |
| `f_001_applicability` | NO (η_conversion → 1 by construction; chit_max bound vacuous) |
| `f_003_applicability` | YES (Q = 1/tan δ; substrate-class spans c, s, r) |
| `characterization_date` | 2026-05-12 |
| `authority` | mpa-relaxation v0 scaffold (data from Jones 2001, Nashif et al. 1985, vendor sheets) |
| `validation_history` | F-003-viscoelastic stress test PASS 2026-05-12 (8 materials, all 3 regimes represented, 4 of 8 within 0.17 of critical, one instance at Q = 0.5 exactly by formulation). |

## 3. Operating envelope

Substrate-class-conditional. Per-material specifics declared in the calibration record.

- **Loss tangent range:** tan δ ∈ [0.1, 3.0] across the substrate-class. Below 0.1: elastic, not designed for damping. Above 3.0: r-regime sluggish, rare in commercial materials.
- **Temperature range:** Material-specific; typical operating window [-40°C, 90°C] for industrial polymers. tan δ peak position shifts ~20–60 K across the glass-transition temperature.
- **Frequency range:** Material-specific; typical [1 Hz, 10 kHz] for vibration-damping applications. tan δ peak position shifts with frequency via WLF time-temperature superposition.
- **Strain amplitude:** Linear viscoelastic regime assumed (small strain, < 1% typically). Nonlinear viscoelasticity at large strain is out of substrate-class.

## 4. Gamut

| Axis | Substrate-declared content |
|---|---|
| Drive axis (G₀) | Mechanical power input via imposed strain. G₀ = ε₀² · ω · E''(ω, T) · π per cycle at strain amplitude ε₀, frequency ω, temperature T. |
| Loss axis (L) | Same as G₀ by construction (all input dissipates as heat). chit at steady-state oscillation: ln(G₀/L) = ln(1) = 0 trivially. |
| Observer scale τ_obs | One oscillation period (2π/ω) to thermal-soak timescale (~minutes for the polymer to equilibrate with environment after strain power input). |
| Reachable regimes | c (tan δ < 2), s (tan δ = 2), r (tan δ > 2). All three reachable by polymer composition. |
| Persistence depth | Single-level — viscoelastic damping does not tower in the cdv1 §Heat-tax sense. |

**F-001 applicability declaration:** NO. Since drive and useful-work share the same channel (mechanical input → heat dissipation), η_conversion = 1 and the F-001 bound is vacuous. This substrate-class is in the **pure-dissipative** scope where F-001 does not apply but F-003 does.

## 5. Translation field (substrate-native → canonical)

| Substrate-native observable | Canonical | Read |
|---|---|---|
| Storage modulus E'(ω, T) | Substrate stiffness (k-analog) | Multiplication by geometry factor (area / thickness) → effective spring constant for a coupled mass-spring system. |
| Loss modulus E''(ω, T) | Substrate dissipation (c-analog) | Multiplication by ω and geometry → effective damping coefficient. |
| Loss tangent tan δ = E''/E' | Q⁻¹ | Direct: Q = 1/tan δ at the operating (ω, T) point. |
| tan δ(ω, T) surface | Substrate gamut | The full multi-parameter dependence; substrate-class instances differ by their tan δ peak position in (ω, T) space. |

## 6. Intents

Per RFC-S §3, the five intents:

| Intent | Applies? | Notes |
|---|---|---|
| I1 regime-preserving | yes | Q from tan δ classifies regime consistently across materials. |
| I2 drive-faithful | partial | Drive-faithful in the steady-state-oscillation reading; transient response involves the multi-rate viscoelastic relaxation spectrum (Prony series, fractional Maxwell models). v0.2 may unfold this. |
| I3 capacity-preserving | N/A | Single-mode oscillator equivalent; capacity trivial. |
| I4 persistence-preserving | N/A | Single-level. |
| I5 signature-preserving | yes | tan δ peak position and amplitude are the substrate-class fingerprint. F-003 confirmed across material heterogeneity. |

## 7. Reference outputs

Canonical test inputs and expected substrate responses, for round-trip validation:

- **Loss tangent at design (T, f):** Substrate-class instance's characteristic Q value. PU45A reference: tan δ = 2.0 → Q = 0.5 (s-boundary by design).
- **Loss tangent peak position:** Material-specific (ω_peak, T_peak); shifts via time-temperature superposition.
- **Substrate-class chit reading:** chit = 0 at steady-state oscillation (SOC attractor trivially landed; F-002 holds for this substrate-class by power-balance construction, not by feedback control).
- **Regime distribution across substrate-class:** at typical design (T, f), commercial damping materials cluster Q ∈ [0.5, 1.5] (substrate-class fingerprint: engineering tuning toward s-boundary).

## 8. Metadata

Methodology: Loss tangent values published in handbooks (Jones, *Handbook of Viscoelastic Vibration Damping*, Wiley 2001; Nashif, Jones, Henderson, *Vibration Damping*, Wiley 1985) and vendor datasheets (3M, EAR Specialty Composites, Sorbothane, Roush, SoundCoat). DMA (Dynamic Mechanical Analysis) measurement per ASTM E756 vibrating-beam method or ASTM D5992 oscillatory torsion method. Vendor methodology not always standardized; cross-vendor comparison requires verifying test conditions match.

**Known limitations:**

- Single-point characterization (peak tan δ at one (T, f)) hides the full multi-parameter substrate. Full characterization requires DMA sweep across (T, f) — substrate-conditional and beyond v0.1 scope.
- Vendor-published values may use different test geometries (beam vs torsion vs compression DMA); cross-substrate calibration must align test conditions.
- Aging effects (oxidation, plasticizer migration, thermal degradation) shift tan δ over substrate lifetime. Calibration records should declare substrate-age state.

**Versioning:** v0.1 covers single-point peak-tan-δ characterization. v0.2 would unfold the (ω, T) tan δ surface for at least one substrate-class instance (full DMA spectrum). v0.3 would handle the time-temperature-superposition (WLF) shift to predict tan δ at off-design conditions.

## Page-budget self-check

Target: ≤1 page per [thin-RFC discipline](https://github.com/ronviers/mpa-atlas/blob/main/CLAUDE.md). This driver profile runs ~2 pages, same pattern as other substrate driver profiles in mpa-relaxation. The growth past target is driven by the substrate-class scope-limit declaration (§1 mode-separation status discussion) and the multi-parameter (T, f) dependence note in §3. First per-material calibration record (Phase D candidate: PU45A as the canonical s-boundary instance) will land at one page or less.
