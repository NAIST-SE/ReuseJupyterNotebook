%%time
#%% make splits for reuse
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=911)
splits = list(skf.split(train, y))

# Logistic Regression
train_pred = np.zeros(train.shape[0])
test_pred = np.zeros(X_test.shape[0])
for train_idx, val_idx in splits:
    X_train, y_train  = X_nb[train_idx], y[train_idx]
    X_val, y_val = X_nb[val_idx], y[val_idx]
    model = LogisticRegression(solver='saga', class_weight='balanced', 
                                    C=0.5, max_iter=250, verbose=1) #seed not set
    model.fit(X_train, y_train)
    val_pred = model.predict_proba(X_val)
    train_pred[val_idx] = val_pred[:,1]
    test_pred += model.predict_proba(X_test_nb)[:,1] / skf.get_n_splits()
    
# Topic Modeling? - coming soon
