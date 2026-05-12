# Reference driver — voice coil linear actuator

**Substrate-class:** `voice-coil-linear-actuator`
**Status:** v0.1 — substrate-zero of mpa-relaxation. First calibration record pending external research output.
**Targets:** [cdv1 (compressed)](https://github.com/ronviers/mpa-atlas/blob/main/framework/cdv1_compressed.md).
**Shape:** [RFC-S §4 driver profile](https://github.com/ronviers/mpa-atlas/blob/main/rfcs/MPA-RFC-S_Scale-Management.md#4-driver-profile).

---

## 1. Substrate-class declaration

A linear voice coil actuator: a coil constrained to translate within a permanent magnet's gap, generating Lorentz force F = BL·i under electrical drive against a mechanical suspension and (configurable) external load. The substrate-class spans hard disk drive head positioners, camera optical image stabilizers, semiconductor lithography stages, haptic linear resonant actuators, inertial vibration actuators, MRI gradient coils, and laboratory shakers. All read through the same cdv1 primitives; per-instance amplitudes declared in per-actuator calibration records.

Substrate excludes: rotating motors (DC, BLDC, stepper) — those are a different substrate-class with different chit structure. Loudspeaker drivers are a configured instance of this substrate (cone + cavity load), characterized separately in Phase E.

## 2. Header

| Field | Value |
|---|---|
| `profile_version` | 0.1 |
| `target_rfc_versions` | RFC-S v0.2, RFC-C v0.2, cdv1 (compressed) |
| `substrate_class` | `voice-coil-linear-actuator` |
| `characterization_date` | 2026-05-12 |
| `authority` | mpa-relaxation v0 scaffold |
| `validation_history` | none yet (first calibration record pending external research) |

## 3. Operating envelope

Substrate-class-conditional. Per-actuator specifics declared in the calibration record.

- **Displacement range:** [-x_max, +x_max]. Bounded by the magnetic gap geometry and suspension travel. Operation past x_max is gamut-edge (BL falls off, suspension hits stops).
- **Current range:** [-i_max, +i_max]. Bounded by thermal limits (continuous I²·R heating) and saturation of the magnetic gap.
- **Frequency range:** Mechanical resonance ω₀ = √(K/M) is the natural reference. Above ω₀: mass-dominated, inertial regime. Below ω₀: stiffness-dominated, quasi-static. Damping region around ω₀: substrate-conditional Q.
- **Thermal envelope:** Coil resistance R(T) drifts with self-heating. Substrate-conditional; calibration records may declare a `thermal_state` field.

## 4. Gamut

| Axis | Substrate-declared content |
|---|---|
| Drive axis (G₀) | Electrical power into the coil. G₀ = V·I = I²·R + BL·v·I where BL·v is back-EMF power coupled to mechanical motion. Range: zero to i_max² · R + saturated electromagnetic conversion. |
| Loss axis (L) | Sum of decomposed losses: I²·R thermal (electrical resistive), suspension damping b·v² (mechanical), load damping (configurable), eddy-current losses in the magnetic structure, friction in bearings (if present). Substrate-instrumented if all components measurable. |
| Observer scale τ_obs | Single mechanical period (~2π/ω₀) to actuator lifetime. Canonical τ_obs for cdv1 reading: step-response averaging window, sized to ~10·(2π/ω₀). |
| Reachable regimes | c (Q > 0.5, underdamped — most actuators in nominal operation), s (Q = 0.5, critically tuned settling), r (Q < 0.5, overdamped — heavily-loaded or eddy-braked). All three reachable by tuning load mass / damping. |
| Persistence depth | Single-mode — voice coil actuators do not tower in the cdv1 §Heat-tax sense. |

## 5. Translation field (substrate-native → canonical)

| Substrate-native observable | Canonical | Read |
|---|---|---|
| Position x(t) | ρ (coherence amplitude) | Direct: sustained position tracking is the substrate's coherence. |
| Coil current I(t) | Drive amplitude (proxy for G₀) | G₀ = V·I; if V not measured, G₀ ≈ I²·R + BL·v·I from current and velocity. |
| Coil resistance R | Static loss component | Direct: I²·R is the resistive dissipation. Declared per drive level (thermal drift). |
| BL product | Electromagnetic coupling | Direct from datasheet or back-EMF measurement (BL = -V_back / v). |
| Moving mass M, suspension stiffness K | Mechanical resonance ω₀ = √(K/M) | Direct: measurable by added-mass method or free-decay. |
| Step response x(t) settling | Recovery profile, c/s/r diagnostic | Fit to e^(-γt)·[A·cos(ω_d·t) + B·sin(ω_d·t)] gives γ and ω_d; Q = ω₀/(2γ). |
| Sustained operating point (NESS) | chit = 0 | At steady-state oscillation under sinusoidal drive at ω₀, G₀ = L by power balance; chit = 0 exactly. The SOC-attractor result. |

## 6. Intents

Per RFC-S §3, the five intents:

| Intent | Applies? | Notes |
|---|---|---|
| I1 regime-preserving | yes | Cross-actuator fingerprint reads chit-envelope and Q structure across HDD VCMs, OIS actuators, LRAs, inertial actuators. |
| I2 drive-faithful | yes | Per-actuator calibration records preserve exact G₀ and L at calibrated operating points. |
| I3 capacity-preserving | partial | Single-mode actuators collapse Erlang-B closure of cdv1 §Capacity to one channel. Multi-coil or multi-axis stages (e.g., 6-DOF lithography) may read as multi-mode — open. |
| I4 persistence-preserving | N/A | Single-level substrate; no persistence tower. |
| I5 signature-preserving | yes | Step-response settling profile is the substrate's relaxation signature. cdv1 §Stability predicts algebraic settling at Q = 0.5 (chit ≈ 0), exponential decay elsewhere. Phase C tests this directly. |

## 7. Reference outputs

Canonical test inputs and expected substrate responses, for round-trip validation:

- **Steady-state sinusoidal drive at ω₀:** chit = 0 exactly. Pass criterion: G₀ = L within current and velocity measurement uncertainty.
- **Step current input, observe position settling:** Fit e^(-γt)·cos(ω_d·t). Q = ω₀/(2γ) substrate-class-conditional regime classifier.
- **Free decay from initial displacement (no drive):** Q = ω₀/(2γ_natural) is the substrate's intrinsic Q without external load. Substrate-class fingerprint candidate.
- **chit envelope:** Substrate-conditional. HDD VCMs: typically Q ≈ 0.7–1.0 (engineered for fast seek without overshoot). LRAs: Q ≈ 50–100 (narrow-band haptic). Lithography stages: Q ≈ 0.5–0.7 (critical for fastest settling). Open prediction: chit_max bounded by -ln(1 - η) where η is electromechanical conversion efficiency (typically 0.3–0.8 for voice coil actuators), giving chit_max bounds in [0.36, 1.6] depending on substrate instance.

## 8. Metadata

Methodology: published step-response data, frequency-response data, or impulse-response data from a controlled test rig. The substrate's exchange surface is the (current, position) time-series — that's what every characterization apparatus exposes.

Known limitations:
- Closed-loop control routinely wraps actuators in industrial use, hiding the open-loop substrate behind controller dynamics. Calibration records must specify open-loop test or explicitly decompose plant from controller per cdv1 §Active modulation.
- Hysteresis and BL-vs-position nonlinearity (per Klippel-type analysis) drift Q at large signals. Calibration records declare drive level.
- Eddy-current damping is amplitude-dependent in some designs (notably HDD VCMs with conductive top plates). Adds a Q-dependence on drive level.

Versioning: v0.1 is the substrate-class scaffold. v0.2 lands when the first calibration record (TBD canonical actuator) populates the gamut and reference outputs with concrete amplitudes. v0.3 (or v1.0) lands when at least two actuator instances are characterized for cross-instance fingerprint validation.

## Page-budget self-check

Target: ≤1 page per [thin-RFC discipline](https://github.com/ronviers/mpa-atlas/blob/main/CLAUDE.md). This driver profile runs ~2 pages, same growth pattern as mpa-engine's IC-engine driver profile: eight-section RFC-S §4 structure, substrate-class enumeration in §6, reference outputs in §7. First per-actuator calibration record will land at one page or less.

**Debt-marker:** §6 I3 ("partial") closes when we decide whether multi-axis / multi-coil stages read as multi-mode (then I3 has content) or as one mode per axis (then I3 is vacuous for substrate zero — multi-axis stages get their own substrate-class). Defer until a candidate multi-axis dataset surfaces. Revert condition: I3 resolves cleanly, table tightens.
