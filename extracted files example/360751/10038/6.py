test_features =  pd.read_csv("../input/lish-moa/test_features.csv",
                 index_col=['sig_id'])
test_control_idx = test_features.query('cp_type=="ctl_vehicle"').index

ctrl_pct = len(set(test_control_idx))/len(test_features)

print(diffs, ctrl_pct)
