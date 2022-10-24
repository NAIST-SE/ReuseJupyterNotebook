# Clean Up any time the actual is less than the real
tt['ConfirmedCases_Pred'] = tt[['ConfirmedCases','ConfirmedCases_Pred']].max(axis=1)
tt['Fatalities_Pred'] = tt[['Fatalities','Fatalities_Pred']].max(axis=1)

tt['ConfirmedCases_Pred'] = tt['ConfirmedCases_Pred'].fillna(0)
tt['Fatalities_Pred'] = tt['Fatalities_Pred'].fillna(0)

# Fill pred with
tt.loc[~tt['ConfirmedCases'].isna(), 'ConfirmedCases_Pred1'] = tt.loc[~tt['ConfirmedCases'].isna()]['ConfirmedCases']
tt.loc[~tt['Fatalities'].isna(), 'Fatalities_Pred1'] = tt.loc[~tt['Fatalities'].isna()]['Fatalities']

tt['ConfirmedCases_Pred'] = tt.groupby('Place')['ConfirmedCases_Pred'].transform('cummax')
tt['Fatalities_Pred'] = tt.groupby('Place')['Fatalities_Pred'].transform('cummax')
