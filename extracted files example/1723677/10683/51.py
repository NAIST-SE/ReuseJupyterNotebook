del df_trainA, df_trainB, df_trainC, df_trainD
del df_train['DateAS'], df_test['DateAS']; x=gc.collect()
cols = [x for x in df_train.columns if x not in ['HasDetections','AvSigVersion2']]
    
print('Factorizing...')
for col in cols: factor_data(df_train, df_test, col)
print('Reducing memory...')
for col in cols: reduce_memory(df_train, col)
for col in cols: reduce_memory(df_test, col)
categorize(df_train, df_test, cols)
display_memory(df_train, df_test)
