# Duffing Oscillator

## Overview

The Duffing oscillator is a nonlinear second-order differential equation used to model systems with a restoring force that is not purely linear. It has applications in physics, engineering, and even biology.

The equation is:

$$
\ddot{x} + \delta \dot{x} + \alpha x + \beta x^3 = \gamma \cos(\omega t)
$$

Where:
- $x$ is the displacement.
- $\delta$ is the damping coefficient.
- $\alpha$ is the linear stiffness.
- $\beta$ is the nonlinear stiffness.
- $\gamma$ is the amplitude of the driving force.
- $\omega$ is the angular frequency of the driving force.

---

## Python Code Example: Simulating and Visualizing the Duffing Oscillator

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the Duffing oscillator
def duffing(t, state, delta, alpha, beta, gamma, omega):
    x, dx_dt = state
    ddx_dt = -delta * dx_dt - alpha * x - beta * x**3 + gamma * np.cos(omega * t)
    return [dx_dt, ddx_dt]

# Parameters
delta = 0.2  # Damping coefficient
alpha = -1.0  # Linear stiffness
beta = 1.0  # Nonlinear stiffness
gamma = 0.3  # Driving force amplitude
omega = 1.2  # Driving force frequency

# Initial conditions
initial_state = [0.1, 0.0]  # Initial displacement and velocity

# Time span for the simulation
time_span = (0, 100)
time_eval = np.linspace(time_span[0], time_span[1], 10000)

# Solve the Duffing oscillator
solution = solve_ivp(duffing, time_span, initial_state, args=(delta, alpha, beta, gamma, omega), t_eval=time_eval, method='RK45')

# Extract the results
x, dx_dt = solution.y

# Plot the displacement over time
plt.figure(figsize=(12, 6))
plt.plot(solution.t, x, label="Displacement", color="blue")
plt.title("Duffing Oscillator: Displacement Over Time")
plt.xlabel("Time")
plt.ylabel("Displacement")
plt.grid()
plt.legend()
plt.savefig("docs/Mechanics/pic/duffing_time.png")
plt.show()

# Plot the phase plane
plt.figure(figsize=(8, 8))
plt.plot(x, dx_dt, color="purple")
plt.title("Phase Plane of the Duffing Oscillator")
plt.xlabel("Displacement")
plt.ylabel("Velocity")
plt.grid()
plt.savefig("docs/Mechanics/pic/duffing_phase.png")
plt.show()
```

---

## Key Insights

1. **Nonlinear Dynamics:** The cubic term introduces nonlinearity, leading to rich dynamics, including bifurcations and chaos.

2. **Phase Space Behavior:** The phase plane can reveal limit cycles, chaotic attractors, or other patterns depending on parameters.

3. **Driven and Damped System:** The interplay of damping, driving force, and nonlinearity determines the behavior of the oscillator.

---

## Suggested Projects

1. **Bifurcation Analysis:** Vary parameters like $\gamma$ or $\omega$ to explore transitions between different dynamical regimes.

2. **Lyapunov Exponent:** Compute the Lyapunov exponent to identify chaotic regions.

3. **Comparison with Real Systems:** Model physical systems like beam vibrations or electronic circuits.

4. **Energy Analysis:** Study how energy evolves in the system over time, especially in chaotic regimes.

---

This example demonstrates the nonlinear dynamics of the Duffing oscillator. Experiment with parameters and initial conditions to uncover its fascinating behavior!
