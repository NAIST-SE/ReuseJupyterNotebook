sub1352 = pd.read_csv('../input/lanl-submissions/LB1.352_submission_147.csv')
sub1389 = pd.read_csv('../input/lanl-submissions/LB1.389_submissionverson_one.csv')
sub1362 = pd.read_csv('../input/lanl-submissions/LB1.362_submission_147.csv')
sub1371 = pd.read_csv('../input/lanl-submissions/LB1.371_submission_137.csv')
sub1380 = pd.read_csv('../input/lanl-submissions/LB1.380_submission.csv')
sub1381 = pd.read_csv('../input/lanl-submissions/LB1.381_submission_147.csv')
sub1389 = pd.read_csv('../input/lanl-submissions/LB1.389_submissionverson_one.csv')
sub_50feats = pd.read_csv('../input/lanl-submissions/submission_50feats_peaks 9000ks.csv')

ss['sub1.352'] = sub1352['time_to_failure']
ss['sub1.389'] = sub1389['time_to_failure']
ss['sub1.362'] = sub1362['time_to_failure']
ss['sub1.371'] = sub1371['time_to_failure']
ss['sub1.380'] = sub1380['time_to_failure']
ss['sub1.381'] = sub1381['time_to_failure']
ss['sub1.389'] = sub1389['time_to_failure']
ss['simulated'] = ss_simulated['time_to_failure']
