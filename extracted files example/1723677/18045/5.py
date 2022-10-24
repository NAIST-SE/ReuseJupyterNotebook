import warnings
warnings.filterwarnings("ignore")
for g in range(5):
    if g==0: res = 100
    else: res = 10

    plt.figure(figsize=(16,8))
    plt.subplot(1,2,1)
    for k in range(0,11):
        idx = np.array( train.loc[(train.open_channels==k) & (train.group==g)].index )
        if len(idx)==0: continue
        plt.scatter(train.signal[idx-1],train.signal[idx],s=0.01,label='%i open channels'%k)
    plt.xlabel('Previous Signal Value',size=14)
    plt.ylabel('Signal Value',size=14)
    lgnd = plt.legend(numpoints=1, fontsize=10)
    for k in range( len(lgnd.legendHandles) ):
        lgnd.legendHandles[k]._sizes = [30]
    
    data = test.loc[test.group==g]
    #plt.scatter(data.signal[:-1][::res],data.signal[1:][::res],s=0.1,color='black')
    xx = plt.xlim(); yy = plt.ylim()
    for k in range(len(cuts[g])):
        if (g!=4)|(k!=0): plt.plot([xx[0],xx[1]],[cuts[g][k],cuts[g][k]],':',color='black')
    plt.title('Train Data in group %i'%g,size=16)
    
    plt.subplot(1,2,2)
    plt.scatter(data.signal[:-1][::res],data.signal[1:][::res],s=0.1,color='black')
    plt.xlim(xx); plt.ylim(yy)
    for k in range(len(cuts[g])):
        if (g!=4)|(k!=0): plt.plot([xx[0],xx[1]],[cuts[g][k],cuts[g][k]],':',color='black')
        if (g==4)&(k!=0): plt.text(xx[0]+1,cuts[g][k],'%i open channels'%(k+2),size=12)
        elif g!=4: plt.text(xx[0]+1,cuts[g][k],'%i open channels'%(k+1),size=14)
    plt.xlabel('Previous Signal Value',size=14)
    plt.ylabel('Signal Value',size=14)
    plt.title('Unknown Test Data in group %i'%g,size=16)

    plt.show()
