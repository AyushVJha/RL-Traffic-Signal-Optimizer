import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("logs/monitor.csv", skiprows=1)
plt.plot(data["r"])
plt.title("Episode Rewards")
plt.xlabel("Episode")
plt.ylabel("Reward")
plt.grid()
plt.savefig("training_reward_plot.png")
plt.show()