# pandas_seaborn_scatter.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset - Iris (comes with seaborn)
df = sns.load_dataset("iris")

# Set Seaborn theme
sns.set(style="whitegrid")

# Create scatter plot using Pandas + Seaborn
plt.figure(figsize=(8, 6))
scatter = sns.scatterplot(
    data=df,
    x="sepal_length",
    y="sepal_width",
    hue="species",          # color by species
    style="species",        # shape by species
    size="petal_length",    # size variation
    palette="Set2"
)

# Enhance plot
plt.title("Iris Dataset: Sepal Dimensions vs Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.legend(title="Species", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Save the plot
plt.savefig("iris_seaborn_scatter.png", dpi=300)

# Show plot
plt.show()
