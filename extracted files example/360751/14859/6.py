index_cols = ['EntryStreetName', 'ExitStreetName', 'EntryHeading', 'ExitHeading']
value_cols = ['TimeFromFirstStop_p' + str(i) for i in [20, 40, 50, 60 , 80]]

def get_times(city, iid, pathlist):
    intersect = train[(train.City == city) & (train.IntersectionId == iid)]
    targets = target_df.loc[intersect.index, :]
    intersect = intersect.join(targets)
    paths = intersect.groupby(index_cols)[value_cols].agg(['mean', 'std']).fillna(0)
    paths['Path'] = pathlist
    paths.columns = paths.columns.swaplevel()
    return paths.sort_index(axis=1)

pathlist_bos = ['E_left', 'E_right', 'NE_left', 'SW_right', 'NE_thru', 'SW_u', 'SW_thru']
bos = get_times('Boston', 2, pathlist_bos)

pathlist_phi = ['N_thru', 'N_right', 'E_left', 'E_thru']
phi = get_times('Philadelphia', 1824, pathlist_phi)

display(bos, phi)
