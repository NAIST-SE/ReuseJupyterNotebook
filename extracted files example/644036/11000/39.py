# Cap the minimum and maximum time to failure values
ss.loc[ss['time_to_failure'] < 0, 'time_to_failure'] = 0
ss.loc[ss['time_to_failure'] > 12, 'time_to_failure'] = 12
