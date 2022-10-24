from datetime import datetime
datedictAS = np.load('../input/malware-timestamps/AvSigVersionTimestamps.npy')[()]
df_train['DateAS'] = df_train['AvSigVersion'].map(datedictAS)
df_test['DateAS'] = df_test['AvSigVersion'].map(datedictAS)

df_testA = df_test[ df_test['DateAS']<datetime(2018,10,25) ]
df_testB = df_test[ df_test['DateAS']>datetime(2018,10,25) ]
comparePlot(df_train, df_testB, 'CountryIdentifier', verbose=False,
           title='Private Test vs. Train', lab1='Train', lab2='Private Test')
comparePlot(df_train, df_testA, 'CountryIdentifier', verbose=False,
           title='Public Test vs. Train', lab1='Train', lab2='Public Test')
