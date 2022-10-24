# LB PROBE 100 VARIABLES STARTING WITH MOST IMPORTANT CV SCORE
df.sort_values('diff',inplace=True,ascending=False)
LBprobe = list(df.loc[ df['diff']>0.04, 'var'])
df.sort_values('var',inplace=True)

# INITIALIZE VARIABLES
df['LB'] = 0.5; df['A'] = 0; ct=0

# PERFORM LB PROBING TO DETERMINE A_K'S
keep = []
for i in LBprobe:
    ct += 1; found = True
    # CALCUATE LB SCORE FOR VAR_K
    df.loc[i,'LB'] = roc_auc_score(public['target'],public[i])
    if (df.loc[i,'LB']<0.47) | (df.loc[i,'LB']>0.53): keep.append(i) 
    else: found = False
    # UPDATE A_K'S
    df.loc[keep,'A'] = (8/9)*df.loc[keep,'LB']+(1/9)*df.loc[keep,'CV']-0.5
    # PREDICT PUBLIC
    predPU = df['A'].values.dot(public.iloc[:,:300].values.transpose())
    aucPU = round( roc_auc_score(public['target'],predPU) ,3)
    # PREDICT PRIVATE
    predPR = df['A'].values.dot(private.iloc[:,:300].values.transpose())
    aucPR = round( roc_auc_score(private['target'],predPR) ,3)
    # DISPLAY CURRENT LB AND PRIVATE SCORE
    if found: print('Submission',ct,': Best LB =',aucPU,'and Private score ='
            ,aucPR,'with',len(keep),'keep')
