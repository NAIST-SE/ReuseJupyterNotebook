pairs = (corr_mtx.where(np.triu(np.ones(corr_mtx.shape), k=1).astype(np.bool))
                     .stack()
                     .sort_values(ascending=False))
pairs[:4]
