# SET MAGIC COLUMN AS ALL USEFUL
useful[146,:] = [True]*512

# REMOVE ALL USELESS BLOCKS
for i in range(512):
    idx = train.columns[1:-1][ ~useful[:,i] ]    
    train.loc[ train.iloc[:,147]==i,idx ] = 0.0
    test.loc[ test.iloc[:,147]==i,idx ] = 0.0 
    #if i%25==0: print(i)
