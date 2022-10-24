tt = had_drift(tt)
tt = add_model_groups(tt)
FILTER_TRAIN = '(time <= 47.6 or time > 48) and (time <= 364 or time > 382.4)'
tt = tt.query(FILTER_TRAIN)
tt['drift'] = tt['drift'].astype('bool')
