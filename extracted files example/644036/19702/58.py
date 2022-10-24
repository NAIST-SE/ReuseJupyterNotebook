tt['Past_7Days_ConfirmedCases_Std'] = tt['Place'].map(tt.dropna(subset=['ConfirmedCases']).query('Date >= 20200324').groupby('Place')['ConfirmedCases'].std().to_dict())
tt['Past_7Days_Fatalities_Std'] = tt['Place'].map(tt.dropna(subset=['ConfirmedCases']).query('Date >= 20200324').groupby('Place')['Fatalities'].std().to_dict())

tt['Past_7Days_ConfirmedCases_Min'] = tt['Place'].map(tt.dropna(subset=['ConfirmedCases']).query('Date >= 20200324').groupby('Place')['ConfirmedCases'].min().to_dict())
tt['Past_7Days_Fatalities_Min'] = tt['Place'].map(tt.dropna(subset=['Fatalities']).query('Date >= 20200324').groupby('Place')['Fatalities'].min().to_dict())

tt['Past_7Days_ConfirmedCases_Max'] = tt['Place'].map(tt.dropna(subset=['ConfirmedCases']).query('Date >= 20200324').groupby('Place')['ConfirmedCases'].max().to_dict())
tt['Past_7Days_Fatalities_Max'] = tt['Place'].map(tt.dropna(subset=['Fatalities']).query('Date >= 20200324').groupby('Place')['Fatalities'].max().to_dict())

tt['Past_7Days_Confirmed_Change_of_Total'] = (tt['Past_7Days_ConfirmedCases_Max'] - tt['Past_7Days_ConfirmedCases_Min']) / (tt['Past_7Days_ConfirmedCases_Max'])
tt['Past_7Days_Fatalities_Change_of_Total'] = (tt['Past_7Days_Fatalities_Max'] - tt['Past_7Days_Fatalities_Min']) / (tt['Past_7Days_Fatalities_Max'])
