import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, color='green', linewidth=2, label='sin(x)')

# Custom ticks and axis styling
plt.xticks(ticks=np.arange(0, 11, 1))
plt.yticks(ticks=[-1, -0.5, 0, 0.5, 1])
plt.xlabel('X Axis (0 to 10)', fontsize=12)
plt.ylabel('Y Axis (sin values)', fontsize=12)
plt.title('Custom Ticks and Axis Styling Example', fontsize=14, fontweight='bold')

# Customize spines (axis lines)
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('blue')
ax.spines['bottom'].set_color('blue')
ax.spines['left'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)

# Grid and legend
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
