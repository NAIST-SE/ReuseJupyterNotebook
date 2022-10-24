average_of_feat = train_df.groupby('target').agg(['mean']).T.reset_index().rename(columns={'level_0':'feature'}).drop('level_1', axis=1)
