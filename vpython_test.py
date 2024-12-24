from vpython import *
import numpy as np

# Parameters
N = 10000  # Total number of points to generate
R = 1      # Radius of the sphere shell
dr = 0.05  # Thickness of the shell
M = 7      # Total mass of the points
dm = M / N # Mass of each individual point
I = 0      # Moment of inertia initialization
rp = []    # List to store the positions of the points

# Generate points until we have N valid points
while len(rp) < N:
    # Generate a random point in 3D space
    rr = vector(np.random.uniform(-1, 1), np.random.uniform(-1, 1), np.random.uniform(-1, 1))
    mag_rr = mag(rr)  # Calculate the magnitude of the vector
    # Check if the point lies within the spherical shell
    if R * (1 - dr) < mag_rr < R*(1 + dr):
        sphere(pos=rr, radius=0.03)  # Visualize the point as a sphere
        rp.append(rr)  # Add the valid point to the list

# Calculate the moment of inertia
I = sum(dm * (rt.x**2 + rt.y**2) for rt in rp)
print("I = ", I, "kgm^2")  # Output the calculated moment of inertia
It = (2 / 3) * M * R**2  # Theoretical moment of inertia for a solid sphere
print("It = ", It, "kgm^2")  # Output the theoretical moment of inertia
