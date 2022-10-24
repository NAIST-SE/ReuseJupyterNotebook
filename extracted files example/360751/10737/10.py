# predict on test set
test = pd.read_csv('../input/test.csv', index_col=['qid'])
test.head()
X_test = test.question_text.tolist()
X_testvecs = np.array([nlp_lg(text).vector for text in tqdm(X_test)])

trounds = 3
preds_test = np.zeros(len(X_test))
for i in range(trounds):
    model = LogisticRegression(solver='saga', class_weight='balanced', 
                                    C=0.5, max_iter=250, verbose=1, n_jobs=-1, random_state=40*i)
    model.fit(X_vecs, y)
    preds_test += lgr.predict_proba(X_testvecs)[:, 1] / trounds

    
# submit
sub = pd.read_csv('../input/sample_submission.csv', index_col=['qid'])
sub['prediction'] = preds_test > best_thresh
sub.to_csv('submission.csv')
