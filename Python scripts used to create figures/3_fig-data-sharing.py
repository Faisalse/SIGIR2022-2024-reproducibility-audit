import matplotlib.pyplot as plt
from pathlib import Path

public_dataset_used = 65
data_filtering_information_provided =  42
download_link_provided = 36
preprocessed_datasets_provided = 13
data_split_shared = 35
categories = ['Public dataset(s) used', 'Data filtering information provided', 'Download link provided', 'Preprocessed dataset used', 'Data splits shared']
values = [public_dataset_used,  data_filtering_information_provided,  download_link_provided,  preprocessed_datasets_provided,  data_split_shared]


# Plot
fig, ax = plt.subplots(figsize=(6, 2))
bars = ax.barh(categories, values, color='dodgerblue')
ax.invert_yaxis()
#ax.invert_yaxis()
# Flip the y-axis so largest value is at the top

# Add values inside bars
for bar in bars:
    width = bar.get_width()
    ax.text(width / 2,                       # x = middle of the bar
            bar.get_y() + bar.get_height()/2,  # y = middle of the bar
            str(width),                      # label text
            ha='center', va='center',        # horizontal and vertical align center
            color='white')       # adjust font size/color as needed

max_val = max(values)
ax.set_xlim(0, max_val + 10)
ax.set_xticks(range(0, max_val + 10, 10))  # start=0, end=max+15, step=5

plt.tight_layout()
path = Path("Python scripts used to create figures/fig-data-sharing.pdf")
plt.savefig(path)
plt.show()
