fig, ax = plt.subplots(figsize=(15, 5))
sns.barplot(data=train.groupby(['Hour','meter_type']).mean().reset_index(),
            x='Hour',
            y='normalized_meter_reading_type',
            hue='meter_type',
            ax=ax)
plt.title('Hour within Day vs. Normalized Meter Reading')
plt.show()
