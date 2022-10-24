import math

# FACTORIZE
def factor_data(df_train, df_test, col):
    df_comb = pd.concat([df_train[col],df_test[col]],axis=0)
    df_comb,_ = df_comb.factorize(sort=True)
    # MAKE SMALLEST LABEL 1, RESERVE 0
    df_comb += 1
    # MAKE NAN LARGEST LABEL
    df_comb = np.where(df_comb==0, df_comb.max()+1, df_comb)
    df_train[col] = df_comb[:len(df_train)]
    df_test[col] = df_comb[len(df_train):]
    del df_comb
    mx = max(df_train[col].max(),df_test[col].max())+1
    return mx
    
# OPTIMIZE MEMORY
def reduce_memory(df,col):
    mx = df[col].max()
    if mx<256:
            df[col] = df[col].astype('uint8')
    elif mx<65536:
        df[col] = df[col].astype('uint16')
    else:
        df[col] = df[col].astype('uint32')
    
# LOG FREQUENCY ENCODE
def encode_FE_lg(df,col,verbose=1):
    ln = 1/df[col].nunique()
    vc = (df[col].value_counts(dropna=False, normalize=True)+ln).map(math.log).to_dict()
    nm = col+'_FE_lg'
    df[nm] = df[col].map(vc)
    df[nm] -= df[nm].min()
    df[nm] = df[nm]/df[nm].max()
    df[nm] = df[nm].astype('float32')
    if verbose==1:
        print('FE encoded',col)
    return [nm]

# STATISTICAL CATEGORY ENCODE
def encode_CE(df, col, filter, zscore, tar='HasDetections', m=0.5, verbose=1):
    cv = pd.DataFrame( df[col].value_counts(dropna=False) ).reset_index()
    cv4 = df.groupby(col)[tar].mean().reset_index().rename({tar:'rate',col:'index'},axis=1)
    d1 = set(cv['index'].unique())
    cv = pd.merge(cv,cv4,on='index',how='left')
    if (len( cv[ cv['index'].isna() ])!=0 ):
        cv.loc[ cv['index'].isna(),'rate' ] = df.loc[ df[col].isna(),tar ].mean()
    cv = cv[ cv[col]> (filter * len(df)) ]
    cv['ratec'] = (df[tar].sum() - cv['rate']*cv[col])/(len(df)-cv[col])
    cv['sd'] = zscore * 0.5 / cv[col].map(lambda x: math.sqrt(x))
    cv = cv[ (abs(cv['rate']-m)>=cv['sd']) | (abs(cv['ratec']-1+m)>=cv['sd']) ]
    d2 = set(cv['index'].unique())
    d = list(d1 - d2)
    if (df[col].dtype.name=='category'):
        if (not 0 in df[col].cat.categories):
            df[col].cat.add_categories(0,inplace=True)
        else:
            print('###WARNING CAT 0 ALREADY EXISTS IN',col)
    df.loc[ df[col].isin(d),col ] = 0
    if verbose==1:
        print('CE encoded',col,'-',len(d2),'values. Removed',len(d),'values')
    mx = df[col].nunique()
    return [mx,d2]

# CATEGORY ENCODE FROM KEEP LIST
def encode_CE_test(df,col,d):
    if (df[col].dtype.name=='category'):
        if (not 0 in df[col].cat.categories):
            df[col].cat.add_categories(0,inplace=True)
        else:
            print('###WARNING CAT 0 ALREADY EXISTS IN',col)
    df.loc[ ~df[col].isin(d),col ] = 0
    mx = df[col].nunique()
    return [mx,d]
