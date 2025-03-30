# Input initial positions, velocities, masses, & lengths
# RK4 integration for velocity and position update
# Acceleration via E-L matrix SLE

import numpy as np
from model.state import State
from model.params import Params
from simulation.integrator import rk4_update
from visualization.animation import animate

# Simulation settings
dt = 0.01
total_time = 5
num_steps = int(total_time / dt)

# Params
params = Params(m_1=2.0, m_2=1.0, l_1=1.0, l_2=1.0)

# Initial state
state = State(theta_1=np.pi / 2, v_1=0.0, theta_2=np.pi / 2 - 0.1, v_2=0.0)

# History of positions for animation
history = np.zeros((num_steps, 4))  # [x1, y1, x2, y2]

for i in range(num_steps):
    # Generalized coordinates cartesian for plotting
    x1 = params.l_1 * np.sin(state.theta_1)
    y1 = -params.l_1 * np.cos(state.theta_1)
    x2 = x1 + params.l_2 * np.sin(state.theta_2)
    y2 = y1 - params.l_2 * np.cos(state.theta_2)

    # Position history
    history[i] = [x1, y1, x2, y2]
    state = rk4_update(state, params, dt)

    # Prevent unwanted increase in velocity
    MAX_VELOCITY = 100
    state.v_1 = np.clip(state.v_1, -MAX_VELOCITY, MAX_VELOCITY)
    state.v_2 = np.clip(state.v_2, -MAX_VELOCITY, MAX_VELOCITY)

    if not np.isfinite([state.theta_1, state.theta_2, state.v_1, state.v_2]).all():
        print(f"🚨 Unstable state at step {i}")
        break

# Run the animation
animate(history)

print('Animation finished.')