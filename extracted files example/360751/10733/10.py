stoplist = []
for i,m in enumerate(opoints.mclust, 1):
    neigh.fit(cities.loc[cities.mclust == m, ['X', 'Y']].values)
    if m != opoints.mclust.values[-1]:
        nextstartnode = opoints.loc[i, 'startpt']
    else: 
        nextstartnode = 0
    nextstart = cities.loc[nextstartnode, ['X', 'Y']].values.reshape(1, -1)
    closestop = neigh.kneighbors(nextstart, return_distance=False)
    stop = cities.index[(cities.mclust == m) & (cities.clustorder == closestop.item())].values[0]
    stoplist.append(stop)
opoints['stoppt'] = stoplist 

display(cities.head(), opoints.head())
