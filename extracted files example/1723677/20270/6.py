# REWRITE DATA TO DATAFRAMES
df[cols] = comb.loc[:df.shape[0]-1,cols].values
test[cols] = comb.loc[df.shape[0]:,cols].values
