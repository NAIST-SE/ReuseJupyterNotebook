# FIND NORMAL TO HYPERPLANE
clf = LogisticRegression(solver='liblinear',penalty='l2',C=0.1,class_weight='balanced')
clf.fit(train.iloc[:,2:],train['target'])
u1 = clf.coef_[0]
u1 = u1/np.sqrt(u1.dot(u1))
