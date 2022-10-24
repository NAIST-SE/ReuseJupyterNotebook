u0 = initial
angDeg = 5
angRad = 2*np.pi*angDeg/360

np.random.seed(42)
for k in range(150):
    # CHOOSE RANDOM SEARCH DIRECTION
    u1 = np.random.normal(0,1,300)
    # REMOVE 250 UNIMPORTANT DIMENSIONS
    u1[ df.iloc[100:,0] ] = 0.0
    # ROTATE 5 DEGREES IN THIS NEW DIRECTION
    u1 = u1 - u1.dot(u0)*u0
    u1 = u1 / np.sqrt(u1.dot(u1))
    u2 = u0*np.cos(angRad) + u1*np.sin(angRad)
    # CALCULATE LB AND PRIVATE SCORE
    aucPU = round(roc_auc_score(public['target'],u2.dot(public.iloc[:,:-1].values.transpose())),5)
    aucPR = round(roc_auc_score(private['target'],u2.dot(private.iloc[:,:-1].values.transpose())),5)
    # IF SCORE INCREASES PRINT RESULTS
    if (aucPU>bestPU)|(k==0):
        bestPU = aucPU
        currentPR = aucPR
        u0 = u2.copy()
        print('Submission',k+1,': Best LB =',bestPU,'and Private score =',currentPR)
