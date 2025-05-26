# annotated_sine_wave.py

import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Plot sine wave
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Sine Wave', color='blue')

# Annotate the peak
peak_x = np.pi / 2
peak_y = np.sin(peak_x)

plt.annotate('Peak (π/2, 1)',
             xy=(peak_x, peak_y),
             xytext=(peak_x + 0.5, peak_y + 0.3),
             arrowprops=dict(facecolor='red', shrink=0.05),
             fontsize=10,
             color='darkred')

# Annotate zero crossing
zero_x = 0
zero_y = 0

plt.annotate('Zero (0, 0)',
             xy=(zero_x, zero_y),
             xytext=(zero_x + 0.5, zero_y - 0.5),
             arrowprops=dict(facecolor='green', shrink=0.05),
             fontsize=10,
             color='darkgreen')

# Add titles and labels
plt.title('Annotated Sine Wave Plot')
plt.xlabel('X axis (radians)')
plt.ylabel('Y = sin(x)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
