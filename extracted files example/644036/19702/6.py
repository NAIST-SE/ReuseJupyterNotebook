tt['Population_final'] = tt['Population_final'].astype('int')
tt['Cases_Per_100kPop'] = (tt['ConfirmedCases'] / tt['Population_final']) * 100000
tt['Fatalities_Per_100kPop'] = (tt['Fatalities'] / tt['Population_final']) * 100000

tt['Cases_Percent_Pop'] = ((tt['ConfirmedCases'] / tt['Population_final']) * 100)
tt['Fatalities_Percent_Pop'] = ((tt['Fatalities'] / tt['Population_final']) * 100)

tt['Cases_Log_Percent_Pop'] = ((tt['ConfirmedCases'] / tt['Population_final']) * 100).apply(np.log1p)
tt['Fatalities_Log_Percent_Pop'] = ((tt['Fatalities'] / tt['Population_final']) * 100).apply(np.log1p)


tt['Max_Confirmed_Cases'] = tt.groupby('Place')['ConfirmedCases'].transform(max)
tt['Max_Fatalities'] = tt.groupby('Place')['Fatalities'].transform(max)

tt['Max_Cases_Per_100kPop'] = tt.groupby('Place')['Cases_Per_100kPop'].transform(max)
tt['Max_Fatalities_Per_100kPop'] = tt.groupby('Place')['Fatalities_Per_100kPop'].transform(max)
