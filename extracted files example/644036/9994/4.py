pd.DataFrame(train.groupby('meter_type')['meter_reading'] \
                 .describe() \
                 .astype(int)) \
                 .sort_values('count',
                              ascending=False)
