data1 = test.loc[test.group==4].iloc[3:]
data1.reset_index(inplace=True)

data2 = train.loc[train.group==4].iloc[3:]
data2.reset_index(inplace=True)

for j in range(5):
    r = np.random.randint(data1.shape[0])
    distances, indices = model.kneighbors(X_test[r:r+1,])

    row=2; 
    plt.figure(figsize=(16,row*4))
    for k in range(row*4):
        if k in [1,2,3]: continue
        plt.subplot(row,4,k+1)
        if k==0: 
            xx,yy = wiggle(data1,r,plt)
            g = data1.loc[r,'group']
            rw = data1.loc[r,'index']
            plt.title('UNKNOWN Test row %i group %i'%(rw,g))
        else:
            r=indices[0,k-4].astype('int')
            wiggle(data2,r,plt,xx,yy)
            g = data2.loc[r,'group']
            rw = data2.loc[r,'index']
            t = data2.loc[r,'open_channels']
            plt.title('LABEL = %i. Train row %i group %i'%(t,rw,g))
        if k%4==0: plt.ylabel('signal')
    plt.tight_layout(pad=3.0)
    plt.show()
