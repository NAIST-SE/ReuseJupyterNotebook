import math, calendar
import matplotlib.pyplot as plt
from datetime import datetime

# PARAMETERS
# data : pandas.DataFrame : your data to plot
# col  : str : which column to plot histogram for left y-axis
# target : str : which column for mean/rate on right y-axis
# bars : int : how many histogram bars to show (or less if you set show or min)
# show : float : stop displaying bars after 100*show% of data is showing
# minn : float : don't display bars containing under 100*minn% of data
# sortby : str : either 'frequency', 'category', or 'rate'
# verbose : int : display text summary 1=yes, 0=no
# top : int : give this many bars nice color (and matches a subsequent dynamicPlot)
# title : str : title of plot
# asc : boolean : sort ascending (for category and rate)
# dropna : boolean : include missing data as a category or not

def staticPlot(data, col, target='HasDetections', bars=10, show=1.0, sortby='frequency'
               , verbose=1, top=5, title='',asc=False, dropna=False, minn=0.0):
    # calcuate density and detection rate
    cv = data[col].value_counts(dropna=dropna)
    cvd = cv.to_dict()
    nm = cv.index.values; lnn = len(nm); lnn2 = lnn
    th = show * len(data)
    th2 = minn * len(data)
    sum = 0; lnn2 = 0
    for x in nm[0:bars]:
        lnn2 += 1
        try: sum += cvd[x]
        except: sum += cv[x]
        if sum>th:
            break
        try:
            if cvd[x]<th2: break
        except:
            if cv[x]<th2: break
    if lnn2<bars: bars = lnn2
    pct = round(100.0*sum/len(data),2)
    lnn = min(lnn,lnn2)
    ratio = [0.0]*lnn; lnn3 = lnn
    if sortby =='frequency': lnn3 = min(lnn3,bars)
    elif sortby=='category': lnn3 = 0
    for i in range(lnn3):
        if target not in data:
            ratio[i] = np.nan
        elif nan_check(nm[i]):
            ratio[i] = data[target][data[col].isna()].mean()
        else:
            ratio[i] = data[target][data[col]==nm[i]].mean()
    try: all = pd.DataFrame( {'category':nm[0:lnn],'frequency':[cvd[x] for x in nm[0:lnn]],'rate':ratio} )
    except: all = pd.DataFrame( {'category':nm[0:lnn],'frequency':[cv[x] for x in nm[0:lnn]],'rate':ratio} )
    if sortby=='rate': 
        all = all.sort_values(sortby, ascending=asc)
    elif sortby=='category':
        try: 
            all['temp'] = all['category'].astype('float')
            all = all.sort_values('temp', ascending=asc)
        except:
            all = all.sort_values('category', ascending=asc)
    if bars<lnn: all = all[0:bars]
    if verbose==1 and target in data:
        print('TRAIN.CSV variable',col,'has',len(nm),'categories')
        print('The',min(bars,lnn),'bars displayed here contain',pct,'% of data.')
        mlnn = data[col].isna().sum()
        print("The data has %.1f %% NA. The plot is sorted by " % (100.0*mlnn/len(data)) + sortby )
    
    # plot density and detection rate
    fig = plt.figure(1,figsize=(15,3))
    ax1 = fig.add_subplot(1,1,1)
    clrs = ['red', 'green', 'blue', 'yellow', 'magenta']
    barss = ax1.bar([str(x) for x in all['category']],[x/float(len(data)) for x in all['frequency']],color=clrs)
    for i in range(len(all)-top):
        barss[top+i].set_color('cyan')
    if target in data:
        ax2 = ax1.twinx()
        if sortby!='category': infected = all['rate'][0:lnn]
        else:
            infected=[]
            for x in all['category']:
                if nan_check(x): infected.append( data[ data[col].isna() ][target].mean() )
                elif cvd[x]!=0: infected.append( data[ data[col]==x ][target].mean() )
                else: infected.append(-1)
        ax2.plot([str(x) for x in all['category']],infected[0:lnn],'k:o')
        #ax2.set_ylim(a,b)
        ax2.spines['left'].set_color('red')
        ax2.set_ylabel('Detection Rate', color='k')
    ax1.spines['left'].set_color('red')
    ax1.yaxis.label.set_color('red')
    ax1.tick_params(axis='y', colors='red')
    ax1.set_ylabel('Category Proportion', color='r')
    if title!='': plt.title(title)
    plt.show()
    if verbose==1 and target not in data:
        print('TEST.CSV variable',col,'has',len(nm),'categories')
        print('The',min(bars,lnn),'bars displayed here contain',pct,'% of the data.')
        mlnn = data[col].isna().sum()
        print("The data has %.1f %% NA. The plot is sorted by " % (100.0*mlnn/len(data)) + sortby )
        
# CHECK FOR NAN
def nan_check(x):
    if isinstance(x,float):
        if math.isnan(x):
            return True
    return False
