# Assume the places with small rate of change will continue slow down of virus spread
constant_fatal_places = tt.loc[(tt['Past_21Days_Fatalities_Change_of_Total'] < 0.01) & (tt['Fatalities'] > 1)]['Place'].unique()
constant_fatal_places
