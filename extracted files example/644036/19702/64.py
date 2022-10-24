# Assume the places with small rate of change will continue slow down of virus spread
constant_case_places = tt.loc[(tt['Past_21Days_Confirmed_Change_of_Total'] < 0.01) & (tt['ConfirmedCases'] > 10)]['Place'].unique()
constant_case_places
