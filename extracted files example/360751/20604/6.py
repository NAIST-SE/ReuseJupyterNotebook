%matplotlib inline

plt.figure(figsize=(12,8))
plt.style.use('seaborn-whitegrid')
SMALL_SIZE = 16
MEDIUM_SIZE = 18
BIGGER_SIZE = 24
plt.rc('font', size=SMALL_SIZE)
plt.rc('axes', titlesize=MEDIUM_SIZE)
plt.rc('axes', labelsize=MEDIUM_SIZE)
plt.rc('xtick', labelsize=MEDIUM_SIZE)
plt.rc('ytick', labelsize=MEDIUM_SIZE)
plt.rc('legend', fontsize=SMALL_SIZE)
plt.rc('figure', titlesize=BIGGER_SIZE)


p1 = kmf1.plot()
p2 = kmf2.plot(ax=p1)


plt.xlim(-5, 118)
plt.title("Maintaining Lung Capacity")
plt.xlabel("Weeks since baseline CT")
plt.ylabel("Fraction of Group with above average FVC")
plt.show()
