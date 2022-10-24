tt.loc[tt['Place'].isin(us_states)].groupby('Place')['Fatalities_Pred1'].max().sum()
