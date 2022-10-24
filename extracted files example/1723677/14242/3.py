%%time
# NORMALIZE D COLUMNS
for i in range(1,16):
    if i in [1,2,3,5,9]: continue
    X_train['D'+str(i)] =  X_train['D'+str(i)] - X_train.TransactionDT/np.float32(24*60*60)
    X_test['D'+str(i)] = X_test['D'+str(i)] - X_test.TransactionDT/np.float32(24*60*60) 
       
# LABEL ENCODE
def encode_LE(df1,df2,col,verbose=True):
    df_comb = cudf.concat([df1[col],df2[col]],axis=0)
    df_comb,_ = df_comb.factorize()
    df1[col] = df_comb[:len(df1)].astype('int32')
    df2[col] = df_comb[len(df1):].astype('int32')
    if verbose: print(col,', ',end='')
        
# SET NAN to -1
for i,f in enumerate(X_train.columns):
    # FACTORIZE CATEGORICAL VARIABLES. SET NAN to -1
    if (X_train[f].dtype=='object'): 
        encode_LE(X_train,X_test,f,False)
    elif f in str_type:
        X_train[f].fillna(-1,inplace=True)
        X_test[f].fillna(-1,inplace=True)
    # SHIFT ALL NUMERICS POSITIVE. SET NAN to -1
    elif f not in ['TransactionAmt','TransactionDT','isFraud']:
        mn = np.min((X_train[f].min(),X_test[f].min()))
        X_train[f] -= np.float32(mn)
        X_test[f] -= np.float32(mn)
        X_train[f].fillna(-1,inplace=True)
        X_test[f].fillna(-1,inplace=True)
