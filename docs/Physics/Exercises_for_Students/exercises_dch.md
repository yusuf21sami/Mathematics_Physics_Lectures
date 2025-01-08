## Mechanics

### Problem 1

<span style="font-size: 1.2em; font-weight: bold;">Investigating the Range as a Function of the Angle of Projection</span>

#### Motivation:

Projectile motion, while seemingly simple, offers a rich playground for exploring fundamental principles of physics. The problem is straightforward: analyze how the range of a projectile depends on its angle of projection. Yet, beneath this simplicity lies a complex and versatile framework. The equations governing projectile motion involve both linear and quadratic relationships, making them accessible yet deeply insightful.

What makes this topic particularly compelling is the number of free parameters involved in these equations, such as initial velocity, gravitational acceleration, and launch height. These parameters give rise to a diverse set of solutions that can describe a wide array of real-world phenomena, from the arc of a soccer ball to the trajectory of a rocket.

#### Task:

1 **Theoretical Foundation:**

   - Begin by deriving the governing equations of motion from fundamental principles. This involves solving a basic differential equation to establish the general form of the motion.
   - Highlight how variations in initial conditions lead to a family of solutions.

2 **Analysis of the Range:**

   - Investigate how the horizontal range depends on the angle of projection.
   - Discuss how changes in other parameters, such as initial velocity and gravitational acceleration, influence the relationship.

3 **Practical Applications:**

   - Reflect on how this model can be adapted to describe various real-world situations, such as projectiles launched on uneven terrain or in the presence of air resistance.

4 **Implementation:**

   - Develop a computational tool or algorithm to simulate projectile motion.
   - Visualize the range as a function of the angle of projection for different sets of initial conditions.

---

#### Deliverables:

1.  A Markdown document with Python script or notebook implementing the simulations.
2.  A detailed description of the family of solutions derived from the governing equations.
3. Graphical representations of the range versus angle of projection, highlighting how different parameters influence the curve.
4. A discussion on the limitations of the idealized model and suggestions for incorporating more realistic factors, such as drag or wind.

--- 

#### Hints and Resources:

- Start from the fundamental laws of motion and gradually build the general solution.
- Use numerical methods or simulation tools to explore scenarios that go beyond simple analytical solutions.
- Consider how this model connects to real-world systems, such as sports, engineering, and astrophysics.

This task encourages a deep understanding of projectile motion while showcasing its versatility and applicability across various domains.

### Problem 2 

<span style="font-size: 1.2em; font-weight: bold;">**Investigating the Dynamics of a Forced Damped Pendulum**</span>

#### Motivation:

The forced damped pendulum is a captivating example of a physical system with intricate behavior resulting from the interplay of damping, restoring forces, and external driving forces. By introducing both damping and external periodic forcing, the system demonstrates a transition from simple harmonic motion to a rich spectrum of dynamics, including resonance, chaos, and quasiperiodic behavior. These phenomena serve as a foundation for understanding complex real-world systems, such as driven oscillators, climate systems, and mechanical structures under periodic stress.

Adding forcing introduces new parameters, such as the amplitude and frequency of the external force, which significantly affect the pendulum's behavior. By systematically varying these parameters, a diverse class of solutions can be observed, including synchronized oscillations, chaotic motion, and resonance phenomena. These behaviors not only highlight fundamental physics principles but also provide insights into engineering applications such as energy harvesting, vibration isolation, and mechanical resonance.

#### Task:

1 **Theoretical Foundation:**

   - Start with the differential equation governing the motion of a forced damped pendulum:

     $\frac{d^2\theta}{dt^2} + b\frac{d\theta}{dt} + \frac{g}{L}\sin\theta = A\cos(\omega t)$

   - Derive the approximate solutions for small-angle oscillations.
   - Explore resonance conditions and their implications for the system's energy.

2 **Analysis of Dynamics:**

   - Investigate how the damping coefficient, driving amplitude, and driving frequency influence the motion of the pendulum.
   - Examine the transition between regular and chaotic motion and their physical interpretations.

3 **Practical Applications:**

   - Discuss real-world scenarios where the forced damped pendulum model applies, such as in energy harvesting devices, suspension bridges, and oscillating circuits.

4 **Implementation:**

   - Create a computational model to simulate the motion of a forced damped pendulum.
   - Visualize the behavior under various damping, driving force, and initial conditions.
   - Plot phase diagrams and Poincaré sections to illustrate transitions to chaos.

