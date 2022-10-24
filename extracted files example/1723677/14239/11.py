# DISPLAY SVM VALIDATION AUC
val_auc = roc_auc_score(train['target'],oof_preds_SVM)
print('SVM_CV = OOF_AUC =',round(val_auc,5))

# PLOT SVM TEST PREDICTIONS
plt.hist(test_preds_SVM,bins=100)
plt.title('SVM test.csv predictions')
plt.show()
