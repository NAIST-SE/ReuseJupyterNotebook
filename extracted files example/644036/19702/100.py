# Questionable numbers
tt.groupby('Date').sum()[['ConfirmedCases',
                          'ConfirmedCases_Pred1',]].plot(figsize=(15, 5))
# Make Iran's Predictions Linear

tt.groupby('Date').sum()[['Fatalities',
                          'Fatalities_Pred1']].plot(figsize=(15, 5))