---

#### Deliverables:

1.  A Markdown document with Python script or notebook implementing the simulations.
2.  A detailed explanation of the general solutions for the forced damped pendulum.
3. Graphical representations of the motion for different damping coefficients, driving amplitudes, and driving frequencies, including resonance and chaotic behavior.
4. A discussion on the limitations of the model and potential extensions, such as introducing nonlinear damping or non-periodic driving forces.
5. Phase portraits, Poincaré sections, and bifurcation diagrams to analyze transitions to complex dynamics.

---

#### Hints and Resources:

- For small angles, approximate $\sin\theta \approx \theta$ to simplify the differential equation.
- Employ numerical techniques (e.g., Runge-Kutta methods) for exploring the dynamics beyond the small-angle approximation.
- Relate the forced damped pendulum to analogous systems in other fields, such as electrical circuits (driven RLC circuits) or biomechanics (human gait).
- Utilize software tools like Python for simulations and visualizations.

This task bridges theoretical analysis with computational exploration, fostering a deeper understanding of forced and damped oscillatory phenomena and their implications in both physics and engineering.

## Gravity

### Problem 1

<span style="font-size: 1.2em; font-weight: bold;">Orbital Period and Orbital Radius</span>

#### Motivation:

The relationship between the square of the orbital period and the cube of the orbital radius, known as Kepler's Third Law, is a cornerstone of celestial mechanics. This simple yet profound relationship allows for the determination of planetary motions and has implications for understanding gravitational interactions on both local and cosmic scales. By analyzing this relationship, one can connect fundamental principles of gravity with real-world phenomena such as satellite orbits and planetary systems.

#### Task:

1. Derive the relationship between the square of the orbital period and the cube of the orbital radius for circular orbits.
2. Discuss the implications of this relationship for astronomy, including its role in calculating planetary masses and distances.
3. Analyze real-world examples, such as the Moon's orbit around Earth or the orbits of planets in the Solar System.
4. Implement a computational model to simulate circular orbits and verify the relationship.

---

#### Deliverables:

1. A Markdown document with Python script or notebook implementing the simulations.
2. A detailed explanation of the subjects.
3. Graphical representations of circular orbits and the relationship between orbital period and radius.
4. A discussion on how this relationship extends to elliptical orbits and other celestial bodies.
 
### Problem 2

<span style="font-size: 1.2em; font-weight: bold;">Escape Velocities and Cosmic Velocities</span>

#### Motivation:

The concept of escape velocity is crucial for understanding the conditions required to leave a celestial body's gravitational influence. Extending this concept, the first, second, and third cosmic velocities define the thresholds for orbiting, escaping, and leaving a star system. These principles underpin modern space exploration, from launching satellites to interplanetary missions.

#### Task:

1. Define the first, second, and third cosmic velocities, explaining their physical meaning.
2. Analyze the mathematical derivations and parameters affecting these velocities.
3. Calculate and visualize these velocities for different celestial bodies like Earth, Mars adn Jupyter.
4. Discuss their importance in space exploration, including launching satellites, missions to other planets, and potential interstellar travel.

---

#### Deliverables:

1. A Markdown document with Python script or notebook implementing the simulations.
2. A detailed explanation of the subjects.
3. Graphical representations of escape velocities and cosmic velocities for various celestial bodies.

### Problem 3


<span style="font-size: 1.2em; font-weight: bold;">Trajectories of a Freely Released Payload Near Earth</span>

#### Motivation:

When an object is released from a moving rocket near Earth, its trajectory depends on initial conditions and gravitational forces. This scenario presents a rich problem, blending principles of orbital mechanics and numerical methods. Understanding the potential trajectories is vital for space missions, such as deploying payloads or returning objects to Earth.

#### Task:

1. Analyze the possible trajectories (e.g., parabolic, hyperbolic, elliptical) of a payload released near Earth.
2. Perform a numerical analysis to compute the path of the payload based on given initial conditions (position, velocity, and altitude).
3. Discuss how these trajectories relate to orbital insertion, reentry, or escape scenarios.
4. Develop a computational tool to simulate and visualize the motion of the payload under Earth's gravity, accounting for initial velocities and directions.

---

#### Hints and Resources:

