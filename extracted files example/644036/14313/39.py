if RUN_LGB:
    # Plot feature importance as done in https://www.kaggle.com/artgor/artgor-utils
    feature_importance["importance"] /= folds.n_splits
    cols = feature_importance[["feature", "importance"]].groupby("feature").mean().sort_values(
        by="importance", ascending=False)[:50].index

    best_features = feature_importance.loc[feature_importance.feature.isin(cols)]

    plt.figure(figsize=(15, 20));
    ax = sns.barplot(x="importance",
                y="feature",
                hue='fold',
                data=best_features.sort_values(by="importance", ascending=False));
    plt.title('LGB Features (avg over folds)');
