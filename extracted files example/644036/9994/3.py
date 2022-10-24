train['train'] = 1
test['train'] = 0
tt = pd.concat([train, test], axis=0, sort=True)

tt.groupby(['timestamp','meter_type'])['meter_reading'] \
    .median() \
    .reset_index().set_index('timestamp') \
    .groupby('meter_type')['meter_reading'] \
    .plot(figsize=(15, 5), title='Median Meter Reading by Meter Type (train and test timeframe)')
plt.legend()
plt.show()
