# # get coordinates from Google - for running locally

# import googlemaps
# gmaps = googlemaps.Client(key='yourAPIkey')
# locations = train['location'].unique()

# queries = []
# for l in tqdm(locations):
#     coords = gmaps.geocode(l, language='ru', region='ru')
#     queries.append(coords)

# coordlist = []
# for i in range(len(queries)):
#     if not queries[i]:
#         coordlist.append([50, 50])
#     else:
#         q=queries[i][0]
#         qpair = (list(q['geometry']['location'].values()))
#         coordlist.append(qpair)

# lats = [c[0] for c in coordlist]
# lons = [c[1] for c in coordlist]

# locs_df = pd.DataFrame(np.column_stack([locations, lons, lats]), columns = ['location', 'lon', 'lat'])

# locs_df['lon'] = pd.to_numeric(locs_df['lon'])
# locs_df['lat'] = pd.to_numeric(locs_df['lat'])
