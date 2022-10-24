# Thanks to @kamalchhirang for this kernel for this code: https://www.kaggle.com/kamalchhirang/eda-simple-feature-engineering-external-data
def get_dictionary(s):
    try:
        d = eval(s)
    except:
        d = {}
    return d
train = train
train['genres_split'] = train['genres'].map(lambda x: sorted([d['name'] for d in get_dictionary(x)])).map(lambda x: ','.join(map(str, x)))
genres = train.genres_split.str.get_dummies(sep=',')
train = pd.concat([train, genres], axis=1, sort=False)
