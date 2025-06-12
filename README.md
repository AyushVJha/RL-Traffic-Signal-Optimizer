# 🚦 RL-Powered Traffic Signal Optimizer

A reinforcement learning project that trains an agent to dynamically control a 4-way traffic signal using Deep Q-Learning. The goal is to minimize vehicle congestion and waiting time using intelligent policy learning.

---

## 📊 Project Highlights

| Feature                        | Description                                                   |
|-------------------------------|---------------------------------------------------------------|
| ✅ Custom `gym.Env`           | Designed from scratch for 4-lane traffic simulation           |
| ✅ RL Algorithm                | Deep Q-Network (DQN) via Stable-Baselines3                    |
| ✅ Interface                   | Streamlit demo to simulate agent decisions in real-time       |
| ✅ Visualization               | Reward-vs-episode curve plotted using Matplotlib              |
| ✅ Real-time inference         | Runs inference on trained agent in CLI and web UI             |
| ✅ Resume-Ready Metrics        | 200 episodes, reward ~-600, steps/episode: 100                |

---

## 🎯 Problem Statement

Traditional traffic signals use fixed timers, which fail to adapt to real-time conditions. This project simulates an **adaptive RL-based signal controller** that:
- Observes the traffic queue on all four sides
- Decides whether to keep North–South or East–West signal green
- Learns to minimize congestion and queue buildup

---

## 🧠 Model & Training Stats

- **Episodes Trained**: 200
- **Average Reward**: `-604` per 100-step episode (improved from ~-800 baseline)
- **FPS**: ~2600
- **Policy**: Fully trained DQN with epsilon decay to 0.05
- **Model Saved**: ✅ Yes (`models/dqn_traffic_model.zip`)

---

## 📦 Tech Stack

- Python 🐍
- [Stable-Baselines3](https://github.com/DLR-RM/stable-baselines3) (DQN)
- OpenAI Gym (Custom Env)
- NumPy, Matplotlib
- Streamlit (Web UI)

---

## 🚀 How to Run

### 1. Install Requirements
```bash
pip install -r requirements.txt
```

### 2. Train the Agent
```bash
python train.py
```

### 3. Evaluate Agent Performance
```bash
python evaluate.py
```

### 4. Plot Reward Curve
```bash
python notebooks/plot_rewards.py
```

### 5. Run the Streamlit Demo
```bash
streamlit run streamlit_app/app.py
```

---

## 📈 Reward vs. Episode Plot

> _Include this image if you have it_
![Reward Curve](training_reward_plot.png)

---

## 📬 Example Output (Console)

```txt
Traffic: N:2 S:4 E:5 W:5
Action: NS Green
Traffic: N:1 S:1 E:0 W:3
...
```

---

## 📁 Folder Structure

```
RL-Traffic-Signal-Optimizer/
├── env/                   # Custom Gym environment
├── models/                # Saved DQN model
├── streamlit_app/         # Web interface
├── notebooks/             # Reward visualization
├── train.py               # RL training
├── evaluate.py            # Run trained agent
├── requirements.txt
└── README.md
```

---

## 📜 License

MIT License © 2024

---

## 💼 Add to Resume

> ✅ Trained a DQN agent using Stable-Baselines3 to optimize a 4-way traffic signal  
> 📉 Achieved average episode reward of ~-600 vs static baseline  
> 🧠 Designed custom OpenAI Gym environment and deployed real-time demo via Streamlit

---

## 🔗 Links

- [SB3 Docs](https://stable-baselines3.readthedocs.io/)
- [Gym API](https://www.gymlibrary.dev/)
