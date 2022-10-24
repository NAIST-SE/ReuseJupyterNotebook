cmap = cmap=sns.diverging_palette(5, 250, as_cmap=True)

train_df.drop(['target', 'wheezy-copper-turtle-magic'], axis=1). \
    describe().T\
    .sort_values('mean', ascending=False)\
    .drop('count', axis=1)\
    .T.style.background_gradient(cmap, axis=1)\
    .set_precision(2)
