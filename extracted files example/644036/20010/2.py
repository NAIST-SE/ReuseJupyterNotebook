train_df['Province_State'].fillna("",inplace = True)
test_df['Province_State'].fillna("",inplace = True)
train_df['Country_Region'] = train_df['Country_Region'] + ' ' + train_df['Province_State']
test_df['Country_Region'] = test_df['Country_Region'] + ' ' + test_df['Province_State']
del train_df['Province_State']
del test_df['Province_State']
