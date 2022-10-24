outliers = []
target = np.ones(250); target[:90] = 0.0
for i in range(1000):
    ct = 0
    for j in range(300):
        useless = np.random.normal(0,1,250)
        auc = roc_auc_score(target,useless)
        if (auc<low)|(auc>high): ct += 1
    outliers.append(ct)
    #if i%100==0: print(i)
plt.hist(outliers,bins=100); plt.show()
mn = np.mean(outliers); st = np.std(outliers)
lw = round(mn-z*st,1); hg = round(mn+z*st,1)
print('We are 80% confident that between',lw,'and',hg,
      'useless variables have AUC less than',low,'or greater than',high)
