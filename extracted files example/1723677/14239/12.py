# DISPLAY ENSEMBLE VALIDATION AUC
val_auc = roc_auc_score(train['target'],oof_preds_SVM+oof_preds_NN)
print('Ensemble_NN+SVM_CV = OOF_AUC =',round(val_auc,5))

# PLOT ENSEMBLE TEST PREDICTIONS
plt.hist(test_preds_SVM+test_preds_NN,bins=100)
plt.title('Ensemble NN+SVM test.csv predictions')
plt.show()
