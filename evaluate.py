from stable_baselines3 import DQN
from env.traffic_env import TrafficEnv

env = TrafficEnv()
model = DQN.load("models/dqn_traffic_model")

obs, _ = env.reset()
for _ in range(20):
    action, _ = model.predict(obs)
    obs, _, done, _, _ = env.step(action)
    env.render()
    if done:
        obs, _ = env.reset()

