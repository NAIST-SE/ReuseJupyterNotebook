# FACTORIZE DATA
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
    
# OPTIMIZE MEMORY
def reduce_memory(df,col):
    mx = df[col].max()
    if mx<256:
            df[col] = df[col].astype('uint8')
    elif mx<65536:
        df[col] = df[col].astype('uint16')
    else:
        df[col] = df[col].astype('uint32')

# REDUCE CATEGORY CARDINALITY
def relax_data(df_train, df_test, col):
    cv1 = pd.DataFrame(df_train[col].value_counts().reset_index().rename({col:'train'},axis=1))
    cv2 = pd.DataFrame(df_test[col].value_counts().reset_index().rename({col:'test'},axis=1))
    cv3 = pd.merge(cv1,cv2,on='index',how='outer')
    cv3['train'].fillna(0,inplace=True)
    cv3['test'].fillna(0,inplace=True)
    factor = len(df_test)/len(df_train)
    cv3['remove'] = False
    cv3['remove'] = cv3['remove'] | (cv3['train'] < len(df_train)/9000)
    cv3['remove'] = cv3['remove'] | (factor*cv3['train'] < cv3['test']/4)
    cv3['remove'] = cv3['remove'] | (factor*cv3['train'] > 4*cv3['test'])
    cv3['new'] = cv3.apply(lambda x: x['index'] if x['remove']==False else 0,axis=1)
    cv3['new'],_ = cv3['new'].factorize(sort=True)
    cv3.set_index('index',inplace=True)
    cc = cv3['new'].to_dict()
    df_train[col] = df_train[col].map(cc)
    reduce_memory(df_train,col)
    df_test[col] = df_test[col].map(cc)
    reduce_memory(df_test,col)
    
# DISPLAY MEMORY STATISTICS
def display_memory(df_train, df_test):
    print(len(df_train),'rows of training data use',df_train.memory_usage(deep=True).sum()//1e6,'Mb memory!')
    print(len(df_test),'rows of test data use',df_test.memory_usage(deep=True).sum()//1e6,'Mb memory!')

# CONVERT DTYPES TO CATEGORIES
def categorize(df_train, df_test, cols):
    for col in cols:
        df_train[col] = df_train[col].astype('category')
        df_test[col] = df_test[col].astype('category')
