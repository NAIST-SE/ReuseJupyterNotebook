cols = []; dd = []

# ENCODE NEW
for x in FE:
    cols += encode_FE(df_train,x)
for x in OHE:
    tmp = encode_OHE(df_train,x,0.005,5)
    cols += tmp[0]; dd.append(tmp[1])
print('Encoded',len(cols),'new variables')

# REMOVE OLD
for x in FE+OHE:
    del df_train[x]
print('Removed original',len(FE+OHE),'variables')
x = gc.collect()
