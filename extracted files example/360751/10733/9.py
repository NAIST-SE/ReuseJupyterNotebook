from sklearn.neighbors import NearestNeighbors

startlist=[0]
neigh = NearestNeighbors(n_neighbors=1, n_jobs=-1)
for i,m in enumerate(opoints.mclust[1:], 0):
    neigh.fit(cities.loc[cities.mclust == m, ['X', 'Y']].values)
    lastcenter = opoints.loc[i, ['X', 'Y']].values.reshape(1, -1)
    closestart = neigh.kneighbors(lastcenter, return_distance=False)
    start = cities.index[(cities.mclust == m) & (cities.clustorder == closestart.item())].values[0]
    startlist.append(start)
opoints['startpt'] = startlist    
