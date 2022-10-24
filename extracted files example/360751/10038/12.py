top_cols, idx = np.unique(pairs_df.iloc[:4, :2].values.flatten(), return_index=True)
                                                    # use df.to_numpy() for 1.0+
msno.matrix(targets_visible.loc[targets_treated[top_cols].any(axis=1), 
                top_cols[idx]].sort_values(['flt3_inhibitor', 'pdgfr_inhibitor', 'kit_inhibitor']), 
                sort=None, color=(1,0,0))
