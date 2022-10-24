fig, ax = plt.subplots(figsize=(15, 5))
sns.barplot(data=train.groupby(['Month','meter_type']).mean().reset_index(),
            x='Month',
            y='normalized_meter_reading_type',
            hue='meter_type',
            ax=ax)
plt.title('Month vs. Normalized Meter Reading')
plt.show()
