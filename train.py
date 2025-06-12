from stable_baselines3 import DQN
from stable_baselines3.common.monitor import Monitor
from env.traffic_env import TrafficEnv
import os

env = TrafficEnv()
env = Monitor(env, "./logs")

model = DQN("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=20000)
model.save("models/dqn_traffic_model")