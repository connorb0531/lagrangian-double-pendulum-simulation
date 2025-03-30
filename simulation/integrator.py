from model.dynamics import compute_accelerations
import numpy as np
from model.state import State
from model.params import Params

# Runge-Kutta numerical integrating method using pendulum state and param
def rk4_update(state, params, dt):
    # k1
    a1 = compute_accelerations(state, params)
    k1 = np.array([state.v_1, a1[0], state.v_2, a1[1]])

    # k2
    temp_state_2 = state.offset_by(k1, dt / 2)
    a2 = compute_accelerations(temp_state_2, params)
    k2 = np.array([temp_state_2.v_1, a2[0], temp_state_2.v_2, a2[1]])

    # k3
    temp_state_3 = state.offset_by(k2, dt / 2)
    a3 = compute_accelerations(temp_state_3, params)
    k3 = np.array([temp_state_3.v_1, a3[0], temp_state_3.v_2, a3[1]])

    # k4
    temp_state_4 = state.offset_by(k3, dt)
    a4 = compute_accelerations(temp_state_4, params)
    k4 = np.array([temp_state_4.v_1, a4[0], temp_state_4.v_2, a4[1]])

    # Combine increments
    total_k = (k1 + 2 * k2 + 2 * k3 + k4) / 6

    # Return updated state
    return state.offset_by(total_k, dt)