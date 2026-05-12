### 1. Canonical actuator candidates

A single peer‑reviewed source provides both the full electromagnetic parameter set and published step‑response time‑series for a bare voice‑coil actuator (bobbin‑on‑cantilever, no cone/cavity, no rotating stage).

| Model / Source | Parameter URL | Step‑response data URL |
|----------------|---------------|-------------------------|
| VCA cantilever (Al bobbin) — “Effect of Electromagnetic Damping on System Performance of Voice‑Coil Actuator…” Actuators 2020, 9(1), 8. | [https://www.mdpi.com/2076-0825/9/1/8/pdf](https://www.mdpi.com/2076-0825/9/1/8/pdf) (Table 2: m=0.0652 kg, c=0.3 N·s/mm, k=1.485 N/mm, R=28.9 Ω, L=24.535 mH, kf=28.46 N/A) | [https://www.mdpi.com/2076-0825/9/1/8/pdf](https://www.mdpi.com/2076-0825/9/1/8/pdf) (Section 4, Figure 12 & Figure 13 – experimental step‑input deflection time traces) |
| VCA cantilever (plastic bobbin) — same paper | as above (Table 2: m=0.0652 kg, c=0.025 N·s/mm, k=1.485 N/mm, R=28.9 Ω, L=24.535 mH, kf=28.46 N/A) | as above (Figure 12 & Figure 13 – reduced‑damping step responses) |

*No additional actuators meeting the dual requirement of full parameter publication and open‑loop step‑response time‑series were found. All other candidates encountered (commercial HDD VCMs, OIS actuators, lithography stages, haptic LRAs, magnetic‑levitation stages, AFM scanners) either lack one of the two datasets or are documented only under closed‑loop servo control.*

---

### 2. Q ↔ damping‑rate mapping

For the voice‑coil‑driven second‑order mass‑spring‑damper

\[
m\,\ddot x + c\,\dot x + k\,x = (BL)\,i(t)
\]

the force constant \(k_f = BL\) and the transfer function from current to position is

\[
\frac{X(s)}{I(s)} =
\frac{k_f/k}{ \displaystyle\frac{s^2}{\omega_n^2} + \displaystyle\frac{2\zeta s}{\omega_n} + 1 }\,,
\qquad
\omega_n = \sqrt{\frac{k}{m}},\;
\zeta = \frac{c}{2\sqrt{mk}} .
\]

The electrical quality factor of the series R–L–C resonator is **not** directly the mechanical Q; for the mechanical subsystem the resonant quality factor is defined as

\[
Q \equiv \frac{1}{2\zeta}
\quad\text{(mechanical oscillator driven at resonance)} .
\]

Thus the exponential damping coefficient \(\gamma\) (the rate of decay of an unforced response) and the damped natural frequency \(\omega_d\) are:

\[
\boxed{\gamma = 2\zeta\omega_n = \frac{\omega_n}{Q}},\qquad
\boxed{\omega_d = \omega_n\sqrt{1-\zeta^{2}} = \omega_n\sqrt{1-\frac{1}{4Q^{2}}}} .
\]

---

**Sanity‑check table**

| \(Q\) | \(\zeta\) | \(e^{-\gamma t}\) decay rate | \(\omega_d\) |
|------|-----------|-----------------------------|-------------|
| 0.5  | 1.0       | \(\gamma = \omega_n / 0.5 = 2\omega_n\) | 0 (critically damped) |
| 0.707 | 0.707    | \(\gamma = \omega_n / 0.707 \approx 1.414\,\omega_n\) | \(\omega_n\sqrt{1-0.5} = 0.707\,\omega_n\) |
| 1.0  | 0.5       | \(\gamma = \omega_n\)       | \(\omega_n\sqrt{1-0.25} = 0.866\,\omega_n\) |

---

### 3. Tunable‑actuator testbed

A single published test rig documents Q variation across the overdamped → critically‑damped → underdamped range by changing the bobbin material, thereby altering the eddy‑current damping.

| Testbed description | Parameter range achieved | Per‑Q step‑response data | Source URL |
|---------------------|--------------------------|---------------------------|------------|
| Cantilever beam with attached bobbin, positioned over a permanent magnet; bobbin material swapped between **aluminum** (high eddy‑current damping) and **plastic** (negligible eddy currents). | Aluminum: \(c=0.3\,\text{N·s/mm}\), \(\zeta=15.2\), \(Q\approx0.033\) (deeply over‑damped).<br>Plastic: \(c=0.025\,\text{N·s/mm}\), \(\zeta=1.27\), \(Q\approx0.39\) (near‑critically damped).<br>**Note:** The Q range falls short of the requested ～0.3–2.0 span; however, the principle of Q tuning via eddy‑current damping is explicitly demonstrated. | Yes – Figure 12 & Figure 13 show step‑input deflection responses for both bobbins. | [https://www.mdpi.com/2076-0825/9/1/8/pdf](https://www.mdpi.com/2076-0825/9/1/8/pdf) |

*No testbed was found that walks Q continuously from ～0.3 to ～2.0 through adjustable mass, eddy‑current damping, or viscous‑compensation current while publishing per‑Q step‑response data.*

---

### 4. Open‑data archives

A systematic scan of Zenodo, Mendeley Data, IEEE DataPort, MDPI Actuators supplementary files, DSpace@MIT, and ePrints Soton returned **no downloadable time‑series datasets** for step responses of bare linear voice‑coil actuators. The only relevant entry is the supplementary‑material link for the paper cited above, which embeds the step‑response figures in the PDF but does not provide machine‑readable time‑series files.

| Repository | Query | Result |
|------------|-------|--------|
| Zenodo | “voice coil” + “step response” | No relevant datasets |
| Mendeley Data | “voice coil actuator” | No step‑response datasets |
| IEEE DataPort | “voice coil motor” | No open‑loop step data |
| MDPI Actuators supplementary | article supplementary files (2076-0825/9/1/8) | Figures embedded in PDF; no separate time‑series download |
| DSpace@MIT | “voice coil” + “step response” | Only educational pre‑lab materials, no empirical time‑series |
| ePrints Soton | “voice coil actuator” | No matching datasets |

**Conclusion:** Open‑data archives currently lack curated, reusable time‑series step‑response datasets for the specified linear voice‑coil actuator types.