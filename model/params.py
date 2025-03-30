from scipy import constants

# Pendulum constant params
class Params:
    def __init__(self, m_1, m_2, l_1, l_2):
        self.m_1 = m_1
        self.m_2 = m_2
        self.l_1 = l_1
        self.l_2 = l_2
        self.g = constants.g