- Use fundamental gravitational principles, such as Newton's Law of Gravitation and Kepler's Laws, to derive equations and analyze scenarios.
- Leverage numerical methods or software tools (e.g., Python) to simulate orbits and trajectories.
- Explore real-world applications, such as space mission planning, satellite deployment, and planetary exploration.

These tasks provide a foundation for understanding gravity's influence on motion and its role in celestial mechanics and space exploration.

#### Deliverables:

1. A Markdown document with Python script or notebook implementing the simulations.
2. A detailed explanation of the subjects.
3. Graphical representations of orbital trajectories, escape velocities, and payload trajectories near Earth.

## Waves

### Problem 1

<span style="font-size: 1.2em; font-weight: bold;">Interference Patterns on a water surface</span>

#### Motivation:

Interference occurs when waves from different sources overlap, creating new patterns. On a water surface, this can be easily observed when ripples from different points meet, forming distinctive interference patterns. These patterns can show us how waves combine in different ways, either reinforcing each other or canceling out.

Studying these patterns helps us understand wave behavior in a simple, visual way. It also allows us to explore important concepts, like the relationship between wave phase and the effects of multiple sources. This task offers a hands-on approach to learning about wave interactions and their real-world applications, making it an interesting and engaging way to dive into wave physics.

#### Task

A circular wave on the water surface, emanating from a point source located at $(x_0, y_0)$, can be described by the Single Disturbance equation:

$$
\eta(x, y, t) = \frac{A}{\sqrt{r}} \cdot \cos\left(kr - \omega t + \phi\right)
$$

where:

- $\eta(x, y, t)$ is the displacement of the water surface at point $(x, y)$ and time $t$,
- $A$ is the amplitude of the wave,
- $k = \frac{2\pi}{\lambda}$ is the wave number, related to the wavelength $\lambda$,
- $\omega = 2\pi f$ is the angular frequency, related to the frequency $f$,
- $r = \sqrt{(x - x_0)^2 + (y - y_0)^2}$ is the distance from the source to the point $(x, y)$,
- $\phi$ is the initial phase.

#### Problem Statement:

Your task is to analyze the interference patterns formed on the water surface due to the superposition of waves emitted from point sources placed at the vertices of a chosen regular polygon.

#### Steps to Follow:

1. **Select a Regular Polygon:** Choose a regular polygon (e.g., equilateral triangle, square, regular pentagon).

2. **Position the Sources:** Place point wave sources at the vertices of the selected polygon.

3. **Wave Equations:** Write the equations describing the waves emitted from each source, considering their respective positions.

4. **Superposition of Waves:** Apply the principle of superposition by summing the wave displacements at each point on the water surface:

   $$
   \eta_{\text{sum}}(x, y, t) = \sum_{i=1}^{N} \eta_i(x, y, t)
   $$

   where $N$ is the number of sources (vertices of the polygon).

5. **Analyze Interference Patterns:** Examine the resulting displacement $\eta_{\text{sum}}(x, y, t)$ as a function of position $(x, y)$ and time $t$. Identify regions of constructive interference (wave amplification) and destructive interference (wave cancellation).

6. **Visualization:** Present your findings graphically, illustrating the interference patterns for the chosen regular polygon.

#### Considerations:

- Assume all sources emit waves with the same amplitude $A$, wavelength $\lambda$, and frequency $f$.
- The waves are coherent, maintaining a constant phase difference.
- You may use simulation and visualization tools such as Python (with libraries like Matplotlib), or other graphical software to aid in your analysis.

#### Deliverables:

1. A Markdown document with Python script or notebook implementing the simulations.
2. A detailed explanation of the interference patterns observed for the chosen regular polygon with the goal of understanding wave superposition.
3. Graphical representations of the water surface showing constructive and destructive interference regions.

## Circuits

### Problem 1

<span style="font-size: 1.2em; font-weight: bold;">Equivalent Resistance Using Graph Theory</span>

#### Motivation:

Calculating equivalent resistance is a fundamental problem in electrical circuits, essential for understanding and designing efficient systems. While traditional methods involve iteratively applying series and parallel resistor rules, these approaches can become cumbersome for complex circuits with many components. Graph theory offers a powerful alternative, providing a structured and algorithmic way to analyze circuits.

