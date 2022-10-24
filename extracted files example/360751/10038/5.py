targets =  pd.read_csv("../input/lish-moa/train_targets_scored.csv",
                 index_col=['sig_id'])
targets_0_idx = targets[targets.sum(axis=1)==0].index

train_features =  pd.read_csv("../input/lish-moa/train_features.csv",
                 index_col=['sig_id'])
control_idx = train_features.query('cp_type=="ctl_vehicle"').index

diffs = len(set(control_idx) - set(targets_0_idx))
