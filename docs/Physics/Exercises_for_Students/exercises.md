## Mechanics

### Problem 1

Discuss the problem of projectile motion. Investigate the dependence of the range on the angle of projection.

### Problem 2

Analyze the dynamics of a damped pendulum.

## Gravity

### Problem 1

Analyze the relationship between the square of the orbital period and the cube of the orbital radius in circular motion, and discuss its implications for astronomy.

### Problem 2

Discuss the concept of escape velocities. Define and analyze the first, second, and third cosmic velocities, and their importance in space exploration.

### Problem 3

Analyze the concept of gravitational slingshot (gravity assist). Explain how spacecraft can use the gravity of celestial bodies to change their trajectory and velocity. Discuss its practical applications in interplanetary missions.

## Waves

Describe the difference between transverse and longitudinal waves, as well as the relationship between wave velocity, frequency, and wavelength. Show three **interesting** examples of adding of waves with various wavelenghts and amplitudes. Can two speakers can produce a silence?

Describe the Doppler Effect for the observed frequency in terms of the velocities of the source and observer. Demonstate various configurations of waves Doppler Effect.

## Electricity and Magnetism

Examine the concept of an electric field. Describe the principle of superposition for electric fields and illustrate it with an example involving multiple point charges.

Analyze the relationship between electric potential and electric field. Derive the expression for the electric field as the gradient of the potential and discuss its physical implications.

Investigate the Lorentz force acting on a charged particle in both electric and magnetic fields. Explain the equation for the force and discuss its applications, such as in cyclotrons and mass spectrometers.

Analyze the relationship between electric currents and magnetic fields. Derive the expression for the magnetic field produced by a current-carrying wire. Describe the forces appearing on a current-carrying wires going in the same or opposite directions. Exlain the right-hand rule, Lenz's Law, and the Biot-Savart Law.

Discuss the principles of electromagnetic induction. Derive Faraday's Law and explain its practical applications, such as in electric generators and transformers.

Examine Maxwell's equations. Highlight their significance in unifying electricity and magnetism and their role in predicting the existence of electromagnetic waves.

## Circuits

- Describe difference between series and parallel circuits applied to restitors and capacitors. Using some example complex circuits, **demonstrate** how to simplify it into a single equivalent value of resistor or capacitor using series-parallel transformations. Is there possible algorithm for computing equivalent resistance or capacitance? 

- Describe Kirchhoff’s Current Law (KCL) and Voltage Law (KVL). **Solve a circuit problem** involving multiple loops and junctions, illustrating the use of these laws.

- Analyze the time evolution of current $I(t)$ and voltage in RL and RC and RLC circuits.

---

Using Ohm’s Law, analyze the relationship between voltage, current, and resistance.

Explain the working principles of capacitors and inductors. Derive the formulas for total capacitance and inductance in series and parallel circuits, and discuss their applications in electronic devices.

Explain the differences between Alternating Current (AC) and Direct Current (DC). Derive the formulas for root mean square (RMS) voltage and current, and discuss their significance in AC circuits.

Analyze the concept of the PN junction in semiconductors. Describe the formation of the depletion zone and its role in controlling current flow.

Explain the working principles of diodes and transistors. Discuss the differences between NPN and PNP transistors and their applications in amplification and switching circuits.

Give the formulas for impedance in resistive, inductive, and capacitive elements, and analyze their behavior in series and parallel configurations.

Analyze the concept of electrical resonance in RLC circuits. Derive the formula for the resonant frequency and discuss the behavior of current and voltage at resonance.

## Measurements

Examine the principles of measurement systems. Discuss the concepts of accuracy, precision, and resolution, and analyze the sources of errors in measurements.

- Discuss the concept of total uncertainty in measurements using total derivative method. Analyze the methods for combining uncertainties in measurements and calculating the overall uncertainty of a result. Demonstrate it by computing resistance using by ammeter and voltmeter.

## Statistics

Discuss the concepts of mean, median, standard deviation and variance as measures of dispersion in data analysis. Provide the formulas for calculating these statistical parameters and discuss their significance.

Discuss the graphical representation of data using histograms, box plots, and scatter plots and error bars. Analyze the characteristics of these plots and their applications in visualizing data distributions and relationships.

Analyze the principles of linear regression in data analysis. Derive the formula for the regression line and discuss its use in predicting the values of dependent variables based on independent variables.

## Modern Physics I

Analyze the life cycle of stars, starting from their formation in nebulae to their evolution into white dwarfs, neutron stars, or black holes. Discuss the role of nuclear fusion in powering stars and the processes of stellar nucleosynthesis.

Discuss the principles of special relativity, focusing on the concepts of constant light speed, time dilation and length contraction. Derive the formulas for these phenomena and discuss their applications, such as GPS satellite systems and muon decay.

Describe the Lorentz transformation equations, and explain how they relate space and time coordinates between inertial frames moving at relativistic speeds.

Use Hubble's Law to calculate the velocity of a galaxy located 200 megaparsecs (Mpc) away, assuming a Hubble constant of 70 km/s/Mpc.

Explain the Big Bang Theory and its key evidence, including the Cosmic Microwave Background (CMB) radiation. Discuss the significance of primordial nucleosynthesis in explaining the abundance of light elements in the universe.

