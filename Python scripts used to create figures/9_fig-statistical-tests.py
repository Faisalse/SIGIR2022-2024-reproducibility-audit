import matplotlib.pyplot as plt
from pathlib import Path

only_p_value_given = 14
t_test = 20
no_analysis = 31


plt.rcParams['font.family'] = 'Arial'
plt.rcParams.update({
    'font.size': 12          # Default text size
})
# Data
categories = ["No statistical analysis", "Some t-test mentioned and p-value given", "Only p-value given", ]
values = [no_analysis, t_test, only_p_value_given ]

# Plot
colors = ['crimson', 'crimson', 'crimson']
fig, ax = plt.subplots(figsize=(6, 1.5))
bars = ax.barh(categories, values, color=colors)
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
max_val = max(values)
ax.set_xlim(0, max_val + 10)
ax.set_xticks(range(0, max_val + 10, 10))  # start=0, end=max+15, step=5


path = Path("Python scripts used to create figures/fig-statistical-tests.pdf")
plt.tight_layout()
plt.savefig(path)
plt.show()
