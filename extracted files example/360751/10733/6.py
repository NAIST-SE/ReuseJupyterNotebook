%%time
#%% parameters
num_iters=100

# main
nnode = int(cities.loc[0, 'mclust'])
locations = centers[['X', 'Y']].values
segment = get_route(locations, nnode, 0, fixed=False)
