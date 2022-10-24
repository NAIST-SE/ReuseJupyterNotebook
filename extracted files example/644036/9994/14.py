train['normalized_meter_reading_type'] = \
    train.groupby('meter_type')['meter_reading'] \
        .transform(lambda x: (x - x.mean()) / x.std())
