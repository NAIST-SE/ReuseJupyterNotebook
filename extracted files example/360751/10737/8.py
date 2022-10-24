# Logistic Regression
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=911)
train_pred = np.zeros(train.shape[0])
for train_idx, val_idx in skf.split(X_vecs, y):
    X_train, y_train  = X_vecs[train_idx], y[train_idx]
    X_val, y_val = X_vecs[val_idx], y[val_idx]
    model = LogisticRegression(solver='saga', class_weight='balanced', 
                                    C=0.5, max_iter=250, verbose=1, n_jobs=-1) #seed not set
    model.fit(X_train, y_train)
    val_pred = model.predict_proba(X_val)
    train_pred[val_idx] = val_pred[:,1]
    

print("finding best threshold")
best_thresh = 0.0
best_score = 0.0
for thresh in np.arange(0, 1, 0.01):
    score = f1_score(y, train_pred > thresh)
    if score > best_score:
        best_thresh = thresh
        best_score = score
print(best_thresh, best_score)
