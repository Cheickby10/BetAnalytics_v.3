import numpy as np

class CrashEnv:
    def step(self, action):
        crash = np.random.exponential(1.6)
        reward = action if crash > action else -1
        return crash, reward

class MinesEnv:
    def step(self, action):
        hit = np.random.rand()
        reward = 1 if hit > 0.5 else -1
        return hit, reward
