print('Factorizing...')
for col in cols+cols2+cols6:
    factor_data(df_train, df_test, col)
print('Relaxing data...')
for col in cols+cols2: relax_data(df_train, df_test, col)
print('Optimizing memory...')
for col in cols+cols2+cols6:
    reduce_memory(df_train, col)
    reduce_memory(df_test, col)
# Converting 6 variables to categorical
categorize(df_train, df_test, cols2)
    
print('Number of variables is',len(cols+cols2+cols3+cols6+cols8))
display_memory(df_train, df_test)
