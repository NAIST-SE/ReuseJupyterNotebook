X = train_features
y = targets.proteasome_inhibitor

X[['cp_type', 'cp_dose']] = X[['cp_type', 'cp_dose']].astype('category').apply(lambda x: x.cat.codes)

rf_model = RandomForestClassifier(n_estimators=100, random_state=10, verbose=True, n_jobs=nproc)
scorer = make_scorer(log_loss)
skf = StratifiedKFold(n_splits=5, random_state=24)
