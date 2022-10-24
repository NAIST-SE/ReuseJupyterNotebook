del X_train, X_val, Y_train, Y_val
# LOAD TEST
load = ['AvSigVersion', 'Census_OSVersion', 'OsBuildLab']
df_test = pd.read_csv('../input/microsoft-malware-prediction/test.csv',dtype='category',usecols=load)
# GOOGLE DATA
df_test['WeekOf'] = df_test['AvSigVersion'].map(weekdictAS)
df_test = pd.merge(df_test, data, on='WeekOf', how='left')
# THREAT DATA
df_test = pd.merge(df_test,cv,on='AvSigVersion',how='left')
df_test['ThreatCount'].fillna(0,inplace=True)
# DELETE EXTRA
del df_test['WeekOf']
# DELETE ORIGINAL
del df_test['AvSigVersion'], df_test['OsBuildLab'], df_test['Census_OSVersion']
x=gc.collect()
print('TEST DATA')
df_test.sample(5)
