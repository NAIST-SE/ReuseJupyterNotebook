meter_mapping = {0: 'electricity', 1: 'chilledwater', 2: 'steam', 3: 'hotwater'}
train['meter_type'] = train['meter'].map(meter_mapping)
test['meter_type'] = test['meter'].map(meter_mapping)
