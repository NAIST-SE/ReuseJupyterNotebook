import warnings
warnings.filterwarnings("ignore")
import seaborn as sns, matplotlib.pyplot as plt
from matplotlib import gridspec

# KERNEL DENSITY BANDWITHS
n = [1000,1000,50000,25000,50,1000,1e6,1e6,5,2]
# DENSITY X RANGES
s = [(1,10000),(0,0),(0,0),(700000,950000),(1,750),(1,10000),(1,2e7),(1,2e7),(0,0),(0,0)]
# REMOVE NAN
df_train = df_train[ df_train['AvSigVersion']!='0.0.0.0' ]
# TEXT FORMATTING
def cc(l):
    for i in range(len(l)): 
        l[i] = '< ('+str(i)+') < '+str(l[i])
    return l
# DISCRETIZING FUNCTION FROM 
# https://www.kaggle.com/guoday/nffm-baseline-0-690-on-lb
def make_bucket(data,num=10):
    data.sort()
    bins=[]
    for i in range(num):
        bins.append(data[int(len(data)*(i+1)//num)-1])
    return bins

ct=0
for col in list(data.columns)[1:]:
    print('###############################################')
    print('###     '+col)
    print('###############################################')
    
    # TIME SERIES PLOT
    plt.figure(figsize=(15,5))
    plt.plot(data['WeekOf'],data[col])
    plt.xlabel('Time')
    plt.ylabel(col)
    plt.title('"'+col+'" versus time')
    plt.show()
    
    # HASDETECTION HISTOGRAM
    bins = make_bucket(df_train[col].copy().values,num=20)
    df_train['P']=np.digitize(df_train[col],bins=bins)
    staticPlot(df_train[ df_train['P']!=20 ],'P',sortby='category',asc=True,bars=20,verbose=0,
               title='HasDetections Rate versus "'+col+'" (Bars use left y-axis. Dotted line uses right)')
    print('KEY TO BINS:',col,cc(bins))
    
    # DENSITY PLOT AND BOXPLOT
    lines = [1, 0]
    plt.figure(figsize=(15,5))
    gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1]) 
    plt.subplot(gs[0])
    for line in lines:
        subset = df_train[ (df_train['HasDetections'] == line) & (~df_train[col].isna())]
        sns.kdeplot(subset[col], bw=n[ct],
                     shade=True, linewidth=3, 
                     label = line)
    plt.legend(prop={'size': 16}, title = 'HasDetections')
    plt.title('Density Plot of HasDetections versus "'+col+'"')
    plt.xlabel(col)
    if s[ct][0]!=0: plt.xlim((s[ct][0],s[ct][1]))
    plt.ylabel('Density')
    ax = plt.subplot(gs[1])
    df_train2 = df_train[ ~df_train[col].isna() ]
    plt.boxplot([df_train2[ df_train2['HasDetections']==0][col],df_train2[ df_train2['HasDetections']==1][col]])
    plt.title('Boxplot of "'+col+'"')
    if s[ct][0]!=0: plt.ylim((s[ct][0],s[ct][1]))
    ct += 1
    plt.xlabel('HasDetections')
    ax.set_xticklabels([0,1])
    plt.show()
del df_train['P']
