# ORIGINAL TRAIN DATA
plt.figure(figsize=(20,5))
r = train.signal.rolling(30000).mean()
plt.plot(train.time.values,r)
for i in range(11): plt.plot([i*50,i*50],[-3,8],'r:')
for j in range(10): plt.text(j*50+20,6,str(j+1),size=20)
plt.title('Training Signal Rolling Mean. Has Drift wherever plot is not horizontal line',size=16)
plt.show()

# TRAIN DATA WITHOUT DRIFT
plt.figure(figsize=(20,5))
r = train2.signal.rolling(30000).mean()
plt.plot(train2.time.values,r)
for i in range(11): plt.plot([i*50,i*50],[-3,8],'r:')
for j in range(10): plt.text(j*50+20,6,str(j+1),size=20)
plt.title('Training Signal Rolling Mean without Drift',size=16)
plt.show()
