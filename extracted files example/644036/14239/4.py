### SAVE RESULTS
oof_qda = oof_qda.reshape(-1, 1)
pred_te_qda = pred_te_qda.reshape(-1, 1)

np.save('{}-oof.np'.format(MODEL_NUMBER), oof_qda)
np.save('{}-pred_te_qda.np'.format(MODEL_NUMBER), pred_te_qda)

# print('Saving model file')
# f = open("{}models/{}-qda_dict-{}CV.pkl".format(BASE_DIR, MODEL_NUMBER, CV_SCORE), "wb")
# pickle.dump(qda_dict, f)
# f.close()

ss = pd.read_csv('../input/instant-gratification/sample_submission.csv'.format(BASE_DIR))
ss['target'] = pred_te_qda
ss.to_csv('{}-submission-{}CV.csv'.format(MODEL_NUMBER, CV_SCORE), index=False)

oof_df = train[['id','target']].copy()
oof_df[MODEL_NUMBER] = oof_qda
oof_df.to_csv('{}-oof-{}CV.csv'.format(MODEL_NUMBER, CV_SCORE), index=False)

seconds_to_run = datetime.now() - startTime
print('Completed in {:.4f} seconds'.format(seconds_to_run.seconds))
print('Completed in {:.4f} minutes'.format(seconds_to_run.seconds/60))
print('Completed in {:.4f} hours'.format(seconds_to_run.seconds/60/60))
