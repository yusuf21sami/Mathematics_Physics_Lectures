# Chua's Circuit

## Overview

Chua's Circuit is a simple electronic circuit that exhibits a wide range of nonlinear dynamics, including chaos. It is a physical realization of a chaotic system and has applications in studying nonlinear dynamics and chaos theory.

The equations describing Chua's circuit are:

$$
\frac{dx}{dt} = \alpha (y - x - h(x))
$$

$$
\frac{dy}{dt} = x - y + z
$$

$$
\frac{dz}{dt} = -\beta y
$$

Where:

- $h(x)$ is a piecewise-linear function that models the nonlinear resistance (Chua's diode):
  $$ h(x) = m_1 x + 0.5 (m_0 - m_1) (|x + 1| - |x - 1|) $$
- $\alpha$, $\beta$, $m_0$, and $m_1$ are parameters defining the circuit's behavior.

---

## Python Code Example: Simulating and Visualizing Chua's Circuit

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the piecewise-linear function h(x)
def chua_diode(x, m0, m1):
    return m1 * x + 0.5 * (m0 - m1) * (np.abs(x + 1) - np.abs(x - 1))

# Define the system of equations for Chua's Circuit
def chua_circuit(t, state, alpha, beta, m0, m1):
    x, y, z = state
    dx_dt = alpha * (y - x - chua_diode(x, m0, m1))
    dy_dt = x - y + z
    dz_dt = -beta * y
    return [dx_dt, dy_dt, dz_dt]

# Parameters
alpha = 9.0
beta = 14.286
m0 = -1.143
m1 = -0.714

# Initial conditions
initial_state = [0.7, 0.0, 0.0]  # Initial values for x, y, z

# Time span for the simulation
time_span = (0, 50)
time_eval = np.linspace(time_span[0], time_span[1], 10000)

# Solve the equations
solution = solve_ivp(chua_circuit, time_span, initial_state, args=(alpha, beta, m0, m1), t_eval=time_eval, method='RK45')

# Extract the results
x, y, z = solution.y

# Plot the attractor in 3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, lw=0.5)
ax.set_title("Chua's Circuit Attractor")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.savefig("docs/Mechanics/pic/chua_attractor.png")
plt.show()
```

---

## Key Insights

1. **Chaos in Electronics:** Chua's circuit is a tangible demonstration of chaos, allowing theoretical predictions to be experimentally verified.

2. **Piecewise Nonlinearity:** The nonlinear resistor introduces the nonlinearity needed for chaotic behavior.

3. **Rich Dynamics:** Depending on the parameters, the circuit exhibits periodic, quasiperiodic, or chaotic behavior.

---

## Suggested Projects

1. **Parameter Exploration:** Investigate how varying $\alpha$, $\beta$, $m_0$, and $m_1$ affects the dynamics.

2. **Lyapunov Exponent:** Compute the Lyapunov exponent to quantify chaos in the circuit.

3. **Physical Implementation:** Build Chua's circuit with real electronic components and compare the experimental results with simulations.

4. **Fractal Dimension:** Calculate the fractal dimension of the attractor to understand its complexity.

---

Chua's Circuit provides a fascinating look into chaos and nonlinear dynamics. Experiment with the parameters and initial conditions to explore its rich behavior!
