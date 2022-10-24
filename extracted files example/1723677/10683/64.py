# GET FREQUENCY ENCODE LIST
FE = []
for col in df_train.columns:
    if col=='HasDetections': continue
    if df_train[col].nunique()>10:
        FE.append(col)

# FEATURE ENGINEER / NEUMERIC ENCODE
NUM = makeNew(df_train,verbose=0,add=1,data=1)
makeNew(df_test,verbose=0,data=2)
print('Engineered '+str(len(NUM))+' variables (including NE)')
ct = len(NUM)+1; cnew = ct
    
# FREQUENCY ENCODE
for x in FE:
    NUM += encode_FE_lg(df_train,x,verbose=0)
    encode_FE_lg(df_test,x,verbose=0)
    #print(str(ct)+': FE: '+x)
    ct += 1
print('Frequency encoded '+str(len(NUM)-cnew)+' variables')
    
# STATISTICAL CATEGORY ENCODE
inps={}; tt = 0
for col in OHE:
    factor_data(df_train,df_test,col)
    d = encode_CE(df_train,col,0.001,1)[1]
    encode_CE_test(df_test,col,d)
    inps[col] = factor_data(df_train,df_test,col)
    tt += inps[col]
    reduce_memory(df_train,col)
    reduce_memory(df_test,col)
    #print(str(ct)+': CE: '+col)
    ct += 1

# REMOVE UNNEEDED
for x in np.unique(NE+MM):
    del df_train[x]
    if x!='AvSigVersion': del df_test[x]
x = gc.collect()

mm = round(df_train.memory_usage(deep=True).sum() / 1024**2)
mm2 = round(df_test.memory_usage(deep=True).sum() / 1024**2)
print('Encoded '+str(len(NUM))+' non-CE variables and '+str(len(OHE))+' CE containing '+str(tt)+' unique values into '+str(mm)+' Mb memory')
print('Test memory is '+str(mm2)+' Mb')
