# Monte Carlo Estimation of $\pi$

## Overview

Monte Carlo methods provide a stochastic way to solve problems that might be deterministic in principle. Estimating the value of $\pi$ is a classic problem in this domain, often demonstrated using simulations like:

1. **Circle and Square Method:** Simulating random points in a square and checking if they fall inside an inscribed circle.
2. **Buffon's Needle Problem:** Dropping needles on a floor with parallel lines and calculating the probability of crossing a line.

Both methods highlight the power of randomness in approximating mathematical constants.

---

## Python Code Example: Estimating $\pi$ with Monte Carlo

### 1. Circle and Square Method

```python
import numpy as np
import matplotlib.pyplot as plt

# Parameters
total_points = 10000

# Generate random points in a unit square
x = np.random.uniform(-1, 1, total_points)
y = np.random.uniform(-1, 1, total_points)

# Check if points are inside the unit circle
inside_circle = x**2 + y**2 <= 1

# Estimate π
pi_estimate = 4 * np.sum(inside_circle) / total_points

# Visualization
plt.figure(figsize=(8, 8))
plt.scatter(x[inside_circle], y[inside_circle], s=1, color='blue', label="Inside Circle")
plt.scatter(x[~inside_circle], y[~inside_circle], s=1, color='red', label="Outside Circle")
circle = plt.Circle((0, 0), 1, color='black', fill=False)
plt.gca().add_artist(circle)
plt.title(f"Monte Carlo Estimation of π: {pi_estimate:.4f}")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.axis("equal")
plt.grid()
plt.savefig("docs/Mechanics/pic/monte_carlo_circle.png")
plt.show()
```

---

### 2. Buffon's Needle Problem

```python
import numpy as np

# Parameters
needle_length = 1
line_spacing = 2
total_needles = 10000

# Simulate needle drops
theta = np.random.uniform(0, np.pi / 2, total_needles)  # Angle with the horizontal
x_center = np.random.uniform(0, line_spacing / 2, total_needles)  # Distance to nearest line

# Check if needle crosses a line
crosses_line = x_center <= (needle_length / 2) * np.sin(theta)

# Estimate π
pi_estimate = (2 * needle_length * total_needles) / (np.sum(crosses_line) * line_spacing)

# Output
print(f"Monte Carlo Estimation of π using Buffon's Needle: {pi_estimate:.4f}")
```

---

## Key Insights

1. **Randomness and Approximation:** Monte Carlo methods rely on randomness to approximate deterministic quantities. Increasing the number of simulations improves the accuracy of the result.

2. **Circle and Square:** This method illustrates the geometric relationship between a circle and its circumscribing square.

3. **Buffon's Needle:** A classic probabilistic approach linking geometry and probability theory.

---

## Suggested Projects

1. **Accuracy vs. Sample Size:** Analyze how the estimation of $\pi$ improves as the number of points or needles increases.

2. **Higher Dimensions:** Extend the circle and square method to estimate the volume of a hypersphere in higher dimensions.

3. **Visualization Enhancements:** Animate the needle drops or point generation for better understanding.

4. **Statistical Analysis:** Perform multiple runs and compute confidence intervals for the estimated $\pi$.

---

These examples showcase how randomness can uncover mathematical truths. Experiment with these methods and variations to appreciate the elegance of Monte Carlo techniques in estimating $\pi$.
