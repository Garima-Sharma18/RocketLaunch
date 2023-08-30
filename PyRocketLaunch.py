import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, HTML, clear_output
import time

# Constants
g = 9.81  # acceleration due to gravity (m/s^2)
rocket_radius = 0.1  # radius of the rocket symbol

def projectile_motion(v0, angle_deg, wall_height, wall_distance):
    angle_rad = np.radians(angle_deg)
    t_flight = 2 * v0 * np.sin(angle_rad) / g
    max_height = (v0**2) * (np.sin(angle_rad)**2) / (2 * g)
    max_distance = v0 * np.cos(angle_rad) * t_flight

    time_intervals = np.linspace(0, t_flight, num=100)
    x = v0 * np.cos(angle_rad) * time_intervals
    y = v0 * np.sin(angle_rad) * time_intervals - 0.5 * g * time_intervals**2

    wall_hit = False
    if x[-1] >= wall_distance and y[-1] <= wall_height:
        wall_hit = True

    return x, y, wall_hit

def animate(i):
    rocket.set_data(x[:i], y[:i])
    return rocket,

# Randomize wall height and distance
wall_height = np.random.uniform(5, 15)
wall_distance = np.random.uniform(20, 40)

# Create initial plot
fig, ax = plt.subplots()
ax.set_xlim(0, 50)
ax.set_ylim(0, 30)
ax.axhline(y=wall_height, color='r', linestyle='--', label='Wall')
ax.set_xlabel('Horizontal Distance (m)')
ax.set_ylabel('Vertical Distance (m)')
ax.set_title('Projectile Motion Game')
ax.legend()

# Initialize rocket symbol
rocket, = ax.plot([], [], marker='o', markersize=10, color='b')

# Get user input for initial velocity
v0_guess = float(input("Enter your initial velocity guess: "))

# Calculate projectile motion
x, y, wall_hit = projectile_motion(v0_guess, 45, wall_height, wall_distance)

# Simulate animation
for i in range(len(x)):
    rocket.set_data(x[:i], y[:i])
    display(fig)
    clear_output(wait=True)
    time.sleep(0.05)

# Display the final result
plt.show()

# Print game result
if wall_hit:
    print("Congratulations! You cleared the wall.")
else:
    print("Oops! The rocket didn't clear the wall.")
    print("The correct initial velocity to clear the wall was:", max(x) / (np.cos(np.radians(45))))
