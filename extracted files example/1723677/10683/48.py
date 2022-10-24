df_train['AvSigVersion2'] = df_train['AvSigVersion'].map(lambda x: np.int(x.split('.')[1]))
df_trainC = df_train[ df_train['AvSigVersion2']<275 ]
df_trainD = df_train[ df_train['AvSigVersion2']>=275 ]
comparePlot(df_trainC, df_trainD, 'CountryIdentifier', verbose=False,
            title='Time-split Validation vs. Train', lab1='Train', lab2='Validation')
