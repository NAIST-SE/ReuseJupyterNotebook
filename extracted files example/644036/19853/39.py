tt.groupby('Date').sum()[['ConfirmedCases',
                          'ConfirmedCases_Pred',]].plot(figsize=(15, 5))
tt.groupby('Date').sum()[['Fatalities',
                          'Fatalities_Pred']].plot(figsize=(15, 5))
