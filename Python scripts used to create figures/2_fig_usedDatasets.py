import matplotlib.pyplot as plt
from pathlib import Path

categories = ['Amazon', 'Yelp', 'MovieLens', 'Gowalla', 'Tmall', 'Last.fm', "Retailrocket", 'Others']
values = [31, 24, 23, 12, 10 , 7, 6, 77]

# Sort data by values descending
sorted_data = sorted(zip(values, categories), reverse=True)
sorted_values, sorted_categories = zip(*sorted_data)

# Plot
fig, ax = plt.subplots(figsize=(6, 2.5))
bars = ax.barh(categories, values, color='dodgerblue')
ax.invert_yaxis()
# Flip the y-axis so largest value is at the top

# Add values inside bars
for bar in bars:
    width = bar.get_width()
    ax.text(width / 2,                       # x = middle of the bar
            bar.get_y() + bar.get_height()/2,  # y = middle of the bar
            str(width),                      # label text
            ha='center', va='center',        # horizontal and vertical align center
            color='white')       # adjust font size/color as needed

# Labels and styling
ax.set_xlim(0, max(values) + 10)

plt.tight_layout()

path = Path("Python scripts used to create figures/fig_usedDatasets.pdf")
plt.savefig(path)
plt.show()
