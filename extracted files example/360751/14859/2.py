tt = pd.concat([train,test], keys=['train', 'test'], sort=False)

if tt.columns[-1:][0] == 'City': #Move city column to where it belongs
    ttcols = tt.columns.tolist() 
    ttcols_moved = ttcols[-1:] + ttcols[:-1] 
    tt = tt[ttcols_moved].reset_index(level=0)
display(tt.head(), target_df.head())
#del train, test
