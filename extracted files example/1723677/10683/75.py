import calendar, math

def dynamicPlot(data,col, target='HasDetections', start=datetime(2018,4,1), end=datetime(2018,12,1)
                ,inc_hr=0,inc_dy=7,inc_mn=0,show=0.99,top=5,top2=4,title='',legend=1,z=0,dots=False):
    # check for timestamps
    if 'Date' not in data:
        print('Error dynamicPlot: DataFrame needs column Date of datetimes')
        return
    
    # remove detection line if category density is too small
    cv = data[(data['Date']>start) & (data['Date']<end)][col].value_counts(dropna=False)
    cvd = cv.to_dict()
    nm = cv.index.values
    th = show * len(data)
    sum = 0; lnn2 = 0
    for x in nm:
        lnn2 += 1
        sum += cvd[x]
        if sum>th:
            break
    top = min(top,len(nm))
    top2 = min(top2,len(nm),lnn2,top)

    # calculate rate within each time interval
    diff = (end-start).days*24*3600 + (end-start).seconds
    size = diff//(3600*((inc_mn * 28 + inc_dy) * 24 + inc_hr)) + 5
    data_counts = np.zeros([size,2*top+1],dtype=float)
    idx=0; idx2 = {}
    for i in range(top):
        idx2[nm[i]] = i+1
    low = start
    high = add_time(start,inc_mn,inc_dy,inc_hr)
    data_times = [low+(high-low)/2]
    while low<end:
        slice = data[ (data['Date']<high) & (data['Date']>=low) ]
        #data_counts[idx,0] = len(slice)
        data_counts[idx,0] = 5000*len(slice['AvSigVersion'].unique())
        for key in idx2:
            if nan_check(key): slice2 = slice[slice[col].isna()]
            else: slice2 = slice[slice[col]==key]
            data_counts[idx,idx2[key]] = len(slice2)
            if target in data:
                data_counts[idx,top+idx2[key]] = slice2['HasDetections'].mean()
        low = high
        high = add_time(high,inc_mn,inc_dy,inc_hr)
        data_times.append(low+(high-low)/2)
        idx += 1

    # plot lines
    fig = plt.figure(1,figsize=(15,3))
    cl = ['r','g','b','y','m']
    ax3 = fig.add_subplot(1,1,1)
    lines = []; labels = []
    if z==1: ax3.plot(data_times,data_counts[0:idx+1,0],'k')
    for i in range(top):
        tmp, = ax3.plot(data_times,data_counts[0:idx+1,i+1],cl[i%5])
        if dots: ax3.plot(data_times,data_counts[0:idx+1,i+1],cl[i%5]+'o')
        lines.append(tmp)
        labels.append(str(nm[i]))
    ax3.spines['left'].set_color('red')
    ax3.yaxis.label.set_color('red')
    ax3.tick_params(axis='y', colors='red')
    if col!='ones': ax3.set_ylabel('Category Density', color='r')
    else: ax3.set_ylabel('Data Density', color='r')
    #ax3.set_yticklabels([])
    if target in data:
        ax4 = ax3.twinx()
        for i in range(top2):
            ax4.plot(data_times,data_counts[0:idx+1,i+1+top],cl[i%5]+":")
            if dots: ax4.plot(data_times,data_counts[0:idx+1,i+1+top],cl[i%5]+"o")
        ax4.spines['left'].set_color('red')
        ax4.set_ylabel('Detection Rate', color='k')
    if title!='': plt.title(title)
    if legend==1: plt.legend(lines,labels,loc=2)
    plt.show()
        
# INCREMENT A DATETIME
def add_time(sdate,months=0,days=0,hours=0):
    month = sdate.month -1 + months
    year = sdate.year + month // 12
    month = month % 12 + 1
    day = sdate.day + days
    if day>calendar.monthrange(year,month)[1]:
        day -= calendar.monthrange(year,month)[1]
        month += 1
        if month>12:
            month = 1
            year += 1
    hour = sdate.hour + hours
    if hour>23:
        hour = 0
        day += 1
        if day>calendar.monthrange(year,month)[1]:
            day -= calendar.monthrange(year,month)[1]
            month += 1
            if month>12:
                month = 1
                year += 1
    return datetime(year,month,day,hour,sdate.minute)

# CHECK FOR NAN
def nan_check(x):
    if isinstance(x,float):
        if math.isnan(x):
            return True
    return False
