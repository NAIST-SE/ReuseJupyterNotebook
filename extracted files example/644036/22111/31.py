def make_feature_types(df, features):
    df = df.copy()
    df = df.replace('nan', np.nan)
    for f in features:
        try:
            df[f] = pd.to_numeric(df[f])
        except ValueError:
            df[f] = df[f].astype('category')
    return df
