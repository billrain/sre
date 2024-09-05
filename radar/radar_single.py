import numpy as np
import matplotlib.pyplot as plt

# Data
categories = ['Infra Engineering', 'Obseravability', 'Automation', 'DevSecOps', 'Incident Response', 'Performance Anaylsis', 'Architecture', 'GRC']
values = [4, 3, 5, 2, 4, 5, 3, 4]

# Number of variables
N = len(categories)

# Compute angle for each category
angles = [n / float(N) * 2 * np.pi for n in range(N)]
values += values[:1]
angles += angles[:1]

# Plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))
ax.plot(angles, values)
ax.fill(angles, values, alpha=0.3)

# Set category labels
plt.xticks(angles[:-1], categories)

# Remove radial labels
ax.set_yticklabels([])

# Add title
plt.title("SRE Radar Map")

plt.show()