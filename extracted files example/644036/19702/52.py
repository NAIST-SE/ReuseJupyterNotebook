tt['ConfirmedCases_Log'] = tt['ConfirmedCases'].apply(np.log1p)
tt['Fatalities_Log'] = tt['Fatalities'].apply(np.log1p)
