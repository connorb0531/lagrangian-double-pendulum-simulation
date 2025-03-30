
# Pendulum state (position & velocity)
class State:
    def __init__(self, theta_1, theta_2, v_1, v_2):
        self.theta_1 = theta_1
        self.theta_2 = theta_2
        self.v_1 = v_1
        self.v_2 = v_2

    # Offsets state values for RK4 integration
    def offset_by(self, k, dt_scalar):
        return State(
            self.theta_1 + dt_scalar * k[0],
            self.v_1 + dt_scalar * k[1],
            self.theta_2 + dt_scalar * k[2],
            self.v_2 + dt_scalar * k[3]
        )