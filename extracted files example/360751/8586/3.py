# get coordinates from file
locs_df = pd.read_csv('../input/russian-cities/city_latlons.csv')

# merge dataframes and convert to Mercator
train = train.merge(locs_df, how='left', on='location')

def merc_from_arrays(lons, lats):
    r_major = 6378137.000
    x = r_major * np.radians(lons)
    scale = x/lons
    y = 180.0/np.pi * np.log(np.tan(np.pi/4.0 + lats * (np.pi/180.0)/2.0)) * scale
    return (x, y)

train['deal_x'], train['deal_y'] = merc_from_arrays(train['lon'].values, train['lat'].values)
train.head()
