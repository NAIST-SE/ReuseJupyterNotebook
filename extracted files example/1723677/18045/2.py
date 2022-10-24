train = pd.read_csv('/kaggle/input/data-without-drift/train_clean.csv')
train['group'] = -1
x = [(0,500000),(1000000,1500000),(1500000,2000000),(2500000,3000000),(2000000,2500000)]
for k in range(5): train.iloc[x[k][0]:x[k][1],3] = k
    
res = 1000
plt.figure(figsize=(20,5))
plt.plot(train.time[::res],train.signal[::res])
plt.plot(train.time,train.group,color='black')
plt.title('Clean Train Data. Blue line is signal. Black line is group number.')
plt.xlabel('time'); plt.ylabel('signal')
plt.show()
