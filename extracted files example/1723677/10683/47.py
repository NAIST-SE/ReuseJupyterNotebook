df_trainA = df_train.sample(frac=0.5)
df_trainB = df_train[ ~df_train.index.isin(df_trainA.index)]
comparePlot(df_trainA, df_trainB, 'CountryIdentifier', verbose=False,
            title='Random Validation Set vs. Train Subset', lab1='Train', lab2='Validation')
