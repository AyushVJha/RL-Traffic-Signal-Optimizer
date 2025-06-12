import gym
from gymnasium import Env, spaces
import numpy as np

class TrafficEnv(Env):
    def __init__(self):
        super(TrafficEnv, self).__init__()
        self.action_space = spaces.Discrete(2)  # 0: NS green, 1: EW green
        self.observation_space = spaces.Box(low=0, high=100, shape=(4,), dtype=np.int32)
        self.reset()

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.traffic = np.random.randint(0, 10, size=(4,))
        self.steps = 0
        return self.traffic, {}

    def step(self, action):
        cars_passed = [0, 0, 0, 0]
        if action == 0:
            cars_passed[0] = min(5, self.traffic[0])
            cars_passed[1] = min(5, self.traffic[1])
        else:
            cars_passed[2] = min(5, self.traffic[2])
            cars_passed[3] = min(5, self.traffic[3])
    
        self.traffic -= cars_passed
        self.traffic = np.maximum(self.traffic, 0)
        new_cars = np.random.randint(0, 3, size=(4,))
        self.traffic += new_cars
        self.steps += 1
    
        reward = -np.sum(self.traffic)
        terminated = self.steps >= 100
        truncated = False
        return self.traffic, reward, terminated, truncated, {}
    
    def render(self, mode='human'):
        print(f"Traffic: N:{self.traffic[0]} S:{self.traffic[1]} E:{self.traffic[2]} W:{self.traffic[3]}")
