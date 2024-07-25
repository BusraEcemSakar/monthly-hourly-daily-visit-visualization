import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# create data
np.random.seed(0)  # Reproducibility 
dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='H')
data = {
    'datetime': dates,
    'day_of_week': dates.day_name(),
    'visit_count': np.random.poisson(lam=100, size=len(dates)) 
}
df = pd.DataFrame(data)


df['hour'] = df['datetime'].dt.hour
df['month'] = df['datetime'].dt.to_period('M').astype(str)  


day_colors = {
    'Monday': 'blue',
    'Tuesday': 'yellow',
    'Wednesday': 'green',
    'Thursday': 'red',
    'Friday': 'purple',
    'Saturday': 'orange',
    'Sunday': 'pink'
}

months = df['month'].unique()
days = df['day_of_week'].unique()


fig, axes = plt.subplots(nrows=len(months), ncols=len(days), figsize=(20, 2*len(months)), sharex=True, sharey=True)

for i, month in enumerate(months):
    for j, day in enumerate(days):
        ax = axes[i, j]
        data_subset = df[(df['month'] == month) & (df['day_of_week'] == day)]
        sns.barplot(x='hour', y='visit_count', data=data_subset, ax=ax, color=day_colors[day])
        ax.set_title(day if i == 0 else "", fontsize=8)
        if j == 0:
            ax.set_ylabel(month, fontsize=8)
        if i == len(months) - 1:
            ax.set_xlabel("Hour of the Day", fontsize=8)
        if j == len(days) - 1:
            ax.set_ylabel("Visit Count", fontsize=8)


plt.suptitle('Hourly Visit Counts for Each Day of the Week by Month', fontsize=16)
plt.subplots_adjust(hspace=0.5, wspace=0.3)

plt.show()
