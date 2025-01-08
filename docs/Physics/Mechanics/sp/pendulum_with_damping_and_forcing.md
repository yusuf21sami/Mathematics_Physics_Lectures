# Pendulum with Damping and Forcing

## Overview

The forced damped pendulum is a classic example of a nonlinear dynamic system that exhibits a wide range of behaviors, including periodic motion, quasiperiodicity, and chaos. It is governed by the following equation:

$$
\ddot{\theta} + b \dot{\theta} + c \sin(\theta) = A \cos(\omega t)
$$

Where:
- $\theta$ is the angular displacement.
- $b$ is the damping coefficient.
- $c$ is the gravitational restoring torque coefficient.
- $A$ is the amplitude of the periodic driving force.
- $\omega$ is the angular frequency of the driving force.

---

## Python Code Example: Simulating and Visualizing the Forced Damped Pendulum

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the forced damped pendulum equations
def forced_damped_pendulum(t, state, b, c, A, omega):
    theta, omega_theta = state
    dtheta_dt = omega_theta
    domega_dt = -b * omega_theta - c * np.sin(theta) + A * np.cos(omega * t)
    return [dtheta_dt, domega_dt]

# Parameters
b = 0.5  # Damping coefficient
c = 9.8  # Restoring torque coefficient
A = 1.2  # Amplitude of the driving force
omega = 2.0  # Angular frequency of the driving force

# Initial conditions
initial_state = [0.1, 0.0]  # Initial angle and angular velocity

# Time span for the simulation
time_span = (0, 50)
time_eval = np.linspace(time_span[0], time_span[1], 10000)

# Solve the equations
solution = solve_ivp(forced_damped_pendulum, time_span, initial_state, args=(b, c, A, omega), t_eval=time_eval, method='RK45')

# Extract the results
theta, omega_theta = solution.y

# Unwrap the angle for better visualization
theta = np.unwrap(theta)

# Plot the angular displacement over time
plt.figure(figsize=(12, 6))
plt.plot(solution.t, theta, label="Angular Displacement", color="blue")
plt.title("Forced Damped Pendulum: Angular Displacement Over Time")
plt.xlabel("Time")
plt.ylabel("Angular Displacement (radians)")
plt.grid()
plt.legend()
plt.savefig("docs/Mechanics/pic/forced_damped_pendulum_time.png")
plt.show()

# Plot the phase plane
plt.figure(figsize=(8, 8))
plt.plot(theta, omega_theta, color="purple")
plt.title("Phase Plane of the Forced Damped Pendulum")
plt.xlabel("Angular Displacement (radians)")
plt.ylabel("Angular Velocity")
plt.grid()
plt.savefig("docs/Mechanics/pic/forced_damped_pendulum_phase.png")
plt.show()
```

---

## Key Insights

1. **Nonlinear Dynamics:** The interaction between damping, restoring force, and driving force creates complex dynamics.

2. **Phase Space Behavior:** The phase plane reveals different regimes: limit cycles, quasiperiodic orbits, and chaotic attractors.

3. **Sensitivity to Parameters:** Small changes in $b$, $c$, $A$, or $\omega$ can lead to drastically different behaviors.

---

## Suggested Projects

1. **Parameter Exploration:** Investigate the effects of varying $A$ and $\omega$ to explore transitions between periodic, quasiperiodic, and chaotic motion.

2. **Poincaré Section:** Visualize the system's dynamics using a Poincaré section to identify periodic orbits and chaos.

3. **Energy Analysis:** Study the energy evolution in the system and identify energy dissipation and driving force contributions.

4. **Comparison with Real Pendulums:** Build a physical forced pendulum and compare its motion to the simulation.

---

The forced damped pendulum serves as a rich system for studying nonlinear dynamics. Experiment with the parameters and initial conditions to uncover its fascinating behaviors!
