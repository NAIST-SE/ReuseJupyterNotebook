# DISPLAY NN VALIDATION AUC
val_auc = metrics.roc_auc_score(y, oof_preds_NN)
print('NN_CV = OOF_AUC =', round( val_auc,5) )
print('Mean_AUC =', round( np.mean(all_auc_NN),5) )

# PLOT NN TEST PREDICTIONS
plt.hist(test_preds_NN,bins=100)
plt.title('NN test.csv predictions')
plt.show()
