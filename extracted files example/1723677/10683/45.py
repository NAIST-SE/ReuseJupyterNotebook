# COMPARE VALUE DENSITIES FROM TWO DIFFERENT DATAFRAMES
#
# PARAMETERS
# df1: pandas.DataFrame containing variable
# df2: pandas.DataFrame containing variable
# col: column to compare between df1 and df2
# override: set to False to prevent display when variables similar
# verbose: display text summary
# scale: zooms y-axis
# title: plot title
# lab1: legend label for df1
# lab2: legend label for df2
# prefix: pre text for verbose summary
#
def comparePlot(df1, df2, col, factor=4, override=True, verbose=True, scale=0.5, title='',
                lab1='', lab2='', prefix=''):
    cv1 = pd.DataFrame(df1[col].value_counts(normalize=True).reset_index().rename({col:'train'},axis=1))
    cv2 = pd.DataFrame(df2[col].value_counts(normalize=True).reset_index().rename({col:'test'},axis=1))
    cv3 = pd.merge(cv1,cv2,on='index',how='outer')
    cv3['train'].fillna(0,inplace=True)
    cv3['test'].fillna(0,inplace=True)
    cv3 = cv3.iloc[np.lexsort((cv3['test'], -cv3['train']))]
    cv3['total'] = cv3['train']+cv3['test']
    cv3['trainMX'] = cv3['train']*factor
    cv3['trainMN'] = cv3['train']/factor
    cv3 = cv3[cv3['total']>0.0001]
    if (len(cv3)<5): return
    cv3.reset_index(inplace=True)
    MX = (cv3['test'] > cv3['trainMX'])
    mxSum = round(100*cv3.loc[MX,'test'].sum(),1)
    MN = (cv3['test'] < cv3['trainMN'])
    mnSum = round(100*cv3.loc[MN,'test'].sum(),1)
    #if override | (MX.sum()+MN.sum()>0):
    if override | (mxSum + mnSum > 1):
        plt.figure(figsize=(15,5))
        if lab1=='': lab1='Train'
        if lab2=='': lab2='Test'
        plt.plot(cv3.index,cv3['train'],linewidth=3,alpha=0.7,color='b',label=lab1)
        plt.plot(cv3.index,cv3['trainMX'],linewidth=2,alpha=1.0,linestyle=':',color='b',label=str())
        plt.plot(cv3.index,cv3['trainMN'],linewidth=2,alpha=1.0,linestyle=':',color='b',label=str())
        #plt.bar(cv3.index,cv3['test'],linewidth=3,alpha=0.7,color='g', label='Test.csv')
        plt.plot(cv3.index,cv3['test'],linewidth=3,alpha=0.7,color='g',label=lab2)
        plt.legend()
        if title=='': plt.title(col)
        else: plt.title(col+' - '+title)
        plt.xlabel(col+' values (ordered by train frequency and relabeled)')
        plt.ylabel('Frequency')
        mx = max(cv3['train'].max(),cv3['test'].max())
        #plt.ylim(0,mx*1.05)
        plt.ylim(0,mx*scale)
        plt.show()
        tempMX = cv3.loc[MX.values,['index','test']].sort_values('test',ascending=False)['index']
        tempMN = cv3.loc[MN.values,['index','test']].sort_values('test',ascending=False)['index']
        if verbose:
            if MX.sum()>0:    
                print(prefix+'Test.csv',col,'has',MX.sum(),'values 4x MORE freq than Train.csv. (',mxSum,'% of data)')
            if MX.sum()>10: print('  Top 10 by test freq:',list(tempMX)[:10])
            elif MX.sum()>0: print(list(tempMX)[:10])
            if MN.sum()>0:
                print(prefix+'Test.csv',col,'has',MN.sum(),'values 4x LESS freq than Train.csv. (',mnSum,'% of data)')
            if MN.sum()>10: print('  Top 10 by test freq:',list(tempMN)[:10])
            elif MN.sum()>0: print(list(tempMN)[:10])
    return
