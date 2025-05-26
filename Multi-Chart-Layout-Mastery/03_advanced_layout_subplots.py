# multi_chart_layout.py

import matplotlib.pyplot as plt
import numpy as np

# Generate synthetic data
x = np.linspace(0, 10, 100)
y = np.sin(x)
categories = ['A', 'B', 'C', 'D']
values = [25, 40, 35, 50]
data = np.random.normal(0, 1, 1000)
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)

# Create a 2x2 grid layout
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Line Chart
axs[0, 0].plot(x, y, color='blue')
axs[0, 0].set_title("Line Chart: Sine Wave")
axs[0, 0].set_xlabel("X")
axs[0, 0].set_ylabel("sin(x)")
axs[0, 0].grid(True)

# Bar Chart
axs[0, 1].bar(categories, values, color='orange')
axs[0, 1].set_title("Bar Chart: Category Values")
axs[0, 1].set_ylabel("Value")

# Histogram
axs[1, 0].hist(data, bins=30, color='green', edgecolor='black')
axs[1, 0].set_title("Histogram: Normal Distribution")

# Scatter Plot
axs[1, 1].scatter(x_scatter, y_scatter, color='purple', alpha=0.7)
axs[1, 1].set_title("Scatter Plot: Random Points")
axs[1, 1].set_xlabel("X")
axs[1, 1].set_ylabel("Y")

# Layout
plt.suptitle("Multi-Chart Layout Mastery", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
