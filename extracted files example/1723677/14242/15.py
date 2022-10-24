plt.hist(oof,bins=100)
plt.ylim((0,5000))
plt.title('XGB OOF')
plt.show()

X_train['oof'] = oof
X_train = X_train.reset_index()
X_train[['TransactionID','oof']].to_pandas().to_csv('oof_xgb_96.csv')
X_train = X_train.set_index('TransactionID',drop=True)
