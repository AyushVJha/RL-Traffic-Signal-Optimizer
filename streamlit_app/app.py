import streamlit as st
from stable_baselines3 import DQN
import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from env.traffic_env import TrafficEnv

st.title("🛑 RL Traffic Signal Optimizer Demo")

# Initialize environment and model
env = TrafficEnv()
model = DQN.load("models/dqn_traffic_model")

# Reset the environment
obs, _ = env.reset()
env.render()

if st.button("Run 10 Steps"):
    for _ in range(10):
        action, _ = model.predict(obs)
        obs, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated

        st.text(f"Action: {'NS Green' if action == 0 else 'EW Green'}")
        st.text(f"Traffic: {obs.tolist()}")
        if done:
            obs, _ = env.reset()

