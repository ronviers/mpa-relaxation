"""cdv1 chit reading on series RLC substrate (substrate-two).

A series RLC circuit (resistor + inductor + capacitor) driven by a voltage
source is the canonical analytical second-order driven-dissipative system.
Same ODE as a damped mechanical oscillator:

    L·d²q/dt² + R·dq/dt + (1/C)·q = V(t)

mapping (q ↔ x, L ↔ m, R ↔ c, 1/C ↔ k). Substrate parameters:

    ω₀ = 1/√(L·C)              natural frequency
    α  = R / (2L)              decay rate (= γ in oscillator notation)
    Q  = ω₀ / (2α) = (1/R)·√(L/C)   quality factor
    ζ  = α / ω₀ = 1/(2Q)       damping ratio

Step response x(t) for unit step input (V_source = 1, capacitor voltage
relaxing toward 1):

    Q > 0.5  (underdamped, c-regime):
        x(t) = 1 - e^(-α·t)·[cos(ω_d·t) + (α/ω_d)·sin(ω_d·t)]
        ω_d  = ω₀·√(1 - 1/(4Q²))

    Q = 0.5  (critically damped, s-boundary):
        x(t) = 1 - (1 + α·t)·e^(-α·t)
        *Decay envelope carries an algebraic factor (1 + α·t).*

    Q < 0.5  (overdamped, r-regime):
        x(t) = 1 - [r₂·e^(-r₁·t) - r₁·e^(-r₂·t)] / (r₂ - r₁)
        r₁,₂ = α ± √(α² - ω₀²)

cdv1 §Stability prediction: at Q = 0.5 (chit ≈ 0 SOC boundary), the relaxation
profile is qualitatively distinct from the c-regime (Q > 0.5, exponential
envelope) and the r-regime (Q < 0.5, double-exponential). The algebraic
factor (1 + α·t) at critical damping is the F-003 signature in this
substrate.

Substrate-two role: textbook null check. RLC has no measurement noise, no
substrate-conditional artefacts, no unmeasured loss channels. If the chit
machinery and regime-classification logic don't work cleanly here, they
won't work on real substrates either.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Optional

import numpy as np


@dataclass(frozen=True)
class RLCParameters:
    """Series RLC circuit parameter set."""
    R: float   # resistance, Ω
    L: float   # inductance, H
    C: float   # capacitance, F

    @property
    def omega_0(self) -> float:
        """Natural frequency ω₀ = 1/√(LC), rad/s."""
        return 1.0 / math.sqrt(self.L * self.C)

    @property
    def alpha(self) -> float:
        """Decay rate α = R/(2L), 1/s."""
        return self.R / (2.0 * self.L)

    @property
    def Q(self) -> float:
        """Quality factor Q = (1/R)·√(L/C)."""
        return (1.0 / self.R) * math.sqrt(self.L / self.C)

    @property
    def zeta(self) -> float:
        """Damping ratio ζ = α/ω₀ = 1/(2Q)."""
        return self.alpha / self.omega_0

    @property
    def regime(self) -> str:
        """Regime classification from Q. s-band ±0.02 around Q = 0.5."""
        if abs(self.Q - 0.5) <= 0.02:
            return "s"
        if self.Q > 0.5:
            return "c"
        return "r"

    @property
    def omega_damped(self) -> Optional[float]:
        """Damped oscillation frequency ω_d = ω₀·√(1 - 1/(4Q²)).

        Real for Q > 0.5; zero at Q = 0.5; None for Q < 0.5 (no oscillation).
        """
        if self.Q < 0.5:
            return None
        if self.Q == 0.5:
            return 0.0
        return self.omega_0 * math.sqrt(1.0 - 1.0 / (4.0 * self.Q * self.Q))


def rlc_from_Q(Q: float, omega_0: float = 1.0) -> RLCParameters:
    """Construct an RLC instance with target Q at a given ω₀.

    Picks L = 1 H by convention; computes R and C to satisfy ω₀ and Q.

    From ω₀ = 1/√(LC) and Q = (1/R)·√(L/C):
        C = 1 / (L·ω₀²)
        R = √(L/C) / Q = ω₀·L / Q
    """
    L = 1.0
    C = 1.0 / (L * omega_0 * omega_0)
    R = omega_0 * L / Q
    return RLCParameters(R=R, L=L, C=C)


def step_response(params: RLCParameters, t: np.ndarray) -> np.ndarray:
    """Series RLC step response: capacitor voltage relaxing toward unit step.

    Returns x(t) where x(0) = 0 and x(∞) = 1.
    """
    Q = params.Q
    alpha = params.alpha
    omega_0 = params.omega_0
    t = np.asarray(t, dtype=float)

    if Q > 0.5 + 1e-9:
        # Underdamped (c-regime)
        omega_d = omega_0 * math.sqrt(1.0 - 1.0 / (4.0 * Q * Q))
        return 1.0 - np.exp(-alpha * t) * (
            np.cos(omega_d * t) + (alpha / omega_d) * np.sin(omega_d * t)
        )

    if abs(Q - 0.5) < 1e-9:
        # Critical (s-boundary)
        return 1.0 - (1.0 + alpha * t) * np.exp(-alpha * t)

    # Overdamped (r-regime)
    delta = math.sqrt(alpha * alpha - omega_0 * omega_0)
    r1 = alpha + delta
    r2 = alpha - delta
    return 1.0 - (r2 * np.exp(-r1 * t) - r1 * np.exp(-r2 * t)) / (r2 - r1)


def envelope_form(Q: float) -> str:
    """Qualitative description of the long-time decay envelope.

    cdv1 §Stability's F-003 prediction: the s-boundary (Q = 0.5) decay
    envelope is qualitatively distinct from the c-regime and r-regime
    envelopes. This function names which form applies.
    """
    if Q > 0.5 + 0.02:
        return "exponential_with_ringing"   # e^(-α·t)·oscillation
    if abs(Q - 0.5) <= 0.02:
        return "algebraic_exponential"      # (1 + α·t)·e^(-α·t)
    return "double_exponential"             # sum of two e^(-rᵢ·t), slower mode dominates


def overshoot(params: RLCParameters) -> float:
    """First-peak overshoot above unity for an underdamped step response.

    Returns 0 for Q ≤ 0.5 (no overshoot at or below critical damping).

    Formula: overshoot = exp(-π·ζ / √(1-ζ²)) = exp(-π / √(4Q² - 1))
    """
    if params.Q <= 0.5 + 1e-9:
        return 0.0
    return math.exp(-math.pi / math.sqrt(4.0 * params.Q * params.Q - 1.0))


def algebraic_signature(params: RLCParameters, n_periods: int = 5) -> dict:
    """Measure how much the (1 + α·t) algebraic factor matters in the decay.

    Compares two reconstructions of x(t) over a fixed long-time window:
        A: pure exponential envelope, x̂_pure(t) = 1 - e^(-α·t)
        B: algebraic-exponential envelope, x̂_alg(t) = 1 - (1 + α·t)·e^(-α·t)

    Returns RMS distance of each reconstruction to the true x(t).

    At Q = 0.5, A is wrong and B is exact → B residual is essentially zero,
    A residual is finite. The B/A residual ratio is the F-003 algebraic
    signature.

    At Q > 0.5 (underdamped), the true x oscillates; both A and B miss the
    oscillations, so both residuals are large and the ratio is uninformative.

    At Q < 0.5 (overdamped), the true x is a difference of exponentials;
    neither A nor B captures it correctly, but B's algebraic factor pulls
    toward the slower root. Diagnostic, not diagnostic-of-criticality.

    The clean F-003 read is to compare the residual ratio in a Q-sweep and
    look for a minimum at Q ≈ 0.5.
    """
    omega_0 = params.omega_0
    alpha = params.alpha
    Q = params.Q
    # Sample over n_periods of the natural period.
    t_end = n_periods * (2.0 * math.pi / omega_0)
    t = np.linspace(0.001 / omega_0, t_end, 2000)

    x_true = step_response(params, t)
    x_pure = 1.0 - np.exp(-alpha * t)
    x_alg = 1.0 - (1.0 + alpha * t) * np.exp(-alpha * t)

    rms_pure = float(np.sqrt(np.mean((x_true - x_pure) ** 2)))
    rms_alg = float(np.sqrt(np.mean((x_true - x_alg) ** 2)))

    return {
        "Q": Q,
        "rms_residual_pure_exp": rms_pure,
        "rms_residual_algebraic_exp": rms_alg,
        "ratio_alg_to_pure": rms_alg / rms_pure if rms_pure > 0 else float("nan"),
    }


__all__ = [
    "RLCParameters",
    "rlc_from_Q",
    "step_response",
    "envelope_form",
    "overshoot",
    "algebraic_signature",
]
