# Clean Up any time the actual is less than the real
tt['ConfirmedCases_Pred1'] = tt[['ConfirmedCases','ConfirmedCases_Pred1']].max(axis=1)
tt['Fatalities_Pred1'] = tt[['Fatalities','Fatalities_Pred1']].max(axis=1)

tt['ConfirmedCases_Pred1'] = tt['ConfirmedCases_Pred1'].fillna(0)
tt['Fatalities_Pred1'] = tt['Fatalities_Pred1'].fillna(0)

# Fill pred with
tt.loc[~tt['ConfirmedCases'].isna(), 'ConfirmedCases_Pred1'] = tt.loc[~tt['ConfirmedCases'].isna()]['ConfirmedCases']
tt.loc[~tt['Fatalities'].isna(), 'Fatalities_Pred1'] = tt.loc[~tt['Fatalities'].isna()]['Fatalities']

tt['ConfirmedCases_Pred1'] = tt.groupby('Place')['ConfirmedCases_Pred1'].transform('cummax')
tt['Fatalities_Pred1'] = tt.groupby('Place')['Fatalities_Pred1'].transform('cummax')
