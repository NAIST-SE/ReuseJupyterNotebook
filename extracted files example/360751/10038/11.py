import missingno as msno

cols_sorted = targets_treated.sum().sort_values(ascending=False).index
targets_visible = targets_treated[cols_sorted].replace(0, np.nan)
                                                # you can also use pd.NA with pandas v1+

msno.matrix(targets_visible.iloc[:, :50].sample(n=1000), sort='descending', color=(1,0,0))
