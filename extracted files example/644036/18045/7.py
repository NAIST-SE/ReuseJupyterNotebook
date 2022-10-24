tt['signal_shift'] = np.nan
tt.loc[~tt['drift'], 'signal_shift'] = tt.loc[~tt['drift']]['signal']
