# Hénon Map

## Overview

The Hénon map is a discrete-time dynamical system that serves as a simple model of chaotic systems. It is defined by a two-dimensional recursive relation:

$$
\begin{align*}
x_{n+1} &= 1 - a x_n^2 + y_n \\
y_{n+1} &= b x_n
\end{align*}
$$

Where:
- $a$ and $b$ are parameters that control the behavior of the system.
- $(x_n, y_n)$ represents the state of the system at iteration $n$.

For the classic values $a = 1.4$ and $b = 0.3$, the map exhibits chaotic behavior and forms a strange attractor.

---

## Python Code Example: Simulating and Visualizing the Hénon Map

```python
import numpy as np
import matplotlib.pyplot as plt

# Define the Hénon map
def henon_map(x, y, a, b):
    x_next = 1 - a * x**2 + y
    y_next = b * x
    return x_next, y_next

# Parameters
a = 1.4
b = 0.3

# Initial conditions
x, y = 0.0, 0.0

# Number of iterations
iterations = 10000

# Store the results
x_values = []
y_values = []

# Iterate the map
for _ in range(iterations):
    x, y = henon_map(x, y, a, b)
    x_values.append(x)
    y_values.append(y)

# Plot the Hénon attractor
plt.figure(figsize=(8, 8))
plt.scatter(x_values, y_values, s=0.1, color="purple")
plt.title("Hénon Map Attractor")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.savefig("docs/Mechanics/pic/henon_map.png")
plt.show()
```

---

## Key Insights

1. **Chaotic Behavior:** The Hénon map is one of the simplest systems to exhibit chaos, making it a foundational model in dynamical systems.

2. **Strange Attractor:** The attractor forms a fractal structure, highlighting the self-similar nature of chaotic systems.

3. **Parameter Sensitivity:** Small changes in $a$ or $b$ can lead to significant differences in the attractor's shape and dynamics.

---

## Suggested Projects

1. **Parameter Exploration:** Investigate how varying $a$ and $b$ affects the attractor's shape and stability.

2. **Fractal Dimension:** Calculate the fractal dimension of the Hénon attractor to quantify its complexity.

3. **Lyapunov Exponent:** Compute the Lyapunov exponent to characterize the map's chaotic nature.

4. **3D Visualization:** Extend the analysis to include a time dimension or color code the points by iteration.

---

This example introduces the chaotic dynamics of the Hénon map. Experiment with different initial conditions and parameters to uncover the fascinating behavior of this simple yet rich system!
