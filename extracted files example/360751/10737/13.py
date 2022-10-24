%%time
#%% Transform with Naive Bayes - combo of Ren and Jeremy Howard
class NBTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, alpha=1):
        self.r = None
        self.alpha = alpha

    def fit(self, X, y):
        p = self.alpha + X[y==1].sum(0)
        q = self.alpha + X[y==0].sum(0)
        self.r = csr_matrix(np.log(
            (p / (self.alpha + (y==1).sum())) /
            (q / (self.alpha + (y==0).sum()))
        ))
        return self

    def transform(self, X, y=None):
        return X.multiply(self.r)

print("nb transforming")
nbt = NBTransformer(alpha=1)
nbt.fit(X, y)
X_nb = nbt.transform(X)
X_test_nb = nbt.transform(X_test)
np.unique(X_nb.getrow(1).toarray()) #look at some contents
