import numpy as np
from model.state import State
from model.params import Params

# Compute acceleration from solved E-L equations
def compute_accelerations(state, params):
    delta = state.theta_1 - state.theta_2

    # Clamp velocities before squaring
    v_1 = np.clip(state.v_1, -1000, 1000)
    v_2 = np.clip(state.v_2, -1000, 1000)

    b1 = 0.2
    b2 = 0.1

    # Matrix coefficients
    A = (params.m_1 + params.m_2) * params.l_1
    B = params.m_2 * params.l_2 * np.cos(delta)
    C = params.m_2 * params.l_1 * np.cos(delta)
    D = params.m_2 * params.l_2

    # RHS constraints with damping
    x_1 = (-params.m_2 * params.l_2 * v_2 * np.sin(delta)
           - (params.m_1 + params.m_2) * params.g * np.sin(state.theta_1)
           - b1 * v_1)

    x_2 = (params.m_2 * params.l_1 * v_1 * np.sin(delta)
           - params.m_2 * params.g * np.sin(state.theta_2)
           - b2 * v_2)

    # SLE Matrix
    a = np.array([[A, B], [C, D]]) # Coefficients
    b = np.array([x_1, x_2]) # Constraints

    if not np.all(np.isfinite([x_1, x_2])):
        return np.array([0.0, 0.0])

    try:
        x = np.linalg.solve(a, b) # Acceleration solution vector
    except np.linalg.LinAlgError:
        print("⚠️ Singular matrix in compute_accelerations")
        return np.array([0.0, 0.0])

    return x