By representing a circuit as a graph—where nodes correspond to junctions and edges represent resistors with weights equal to their resistance values—we can systematically simplify even the most intricate networks. This method not only streamlines calculations but also opens the door to automated analysis, making it particularly useful in modern applications like circuit simulation software, optimization problems, and network design.

Studying equivalent resistance through graph theory is valuable not only for its practical applications but also for the deeper insights it provides into the interplay between electrical and mathematical concepts. This approach highlights the versatility of graph theory, demonstrating its relevance across physics, engineering, and computer science.

---

#### Task Options:

##### **Option 1: Simplified Task – Algorithm Description**

1. Describe the algorithm for calculating the equivalent resistance using graph theory.

2. Provide the pseudocode that:

    - Identifies series and parallel connections.
    - Iteratively reduces the graph until a single equivalent resistance is obtained.

3. Include a clear explanation of how the algorithm handles nested combinations.

##### **Option 2: Advanced Task – Full Implementation**

1. Implement the algorithm in a programming language of your choice.

2. Ensure the implementation:

    - Accepts a circuit graph as input.
    - Handles arbitrary resistor configurations, including nested series and parallel connections.
    - Outputs the final equivalent resistance.

3. Test your implementation with examples, such as:

    - Simple series and parallel combinations.
    - Nested configurations.
    - Complex graphs with multiple cycles.

---
#### Deliverables:

- A detailed pseudocode (but preferably a full implementation) and explanation of the algorithm.
- Description of how it handles complex circuit configurations on three input examples.
- A brief analysis of the algorithm's efficiency and potential improvements.

---

#### Hints and Resources:

* Focus on iterative graph simplification:
    - Detect linear chains for series reduction.
    - Identify cycles for parallel reduction.
* Use tools like `networkx` (Python) or similar for graph manipulation if you choose implementation.
* Depth-first search (DFS) or other traversal methods can help identify patterns in the graph.

Choose the task that matches your skill level while providing a clear and structured solution to the problem.

## Electromangetism

### Problem 1

<span style="font-size: 1.2em; font-weight: bold;">**Simulating the effects of the Lorentz Force**</span>

#### Motivation:

The Lorentz force, expressed as $\mathbf{F} = q\mathbf{E} + q\mathbf{v} \times \mathbf{B}$, governs the motion of charged particles in electric and magnetic fields. It is foundational in fields like plasma physics, particle accelerators, and astrophysics. By focusing on simulations, we can explore the practical applications and visualize the complex trajectories that arise due to this force.

#### Task:

1 **Exploration of Applications:**

   - Identify systems where the Lorentz force plays a key role (e.g., particle accelerators, mass spectrometers, plasma confinement).
   - Discuss the relevance of electric ($\mathbf{E}$) and magnetic ($\mathbf{B}$) fields in controlling the motion of charged particles.

2 **Simulating Particle Motion:**

   - Implement a simulation to compute and visualize the trajectory of a charged particle under:
     - A uniform magnetic field.
     - Combined uniform electric and magnetic fields.
     - Crossed electric and magnetic fields.
   - Simulate the particle’s circular, helical, or drift motion based on initial conditions and field configurations.

3 **Parameter Exploration:**

   - Allow variations in:
     - Field strengths ($E$, $B$).
     - Initial particle velocity ($\mathbf{v}$).
     - Charge and mass of the particle ($q$, $m$).
   - Observe how these parameters influence the trajectory.

4 **Visualization:**

   - Create clear, labeled plots showing the particle’s path in 2D and 3D for different scenarios.
   - Highlight physical phenomena such as the Larmor radius and drift velocity.

---

#### Deliverables:

1. A Markdown document with Python script or notebook implementing the simulations.
2. Visualizations of particle trajectories for the specified field configurations.
3. A discussion on how the results relate to practical systems, such as cyclotrons or magnetic traps.

---

#### Hints and Resources:

- Use numerical methods like the Euler or Runge-Kutta method to solve the equations of motion
- Employ Python libraries such as NumPy for calculations and Matplotlib for visualizations.
- Start with simple cases (e.g., uniform magnetic field) and gradually add complexity (e.g., crossed fields).

This task focuses on applying the Lorentz force concept through simulations, enabling an intuitive understanding of its effects in real-world scenarios.

#### Deliverables:

