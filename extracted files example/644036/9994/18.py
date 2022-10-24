fig, ax = plt.subplots(figsize=(15, 5))
sns.lineplot(data=train.groupby(['DayofYear','meter_type']).mean().reset_index(),
            x='DayofYear',
            y='normalized_meter_reading_type',
            hue='meter_type',
            ax=ax)
# plt.title('Day of Year vs. Normalized Meter Reading')
plt.show()
