train['Weekday'] = train['timestamp'].dt.weekday
train['Weekday_Name'] = train['timestamp'].dt.weekday_name
train['Month'] = train['timestamp'].dt.month
train['DayofYear'] = train['timestamp'].dt.dayofyear
train['Hour'] = train['timestamp'].dt.hour
