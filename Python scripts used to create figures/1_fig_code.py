import matplotlib.pyplot as plt
from pathlib import Path


proposed_model_code = 49 
data_preprocessing = 15
baseline_models = 12
hyperparameter_tuning_code = 3

values = [proposed_model_code, data_preprocessing,  baseline_models, hyperparameter_tuning_code]
categories = ['Proposed model', 'Data Preprocessing', 'Baseline models', 'Hyperparameter tuning']

# Sort data by values descending
sorted_data = sorted(zip(values, categories), reverse=True)
sorted_values, sorted_categories = zip(*sorted_data)

# Plot
fig, ax = plt.subplots(figsize=(6, 2))
bars = ax.barh(sorted_categories, sorted_values, color='dodgerblue')

# Flip the y-axis so largest value is at the top
ax.invert_yaxis()
# Add values inside bars
for bar in bars:
    width = bar.get_width()
    ax.text(width / 2,                       # x = middle of the bar
            bar.get_y() + bar.get_height()/2,  # y = middle of the bar
            str(width),                      # label text
            ha='center', va='center',        # horizontal and vertical align center
            color='white')       # adjust font size/color as needed

# Labels and styling
ax.set_xlim(0, max(sorted_values) + 10)


path = Path("Python scripts used to create figures/fig-code.pdf")
plt.tight_layout()
plt.savefig(path)
plt.show()
