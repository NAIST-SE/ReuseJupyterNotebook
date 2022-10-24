cols = [x for x in df_train.columns if x not in ['HasDetections']+CE+cols3+cols6+cols8]
cols2 = CE; ct = 1
    
for col in cols.copy():
    rate = df_train[col].value_counts(normalize=True, dropna=False).values[0]
    if rate > 0.98:
        del df_train[col]
        del df_test[col]
        cols.remove(col)
        ct += 1

rmv3=['Census_OSSkuName', 'OsVer', 'Census_OSArchitecture', 'Census_OSInstallLanguageIdentifier']
rmv4=['SMode']
for col in rmv3+rmv4:
    del df_train[col]
    del df_test[col]
    cols.remove(col)
    ct +=1
    
print('Removed',ct,'variables')
x=gc.collect()
