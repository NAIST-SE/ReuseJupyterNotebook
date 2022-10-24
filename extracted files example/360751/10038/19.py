from itertools import combinations

train_features_with = train_features.copy()
important = weights_df.loc[:5, 'feature'].tolist()
for pair in combinations(important, 2):
    col = "_".join(pair)
    train_features_with[col] = train_features_with[pair[0]] * train_features_with[pair[1]]

train_features_with[:5]
