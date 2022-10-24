train.groupby(['timestamp','meter_type'])['meter_reading'] \
    .median() \
    .reset_index().set_index('timestamp') \
    .groupby('meter_type')['meter_reading'] \
    .plot(figsize=(15, 5), title='Median Meter Reading by Meter Type (Test Set)')
plt.legend()
plt.show()
