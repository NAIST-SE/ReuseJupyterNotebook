# Engineer a single feature: distance vector between atoms
#  (there's ways to speed this up!)

# def dist(row):
#     return ( (row['x_1'] - row['x_0'])**2 +
#              (row['y_1'] - row['y_0'])**2 +
#              (row['z_1'] - row['z_0'])**2 ) ** 0.5

# train['dist'] = train.apply(lambda x: dist(x), axis=1)
# test['dist'] = test.apply(lambda x: dist(x), axis=1)

# takes 7+ minutes per run
