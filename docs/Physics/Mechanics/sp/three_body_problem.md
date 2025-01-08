# Three-Body Problem in a Plane

## Overview

The three-body problem is a classical problem in celestial mechanics that describes the motion of three masses under their mutual gravitational attraction. In the planar case, all three bodies move within a single plane.

The equations of motion for each body are derived from Newton's law of gravitation:

$$
\ddot{\vec{r}}_i = G \sum_{j \neq i} m_j \frac{\vec{r}_j - \vec{r}_i}{|\vec{r}_j - \vec{r}_i|^3},
$$

where:
- $\vec{r}_i$ is the position vector of the $i$-th body.
- $m_j$ is the mass of the $j$-th body.
- $G$ is the gravitational constant.

---

## Python Code Example: Simulating and Visualizing the Planar Three-Body Problem

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the equations of motion for the three-body problem
def three_body_equations(t, state, G, m1, m2, m3):
    r1 = state[:2]
    r2 = state[2:4]
    r3 = state[4:6]
    v1 = state[6:8]
    v2 = state[8:10]
    v3 = state[10:12]

    # Distances between bodies
    r12 = np.linalg.norm(r2 - r1)
    r13 = np.linalg.norm(r3 - r1)
    r23 = np.linalg.norm(r3 - r2)

    # Accelerations
    a1 = G * m2 * (r2 - r1) / r12**3 + G * m3 * (r3 - r1) / r13**3
    a2 = G * m1 * (r1 - r2) / r12**3 + G * m3 * (r3 - r2) / r23**3
    a3 = G * m1 * (r1 - r3) / r13**3 + G * m2 * (r2 - r3) / r23**3

    return np.concatenate([v1, v2, v3, a1, a2, a3])

# Parameters
G = 1.0  # Gravitational constant
m1, m2, m3 = 1.0, 1.0, 1.0  # Masses of the three bodies

# Initial positions and velocities (in the plane)
initial_positions = [
    [0.5, 0.0],  # Body 1
    [-0.5, 0.0],  # Body 2
    [0.0, 0.5],   # Body 3
]
initial_velocities = [
    [0.0, 0.1],  # Body 1
    [0.0, -0.1],  # Body 2
    [-0.1, 0.0],  # Body 3
]

# Flatten initial conditions
initial_state = np.concatenate([
    np.array(initial_positions).flatten(),
    np.array(initial_velocities).flatten()
])

# Time span for the simulation
time_span = (0, 10)
time_eval = np.linspace(time_span[0], time_span[1], 1000)

# Solve the equations
solution = solve_ivp(
    three_body_equations, time_span, initial_state, args=(G, m1, m2, m3),
    t_eval=time_eval, method='RK45'
)

# Extract the results
r1 = solution.y[:2].T
r2 = solution.y[2:4].T
r3 = solution.y[4:6].T

# Plot the trajectories
plt.figure(figsize=(10, 10))
plt.plot(r1[:, 0], r1[:, 1], label="Body 1", color="blue")
plt.plot(r2[:, 0], r2[:, 1], label="Body 2", color="red")
plt.plot(r3[:, 0], r3[:, 1], label="Body 3", color="green")
plt.scatter(initial_positions[0][0], initial_positions[0][1], color="blue", marker="o")
plt.scatter(initial_positions[1][0], initial_positions[1][1], color="red", marker="o")
plt.scatter(initial_positions[2][0], initial_positions[2][1], color="green", marker="o")
plt.title("Three-Body Problem Trajectories")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.savefig("docs/Mechanics/pic/three_body_problem.png")
plt.show()
```

---

## Key Insights

1. **Nonlinearity and Chaos:** The three-body problem is highly nonlinear and exhibits sensitive dependence on initial conditions, leading to chaotic trajectories.

2. **Unpredictability:** Long-term predictions of the bodies' positions are inherently limited by numerical precision and initial condition accuracy.

3. **Conservation Laws:** The system conserves total energy and angular momentum, providing useful checks for numerical simulations.

---

## Suggested Projects

1. **Energy Conservation:** Calculate and verify the conservation of total energy throughout the simulation.

2. **Initial Condition Sensitivity:** Explore how small changes in initial positions or velocities affect the trajectories.

3. **Visualization Enhancements:** Create interactive 3D visualizations or add color coding for time progression.

4. **Symmetrical Configurations:** Investigate special cases such as equilateral triangle orbits and their stability.

---

The planar three-body problem is a rich source of nonlinear dynamics and chaos. Experiment with different initial conditions and parameters to explore its fascinating behaviors!
