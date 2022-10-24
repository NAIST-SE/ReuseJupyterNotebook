fig, ax = plt.subplots(figsize=(15, 5))
sns.barplot(data=train.groupby(['Weekday_Name','meter_type']).mean().reset_index(),
            x='Weekday_Name',
            y='normalized_meter_reading_type',
            hue='meter_type',
            ax=ax)
plt.title('Day of Week vs. Normalized Meter Reading')
plt.show()
