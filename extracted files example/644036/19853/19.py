tt['ConfirmedCasesRolling2'] = tt.groupby('Place')['ConfirmedCases'].rolling(2, center=True).mean().values
tt['FatalitiesRolling2'] = tt.groupby('Place')['Fatalities'].rolling(2, center=True).mean().values
train = tt.loc[~tt['ConfirmedCases'].isna()].query('Days_Since_First_Case > 0')

TARGET = 'ConfirmedCasesRolling2'
