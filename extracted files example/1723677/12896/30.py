auc = []
target = np.ones(250); target[:90] = 0.0
for i in range(10000):
    useless = np.random.normal(0,1,250)
    auc.append( roc_auc_score(target,useless) )
    #if i%1000==0: print(i)
z = 1.28 # 80% CE, 1.645 is 90% CE
low = round( 0.500 - z * np.std(auc),3)
high = round( 0.500 + z * np.std(auc),3)
print('80% of useless AUC are between',low,'and',high)
plt.hist(auc,bins=100); plt.show()
