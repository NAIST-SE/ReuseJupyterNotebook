train.query('meter_reading < 5000')['meter_reading'] \
    .plot(kind='hist',
          figsize=(15, 3),
          title='Distribution of meter_reading, excluding values greater than 5000',
          bins=200)
plt.show()
train.query('meter_reading < 500')['meter_reading'] \
    .plot(kind='hist',
          figsize=(15, 3),
          title='Distribution of meter_reading, excluding values greater than 500',
         bins=200)
plt.show()
train.query('meter_reading < 100')['meter_reading'] \
    .plot(kind='hist',
          figsize=(15, 3),
          title='Distribution of meter_reading, excluding values greater than 100',
         bins=100)
plt.show()
