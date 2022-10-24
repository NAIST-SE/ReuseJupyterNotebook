# GROUP AGGREGATIONS
def add_feature(df1,df2,uid,col,agg,verbose=True):
    if agg=='count': func = count2
    elif agg=='mean': func = mean2
    elif agg=='std' : func = std2
    elif agg=='nunique': func = nunique2
    else: return
    df1['idx'] = np.arange(len(df1))
    df2['idx'] = np.arange(len(df2))+len(df1)
    temp_df = cudf.concat([df1[[uid,col,'idx']], df2[[uid,col,'idx']]])
    tmp = temp_df.groupby(uid,method='cudf').apply_grouped(
        func,
        incols={col:'x'},
        outcols=dict(y_out=np.float32),
        tpb=32
    ).rename({'y_out':'new'})  
    tmp = tmp.sort_values('idx')
    df1[uid+'_'+col+'_'+agg] = tmp.iloc[:len(df1)].new
    df2[uid+'_'+col+'_'+agg] = tmp.iloc[len(df1):].new
    if verbose: print(uid+'_'+col+'_'+agg,', ',end='')
    df1.drop_column('idx')
    df2.drop_column('idx')
    
def add_features(df1,df2,uids,cols,aggs,verbose=True):
    for col in cols:
        for uid in uids:
            for agg in aggs:
                add_feature(df1,df2,uid,col,agg,verbose)
                
# COMBINE FEATURES
def encode_CB(df1,df2,col1,col2,verbose=True):
    nm = col1+'_'+col2
    df1[nm] = df1[col1].astype(str)+'_'+df1[col2].astype(str)
    df2[nm] = df2[col1].astype(str)+'_'+df2[col2].astype(str) 
    encode_LE(df1,df2,nm,verbose=False)
    if verbose: print(nm,', ',end='')
