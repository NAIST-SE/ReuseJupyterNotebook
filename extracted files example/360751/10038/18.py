weights = eli5.explain_weights_dfs(perm, feature_names=X.columns.tolist())
weights_df = weights['feature_importances']
weights_df[:15]
