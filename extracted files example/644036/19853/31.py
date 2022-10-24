tt['ConfirmedCases_Pred'] = tt[['ConfirmedCases_Pred1','ConfirmedCases_forecast']].mean(axis=1)
tt['Fatalities_Pred'] = tt[['Fatalities_Pred1','Fatalities_forecast']].mean(axis=1)
