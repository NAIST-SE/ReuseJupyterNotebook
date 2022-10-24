%%time 
num_iters = 100
seglist = []
total_clusts = cities.shape[0]
for i,m in enumerate(opoints.mclust):
    district = cities[cities.mclust == m]
    print("begin cluster {}, {} of {}".format(m, i, opoints.shape[0]-1))

    clstart = opoints.loc[i, 'startpt']
    nnode = district.loc[clstart, 'clustorder']
    clstop = opoints.loc[i, 'stoppt']
    pnode = district.loc[clstop, 'clustorder']
    locations = district[['X', 'Y']].values
    
    segnodes = get_route(locations, nnode, pnode, fixed=False) #output is type list
    ord_district =  district.iloc[segnodes]
    segment = ord_district.index.tolist()
    seglist.append(segment)

seglist.append([0])
path = np.concatenate(seglist)
