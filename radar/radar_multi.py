import numpy as np
import matplotlib.pyplot as plt

def create_radar_chart(values, title):
    # Data
    categories = ['Infra Engineering', 'Observability', 'Automation', 'DevSecOps', 'Incident Response', 'Performance Analysis', 'Architecture', 'GRC']
    
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
    plt.title(f"SRE Skillset Radar - {title}")

    # Add watermark to bottom right
    fig.text(0.95, 0.05, 'LuMing SRE', fontsize=20, color='gray',
             ha='right', va='bottom', alpha=0.5, rotation=45)

    # Save the plot as PNG
    plt.savefig(f"sre_radar_{title.lower().replace(' ', '_')}.png")
    plt.close()

# Example usage
create_radar_chart([4, 4.5, 4, 3, 3, 4, 4, 3], "Full Stack SRE")
create_radar_chart([4, 2, 5, 3, 2, 2, 3, 2], "Cloud&Platform Engineer")
create_radar_chart([3.5, 2, 5, 5, 1, 1, 2, 1], "DevOps")
create_radar_chart([2, 4, 3, 4, 3, 3, 5, 5], "SRE Architect")
create_radar_chart([1, 4, 2, 2, 5, 3, 3, 3], "Incident&Operation Manager")