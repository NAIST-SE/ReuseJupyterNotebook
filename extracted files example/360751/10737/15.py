%%time
#%% find best threshold
def thresh_search(y_true, y_proba):
    best_thresh = 0
    best_score = 0
    for thresh in np.arange(0, 1, 0.01):
        score = f1_score(y_true, y_proba > thresh)
        if score > best_score:
            best_thresh = thresh
            best_score = score
    return best_thresh, best_score

print(roc_auc_score(y, train_pred))
thresh, score = thresh_search(y, train_pred)
print(thresh, score)
