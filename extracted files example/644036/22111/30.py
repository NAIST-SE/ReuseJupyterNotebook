def get_train_long(train):
    dfs = []

    def pad(feat, tolen):
        padded = np.pad(feat,
                        (0, tolen-len(feat)),
                        mode='constant',
                        constant_values=np.nan)
        return padded

    for d in tqdm(train.itertuples(), total=len(train)):
        sequence = [s for s in d[3]]
        seq_len = len(sequence)
        structure = [s for s in d[4]]
        predicted_loop_type = [s for s in d[5]]
        reactivity_error = pad([s for s in d[10]], seq_len)
        deg_error_Mg_pH10 = pad([s for s in d[11]], seq_len)
        deg_error_pH10 = pad([s for s in d[12]], seq_len)
        deg_error_Mg_50C = pad([s for s in d[13]], seq_len)
        deg_error_50C = pad([s for s in d[14]], seq_len)

        reactivity = pad([s for s in d[15]], seq_len)
        deg_Mg_pH10 = pad([s for s in d[16]], seq_len)
        deg_pH10 = pad([s for s in d[17]], seq_len)
        deg_Mg_50C = pad([s for s in d[18]], seq_len)
        deg_50C = pad([s for s in d[10]], seq_len)
        myid = [d[2]] * len(sequence)
        seqpos = [c for c in range(len(sequence))]
        dfs.append(pd.DataFrame(np.array([myid,
                                          seqpos,
                                          sequence,
                                          structure,
                                          predicted_loop_type,
                                          reactivity_error,
                                          deg_error_Mg_pH10,
                                          deg_error_pH10,
                                          deg_error_Mg_50C,
                                          deg_error_50C,
                                          reactivity,
                                          deg_Mg_pH10,
                                          deg_pH10,
                                          deg_Mg_50C,
                                         ]).T))
    train_long = pd.concat(dfs)

    train_long.columns=['id',
               'seqpos',
               'sequence',
               'structure',
               'predicted_loop_type',
               'reactivity_error',
               'deg_error_Mg_pH10',
               'deg_error_pH10',
               'deg_error_Mg_50C',
               'deg_error_50C',
               'reactivity',
               'deg_Mg_pH10',
               'deg_pH10',
               'deg_Mg_50C']

    return train_long


def get_test_long(test):
    dfs = []

    def pad(feat, tolen):
        padded = np.pad(feat,
                        (0, tolen-len(feat)),
                        mode='constant',
                        constant_values=np.nan)
        return padded

    for d in tqdm(test.itertuples(), total=len(test)):
        sequence = [s for s in d[3]]
        seq_len = len(sequence)
        structure = [s for s in d[4]]
        predicted_loop_type = [s for s in d[5]]
        myid = [d[2]] * len(sequence)
        seqpos = [c for c in range(len(sequence))]
        dfs.append(pd.DataFrame(np.array([myid,
                                          seqpos,
                                          sequence,
                                          structure,
                                          predicted_loop_type,
                                         ]).T))
    test_long = pd.concat(dfs)

    test_long.columns=['id',
               'seqpos',
               'sequence',
               'structure',
               'predicted_loop_type']

    return test_long

def add_long_features(df):
    df = df.copy()
    df['seqpos'] = df['seqpos'].astype('int')
    df = df.merge(df.query('seqpos <= 106') \
                    .groupby('id')['sequence'] \
                      .value_counts() \
                      .unstack() \
                      .reset_index(),
             how='left',
             on=['id'],
             validate='m:1'
            )
    
    df = df.merge(df.query('seqpos <= 106') \
                  .groupby('id')['structure'] \
                      .value_counts() \
                      .unstack() \
                      .reset_index(),
             how='left',
             on=['id'],
             validate='m:1'
            )

    df = df.merge(df.query('seqpos <= 106') \
                  .groupby('id')['predicted_loop_type'] \
                      .value_counts() \
                      .unstack() \
                      .reset_index(),
             how='left',
             on=['id'],
             validate='m:1'
            )
    for shift in [-5, -4, -3, -2 -1, 1, 2, 3, 4, 5]:
        for f in ['sequence','structure','predicted_loop_type']:
            df[f'{f}_shift{shift}'] = df.groupby('id')[f].shift(shift)
    return df
