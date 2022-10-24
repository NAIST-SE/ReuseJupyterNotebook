def wiggle(df, row, plt, xx=None, yy=None):
    plt.plot([-3,-2,-1,0,1,2,3],df.loc[df.index[row-3:row+4],'signal'],'-')
    sizes = np.array([1,2,3,12,3,2,1])*50
    colors = ['red','red','red','green','blue','blue','blue']
    for k in range(7):
        plt.scatter(k-3,df.loc[df.index[row+k-3],'signal'],s=sizes[k],color=colors[k])
    if xx!=None: plt.xlim(xx)
    if yy!=None: plt.ylim(yy)
    return plt.xlim(),plt.ylim()

row=2; col=4;
np.random.seed(42)
plt.figure(figsize=(4*col,4*row))
for k in range(row*col):
    plt.subplot(row,col,k+1)
    r = np.random.randint(2e6)
    wiggle(test,r,plt)
    if k%col==0: plt.ylabel('signal')
    g = test.loc[r,'group']
    plt.title('Test row %i group %i'%(r,g))
plt.tight_layout(pad=3.0)
plt.show()