1. A Markdown document with Python script or notebook implementing the simulations.
2. Visualizations of particle trajectories for the specified field configurations.
3. A discussion on how the results relate to practical systems, such as cyclotrons or magnetic traps.
4. Suggestions for extending the simulation to more complex scenarios, such as non-uniform fields.

## Statistics

### Problem 1

<span style="font-size: 1.2em; font-weight: bold;">**Exploring the Central Limit Theorem through simulations**</span>

#### Motivation:

The Central Limit Theorem (CLT) is a cornerstone of probability and statistics, stating that the sampling distribution of the sample mean approaches a normal distribution as the sample size increases, regardless of the population’s original distribution. Simulations provide an intuitive and hands-on way to observe this phenomenon in action.

#### Task:

1 **Simulating Sampling Distributions:**

   - Select several types of population distributions, such as:
     - Uniform distribution.
     - Exponential distribution.
     - Binomial distribution.
   - For each distribution, generate a large dataset representing the population.

2 **Sampling and Visualization:**

   - Randomly sample data from the population and calculate the sample mean for different sample sizes (e.g., 5, 10, 30, 50).
   - Repeat the process multiple times to create a sampling distribution of the sample mean.
   - Plot histograms of the sample means for each sample size and observe the convergence to a normal distribution.

3 **Parameter Exploration:**

   - Investigate how the shape of the original distribution and the sample size influence the rate of convergence to normality.
   - Highlight the impact of the population’s variance on the spread of the sampling distribution.

4 **Practical Applications:**

   - Reflect on the importance of the CLT in real-world scenarios, such as:
     - Estimating population parameters.
     - Quality control in manufacturing.
     - Predicting outcomes in financial models.

---

#### Deliverables:

1. A Markdown document and Python scripts or notebooks implementing the simulations for various population distributions.
2. Plots illustrating the sampling distributions and their progression toward normality.
3. A discussion on the implications of the results and their connection to theoretical expectations.

---

#### Hints and Resources:

- Use Python libraries such as NumPy for random number generation and Matplotlib/Seaborn for visualization.
- Begin with simple populations (e.g., uniform or normal) before exploring more complex distributions.
- Ensure students understand how to calculate and interpret the sample mean and variance.

This task encourages students to explore the Central Limit Theorem through computational experiments, deepening their understanding of its significance in statistics.

### Problem 2

<span style="font-size: 1.2em; font-weight: bold;">**Estimating Pi using Monte Carlo Methods**</span>

#### Motivation:

Monte Carlo simulations are a powerful class of computational techniques that use randomness to solve problems or estimate values. One of the most elegant applications of Monte Carlo methods is estimating the value of $\pi$ through geometric probability. By randomly generating points and analyzing their positions relative to a geometric shape, we can approximate $\pi$ in an intuitive and visually engaging way.

This problem connects fundamental concepts of probability, geometry, and numerical computation. It also provides a gateway to understanding how randomness can be harnessed to solve complex problems in physics, finance, and computer science. The Monte Carlo approach to $\pi$ estimation highlights the versatility and simplicity of this method while offering practical insights into convergence rates and computational efficiency.

---

#### Task

##### Part 1: Estimating $\pi$ Using a Circle

1 **Theoretical Foundation:**

   - Explain how the ratio of points inside a circle to the total number of points in a square can be used to estimate $\pi$.
   - Derive the formula $\pi \approx 4 \cdot (\text{points inside the circle} / \text{total points})$ for a unit circle.

2 **Simulation:**

   - Generate random points in a 2D square bounding a unit circle.
   - Count the number of points falling inside the circle.
   - Estimate $\pi$ based on the ratio of points inside the circle to the total points.

3 **Visualization:**

   - Create a plot showing the randomly generated points, distinguishing those inside and outside the circle.

4 **Analysis:**

   - Investigate how the accuracy of the estimate improves as the number of points increases.
   - Discuss the convergence rate and computational considerations for this method.

---

##### Part 2: Estimating $\pi$ Using Buffon’s Needle

1 **Theoretical Foundation:**

   - Describe Buffon’s Needle problem, where $\pi$ can be estimated based on the probability of a needle crossing parallel lines on a plane.
   - Derive the formula $\pi \approx (2 \cdot \text{needle length} \cdot \text{number of throws}) / (\text{distance between lines} \cdot \text{number of crossings})$.

