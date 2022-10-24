from sklearn.cluster import KMeans
clust = KMeans()
deviation_pivot['cluster'] = clust.fit_predict(deviation_pivot)
