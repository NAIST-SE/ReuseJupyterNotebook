step = 0.2
pt = [[],[],[],[],[]]
cuts = [[],[],[],[],[]]
for g in range(5):
    mn = train.loc[train.group==g].signal.min()
    mx = train.loc[train.group==g].signal.max()
    old = 0
    for x in np.arange(mn,mx+step,step):
        sg = train.loc[(train.group==g)&(train.signal>x-step/2)&(train.signal<x+step/2)].open_channels.values
        if len(sg)>100:
            m = mode(sg)[0][0]
            pt[g].append((x,m))
            if m!=old: cuts[g].append(x-step/2)
            old = m
    pt[g] = np.vstack(pt[g])
    
models = ['1 channel low prob','1 channel high prob','3 channel','5 channel','10 channel']
plt.figure(figsize=(15,8))
for g in range(5):
    plt.plot(pt[g][:,0],pt[g][:,1],'-o',label='Group %i (%s model)'%(g,models[g]))
plt.legend()
plt.title('Traing Data Open Channels versus Clean Signal Value',size=16)
plt.xlabel('Clean Signal Value',size=16)
plt.ylabel('Open Channels',size=16)
plt.show()
