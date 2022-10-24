# Questionable numbers
tt.query('Place == "Iran"').set_index('Date')[['ConfirmedCases',
                                               'ConfirmedCases_Pred1',]].plot(figsize=(15, 5))
# Make Iran's Predictions Linear

tt.query('Place == "Iran"').set_index('Date')[['Fatalities','Fatalities_Pred1']].plot(figsize=(15, 5))
