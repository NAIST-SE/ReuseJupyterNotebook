cities = pd.read_csv("../input/cities.csv", index_col=['CityId'])
pnums = list(sieve.primerange(0, cities.shape[0]))
cities['isprime'] = cities.index.isin(pnums)
display(cities.head())

# show all points and density of primes
allpoints = cities.hvplot.scatter('X', 'Y',  width=380, height=350, datashade=True, 
                title='All Cities')
colors = list(reversed(cc.kbc))
primedensity = cities[cities.isprime].hvplot.hexbin(x='X', y='Y', width=420, height=350, 
                cmap=colors, title='Density of Prime Cities').options(size_index='Count', 
                min_scale=0.8, max_scale=0.95)
allpoints + primedensity
