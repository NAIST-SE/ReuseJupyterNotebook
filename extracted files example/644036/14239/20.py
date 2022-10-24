test_df.drop(['wheezy-copper-turtle-magic'], axis=1). \
    describe().T\
    .sort_values('mean', ascending=False)\
    .drop('count', axis=1)\
    .T.style.background_gradient(cmap, axis=1)\
    .set_precision(2)
