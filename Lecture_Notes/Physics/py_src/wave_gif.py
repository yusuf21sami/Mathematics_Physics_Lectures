import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import os

# Parameters
L = 1.0          # Length of the string
T = 1.0          # Total simulation time
c = 1.0          # Wave speed
nx = 100         # Number of spatial points
nt = 500         # Number of time steps

dx = L / (nx - 1)            # Spatial step size
dt = T / nt                  # Time step size
r = c * dt / dx              # Courant number

# Initialize arrays
u = np.zeros((nt, nx))       # Solution array for each time step
x = np.linspace(0, L, nx)    # Spatial coordinates

# Initial condition: Gaussian pulse centered at x=0.5
u[0, :] = np.exp(-100 * (x - 0.5)**2)
u[1, :] = u[0, :]

# Boundary conditions: u(0, t) = u(L, t) = 0 (string fixed at both ends)
u[:, 0] = 0
u[:, -1] = 0

# Time-stepping loop using finite difference method
for n in range(1, nt - 1):
    for i in range(1, nx - 1):
        u[n + 1, i] = (2 * (1 - r**2) * u[n, i] -
                       u[n - 1, i] +
                       r**2 * (u[n, i + 1] + u[n, i - 1]))

# Create and save frames for the animation
filenames = []
for n in range(nt):
    plt.figure()
    plt.plot(x, u[n, :], label=f'Time = {n*dt:.2f} s')
    plt.ylim(-1.1, 1.1)
    plt.xlabel('Position along the string')
    plt.ylabel('Amplitude')
    plt.title('Wave propagation on a string')
    plt.legend()
    filename = f'frame_{n:04d}.png'
    plt.savefig(filename)
    plt.close()
    filenames.append(filename)

# Create GIF from the saved frames
with imageio.get_writer('Physics/py_src/wave_propagation.gif', mode='I', duration=dt, loop=0) as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

# Remove temporary frame files
for filename in filenames:
    os.remove(filename)
