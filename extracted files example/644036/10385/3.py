# Identify the index of postitive and negative observations
train_T.index = [x for x in range(0,200)]
negative_index = train.loc[train['target'] == 0].index.values
positive_index = train.loc[train['target'] == 1].index.values

# plot each one
for plotcount in tqdm(range(0, 5)):
    ax = train_T.sort_values('feat_mean')[negative_index[plotcount]].reset_index(drop=True).plot(figsize=(15, 5),
                                                                                                 color=colors[0],
                                                                                                 alpha=0.5)
    train_T.sort_values('feat_mean')[positive_index[plotcount]].reset_index(drop=True).plot(figsize=(15, 5),
                                                                                            color=colors[2],
                                                                                            alpha=0.5)
    ax.tick_params(which='minor', length=4, color='r')
