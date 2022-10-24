remaining_places = pd.DataFrame(tt.groupby('Place')['ConfirmedCases_Pred1'].max().isna()).query('ConfirmedCases_Pred1').index.values
print(remaining_places)
print(len(remaining_places))
