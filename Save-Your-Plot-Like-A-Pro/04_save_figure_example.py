# save_plot_high_quality.py

import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import os

# Generate sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='sin(x)', color='blue')
plt.title("High-Quality Sine Wave Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()

# Create 'exports' folder if not exists
os.makedirs("exports", exist_ok=True)

# Generate timestamped filename
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Save as PNG
plt.savefig(f"exports/sine_plot_{timestamp}.png", dpi=300, bbox_inches='tight')

# Save as PDF
plt.savefig(f"exports/sine_plot_{timestamp}.pdf", bbox_inches='tight')

print(f"Plot saved as PNG and PDF in 'exports' folder with timestamp: {timestamp}")

# Optional: show the plot
plt.show()