2 **Simulation:**

   - Simulate the random dropping of a needle on a plane with parallel lines.
   - Count the number of times the needle crosses a line.
   - Estimate $\pi$ based on the derived formula.

3 **Visualization:**

   - Create a graphical representation of the simulation, showing the needle positions relative to the lines.

4 **Analysis:**

   - Explore how the number of needle drops affects the estimate’s accuracy.
   - Compare the convergence rate of this method to the circle-based approach.

---

#### Deliverables

1 A Markdown document with:

   - Clear explanations of the methods and formulas.
   - A discussion of theoretical foundations and results.

2 Python scripts or notebooks implementing the simulations, including:

   - Code for the circle-based Monte Carlo method.
   - Code for the Buffon’s Needle method.

3 Graphical outputs:

   - Plots showing random points for the circle-based method.
   - Visualizations of needle positions for Buffon’s Needle.

4 Analysis:

   - Tables or graphs showing the convergence of estimated $\pi$ as a function of the number of iterations for both methods.
   - A comparison of the methods in terms of accuracy and computational efficiency.

---

#### Hints and Resources

- Use Python libraries such as NumPy for random number generation and Matplotlib for visualizations.
- For the circle-based method, ensure the random points are uniformly distributed within the square.
- For Buffon’s Needle, pay attention to geometric constraints, such as the relationship between the needle length and the distance between lines.
- Start with a small number of iterations to validate the implementation, then increase the sample size to observe convergence.

## Measurements

### Problem 1

<span style="font-size: 1.2em; font-weight: bold;">**Measuring Earth's Gravitational Acceleration with a Pendulum**</span>

#### Motivation:

The acceleration $g$ due to gravity is a fundamental constant that influences a wide range of physical phenomena. Measuring $g$ accurately is crucial for understanding gravitational interactions, designing structures, and conducting experiments in various fields. One classic method for determining $g$ is through the oscillations of a simple pendulum, where the period of oscillation depends on the local gravitational field.

#### Task:

Measure the acceleration  $g$ due to gravity using a pendulum and in details analyze the uncertainties in the measurements.

This exercise emphasizes rigorous measurement practices, uncertainty analysis, and their role in experimental physics.

---

#### **Procedure:**

1 **Materials:**
   
   - A string (1 or 1.5 meters long).
   - A small weight (e.g., bag of coins, bag of sugar, key chain) mounted on the string.
   - Stopwatch (or smartphone timer).
   - Ruler or measuring tape.

2 **Setup:**
   
   - Attach the weight to the string and fix the other end to a sturdy support.
   - Measure the length of the pendulum, $L$, from the suspension point to the center of the weight using a ruler or measuring tape. Record the resolution of the measuring tool and calculate the uncertainty as half the resolution $\Delta L=\text{(Ruler Resolution)}/2$.

3 **Data Collection:**
   
   - Displace the pendulum slightly (<15°) and release it.
   - Measure the time for 10 full oscillations ($T_{10}$) and repeat this process 10 times. Record all 10 measurements.
   - Calculate the mean time for 10 oscillations ($\overline{T}_{10}$) and the standard deviation ($\sigma_T$).
   - Determine the uncertainty in the mean time as:
     $$ \Delta T_{10} = \frac{\sigma_T}{\sqrt{n}} $$
     where $n = 10$.

---

#### **Calculations:**

1 **Calculate the period:**

   $T = \frac{\overline{T}_{10}}{10}$ and $\Delta T = \frac{\Delta T_{10}}{10}$

2 **Determine $g$:**

   $g = \frac{4\pi^2 L}{T^2}$

3 **Propagate uncertainties:**

   $\Delta g = g \sqrt{\left(\frac{\Delta L}{L}\right)^2 + \left(2\frac{\Delta T}{T}\right)^2}$

---

#### **Analysis:**

1 Compare your measured $g$ with the standard value ($9.81 \, \text{m/s}^2$).

2 Discuss:

   - The effect of measurement resolution on $\Delta L$.
   - Variability in timing and its impact on $\Delta T$.
   - Any assumptions or experimental limitations.

---

#### **Deliverables:**

1 Tabulated data in markdown:

   - $L$, $\Delta L$, $T_{10}$ measurements, $\overline{T}_{10}$, $\sigma_T$, $\Delta T$.
   - Calculated $g$ and $\Delta g$.
  
2 The discussion on sources of uncertainty and their impact on the results.