## Modern Physics II

Discuss the Bohr model of the atom and its application to the hydrogen spectrum. Give the expression for the quantized energy levels of the hydrogen atom and explain the significance of the Rydberg formula.

P: Find all colors of light emitted by hydrogen atom when electron transitions from higher energy level to lower energy level (hint: there are 4 possible transitions).

Describe the phenomenon of wave-particle duality. Use Young's Double-Slit Experiment to illustrate how particles such as electrons exhibit both wave-like and particle-like behavior.

Explain the Heisenberg Uncertainty Principle and discuss its implications for the simultaneous measurement of position and momentum. Provide an example demonstrating the calculation of uncertainty in momentum when the uncertainty in position is known.

Discuss the principles of quantum mechanics, including wave functions, probability amplitudes, and the Schrödinger equation.

Analyze the behavior of particles in potential wells and barriers, and explain the concept of quantum tunneling.
Explain the concept of wavefunction normalization. For a given wavefunction $\psi(x) = A e^{-x^2}$, determine the normalization constant $A$ over the range $x \in (-\infty, \infty)$ and in another range $x \in (-L,L)$.

Analyze the wave functions and the quantization of energy levels in a one-dimensional infinite potential well.

Describe the concept of radioactive decay and three types of decay processes: alpha, beta, and gamma decay.

Describe the decay rates and half-lives of radioactive isotopes.

Discuss the Standard Model of particle physics. Describe the fundamental particles and forces in the model.


### Physics Exercise: Electric Field and Potential from Multiple Charge Sources

---

#### **Objective:**

Analyze and compare the electric field and potential created by a system of point charges. Use computational methods to:

1. Calculate and visualize the effective electric field from multiple charges.
2. Plot the electric potential and its gradient.
3. Compare the electric field derived directly with that obtained via the gradient of the potential.

---

#### **Problem Statement:**

You are tasked with analyzing the electric field and potential from a set of point charges arranged in space. By simulating and visualizing these quantities, you will explore their relationships and understand how to compute the electric field both directly and via the gradient of the potential.

---

#### **Steps to Follow:**

1. **Setup the Charge Configuration:**
   - Define a system of $N$ point charges (at least three), each with charge $q_i$ positioned at coordinates $(x_i, y_i)$.
   - Choose arbitrary values for $q_i$ (positive or negative) and their positions $(x_i, y_i)$.

2. **Compute the Electric Field:**
   - The electric field $\mathbf{E}$ at a point $(x, y)$ due to a charge $q_i$ at $(x_i, y_i)$ is given by:
     $$
     \mathbf{E}_i(x, y) = \frac{k_e q_i}{r_i^2} \hat{\mathbf{r}}_i
     $$
     where:
     - $k_e$ is Coulomb's constant.
     - $r_i = \sqrt{(x - x_i)^2 + (y - y_i)^2}$ is the distance between the field point and the charge.
     - $\hat{\mathbf{r}}_i = \frac{(x - x_i, y - y_i)}{r_i}$ is the unit vector pointing from the charge to the field point.

   - Calculate the total electric field as the vector sum of the contributions from all charges:
     $$
     \mathbf{E}(x, y) = \sum_{i=1}^N \mathbf{E}_i(x, y)
     $$

3. **Compute the Electric Potential:**
   - The electric potential $V$ at a point $(x, y)$ due to a charge $q_i$ at $(x_i, y_i)$ is given by:
     $$
     V_i(x, y) = \frac{k_e q_i}{r_i}
     $$
   - Calculate the total potential as the sum of contributions from all charges:
     $$
     V(x, y) = \sum_{i=1}^N V_i(x, y)
     $$

4. **Derive the Field from the Potential:**
   - Compute the electric field from the gradient of the potential:
     $$
     \mathbf{E}(x, y) = -\nabla V(x, y)
     $$
     where:
     $$
     \nabla V = \left( \frac{\partial V}{\partial x}, \frac{\partial V}{\partial y} \right)
     $$

5. **Visualization:**
   - Plot the electric field vectors as an arrow field on a grid.
   - Plot the electric potential $V(x, y)$ as a contour map.
   - Overlay the gradient vectors $-\nabla V$ on the potential map.

6. **Comparison:**
   - Compare the electric field calculated directly (step 2) with that obtained via the gradient of the potential (step 4).
   - Discuss the similarities, differences, and numerical accuracy of the two methods.

---

#### **Deliverables:**

1. **Code Implementation:**
   - Python script or notebook that calculates and visualizes:
     - Electric field vectors.
     - Electric potential and its gradient.
     - Overlay of both methods for comparison.
2. **Plots:**
   - Vector field of the electric field.
   - Contour map of the electric potential with gradient arrows.
3. **Analysis:**
   - A brief discussion comparing the two methods of computing the electric field.
   - Comments on numerical accuracy, limitations, and sources of error.

---

#### **Hints and Resources:**

- Use Python libraries like `NumPy` for calculations and `Matplotlib` for plotting.
- For numerical gradients, consider using `numpy.gradient`.
- Start with a simple charge configuration (e.g., two or three charges) before scaling up.

This exercise develops skills in electrostatics, numerical computation, and visualization while encouraging critical thinking about the relationship between electric field and potential.