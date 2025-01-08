# Lotka-Volterra Equations (Predator-Prey Model)

## Overview

The Lotka-Volterra equations are a pair of first-order, non-linear differential equations frequently used to describe the dynamics of biological systems in which two species interact, one as a predator and the other as prey.

The equations are:

$$
\frac{dx}{dt} = \alpha x - \beta xy
$$

$$
\frac{dy}{dt} = \delta xy - \gamma y
$$

Where:

- $x$ is the population of the prey.
- $y$ is the population of the predator.
- $\alpha$ is the growth rate of the prey.
- $\beta$ is the rate at which predators consume prey.
- $\gamma$ is the death rate of the predators.
- $\delta$ is the rate at which predators increase by consuming prey.

---

## Python Code Example: Simulating and Visualizing the Lotka-Volterra Equations

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the Lotka-Volterra equations
def lotka_volterra(t, state, alpha, beta, gamma, delta):
    x, y = state
    dx_dt = alpha * x - beta * x * y
    dy_dt = delta * x * y - gamma * y
    return [dx_dt, dy_dt]

# Parameters
alpha = 0.1  # Prey growth rate
beta = 0.02  # Predator consumption rate
gamma = 0.3  # Predator death rate
delta = 0.01  # Predator reproduction rate

# Initial conditions
initial_state = [40, 9]  # Initial populations of prey and predator

# Time span for the simulation
time_span = (0, 200)
time_eval = np.linspace(time_span[0], time_span[1], 1000)

# Solve the Lotka-Volterra equations
solution = solve_ivp(lotka_volterra, time_span, initial_state, args=(alpha, beta, gamma, delta), t_eval=time_eval, method='RK45')

# Extract the results
prey, predator = solution.y

# Plot the populations over time
plt.figure(figsize=(12, 6))
plt.plot(solution.t, prey, label="Prey Population", color="blue")
plt.plot(solution.t, predator, label="Predator Population", color="red")
plt.title("Lotka-Volterra Predator-Prey Model")
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend()
plt.grid()
plt.savefig("docs/Mechanics/pic/lotka_volterra_time.png")
plt.show()

# Plot the phase plane
plt.figure(figsize=(8, 8))
plt.plot(prey, predator, color="purple")
plt.title("Phase Plane of the Lotka-Volterra Model")
plt.xlabel("Prey Population")
plt.ylabel("Predator Population")
plt.grid()
plt.savefig("docs/Mechanics/pic/lotka_volterra_phase.png")
plt.show()
```

---

## Key Insights

1. **Oscillatory Behavior:** The populations of prey and predators tend to oscillate over time, with predator peaks lagging behind prey peaks.

2. **Phase Plane:** The phase plane reveals closed orbits, indicating periodic solutions depending on initial conditions.

3. **Nonlinearity:** The interaction terms ($\beta xy$ and $\delta xy$) introduce nonlinearity, leading to complex dynamics.

---

## Suggested Projects

1. **Parameter Sensitivity:** Investigate how varying $\alpha$, $\beta$, $\gamma$, and $\delta$ affects the dynamics.

2. **Stability Analysis:** Analyze the stability of the fixed points to understand long-term behavior.

3. **Real-World Data:** Fit the Lotka-Volterra model to real-world predator-prey data to evaluate its applicability.

4. **Extensions:** Add additional species or environmental factors to study more complex ecosystems.

---

This example provides a basic introduction to the predator-prey dynamics described by the Lotka-Volterra equations. Experiment with different parameters and initial conditions to observe the rich behavior of this classic model.
