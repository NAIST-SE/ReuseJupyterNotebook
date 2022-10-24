%%time
from sklearn.mixture import GaussianMixture

mclusterer = GaussianMixture(n_components=350, tol=0.01, random_state=66, verbose=1)
cities['mclust'] = mclusterer.fit_predict(cities[['X', 'Y']].values)
nmax = cities.mclust.max()
print("{} clusters".format(nmax+1))
