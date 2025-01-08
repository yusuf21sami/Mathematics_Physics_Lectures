# Lorenz System and Attractor

## Overview

The Lorenz system is a set of three coupled, first-order differential equations that exhibit chaotic behavior for certain parameter values. It was originally derived by Edward Lorenz as a simplified model for atmospheric convection.

The equations are:

$$
\frac{dx}{dt} = \sigma(y - x)
$$

$$
\frac{dy}{dt} = x(\rho - z) - y
$$

$$
\frac{dz}{dt} = xy - \beta z
$$

Where:

- $\sigma$ is the Prandtl number.
- $\rho$ is the Rayleigh number.
- $\beta$ is a geometric factor.

For $\sigma = 10$, $\rho = 28$, and $\beta = 8/3$, the system exhibits chaotic behavior.

---

## Python Code Example: Simulating and Visualizing the Lorenz Attractor

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the Lorenz system
def lorenz(t, state, sigma, rho, beta):
    x, y, z = state
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return [dx_dt, dy_dt, dz_dt]

# Parameters
sigma = 10.0
rho = 28.0
beta = 8 / 3

# Initial conditions
initial_state = [1.0, 1.0, 1.0]

# Time span for the simulation
time_span = (0, 50)
time_eval = np.linspace(time_span[0], time_span[1], 10000)

# Solve the Lorenz system
solution = solve_ivp(lorenz, time_span, initial_state, args=(sigma, rho, beta), t_eval=time_eval, method='RK45')

# Extract the results
x, y, z = solution.y

# Plot the Lorenz attractor
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, lw=0.5)
ax.set_title("Lorenz Attractor")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.savefig("docs/Mechanics/pic/lorenz_attractor.png")
plt.show()
```

---

## Key Insights

1. **Sensitivity to Initial Conditions:**
   Small differences in initial conditions lead to vastly different trajectories over time, a hallmark of chaos.

2. **Attractor Shape:**
   The trajectories form a butterfly-shaped attractor in 3D space.

---

## Suggested Projects

1. **Parameter Exploration:** Study how changing $\sigma$, $\rho$, and $\beta$ affects the system’s behavior.

2. **Lyapunov Exponent:** Quantify the chaos by calculating the Lyapunov exponent of the system.

3. **Comparison with Real Systems:** Compare the Lorenz system to experimental data from fluid dynamics or weather patterns.

4. **3D Visualization:** Use interactive tools like Plotly to explore the attractor dynamically.

---

This example demonstrates the chaotic nature of the Lorenz system. Experiment with the parameters or initial conditions to further explore its dynamics!
