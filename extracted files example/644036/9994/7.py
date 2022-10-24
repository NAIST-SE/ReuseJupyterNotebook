train.query('building_id == 0 and meter == 0') \
    .set_index('timestamp')['meter_reading'].plot(figsize=(15, 3),
                                                 title='Building 0 - Meter 0')

plt.show()
train.query('building_id == 753').set_index('timestamp').groupby('meter')['meter_reading'].plot(figsize=(15, 3),
                                                 title='Building 753 - Meters 0-3')
plt.show()
train.query('building_id == 1322').set_index('timestamp').groupby('meter')['meter_reading'].plot(figsize=(15, 3),
                                                 title='Building 1322 - Meters 0-3')
plt.show()
