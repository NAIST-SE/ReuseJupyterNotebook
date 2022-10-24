%%time

losses = np.zeros((2, 3, 5))
for i in range(3):
    skf = StratifiedKFold(n_splits=5, random_state=i*8)
    scorer = make_scorer(log_loss, greater_is_better=False, needs_proba=True)
    losses[0,i] = cross_val_score(rf_model, X, y, scoring=scorer, cv=skf, n_jobs=nproc)
    losses[1,i] = cross_val_score(rf_model_with, X_with, y, scoring=scorer, cv=skf, n_jobs=nproc)
