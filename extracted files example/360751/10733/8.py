opoints.reset_index(drop=True, inplace=True) #recall ordered points
cities['clustorder'] = cities.groupby('mclust').cumcount()
