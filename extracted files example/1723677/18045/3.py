test = pd.read_csv('/kaggle/input/data-without-drift/test_clean.csv')
test['group'] = -1
x = [[(0,100000),(300000,400000),(800000,900000),(1000000,2000000)],[(400000,500000)], 
     [(100000,200000),(900000,1000000)],[(200000,300000),(600000,700000)],[(500000,600000),(700000,800000)]]
for k in range(5):
    for j in range(len(x[k])): test.iloc[x[k][j][0]:x[k][j][1],2] = k
        
res = 400
plt.figure(figsize=(20,5))
plt.plot(test.time[::res],test.signal[::res])
plt.plot(test.time,test.group,color='black')
plt.title('Clean Test Data. Blue line is signal. Black line is group number.')
plt.xlabel('time'); plt.ylabel('signal')
plt.show()
