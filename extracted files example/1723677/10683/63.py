def makeNew(df,verbose=1,add=0,TS=True,data=0):

    old = df.columns
    
    # FEATURE ENGINEER
    df['AppVersion2'] = df['AppVersion'].apply(lambda x: x.split('.')[1]).astype('category')

    if TS:
        from datetime import datetime, date, timedelta

        # AS timestamp
        datedictAS = np.load('../input/malware-timestamps/AvSigVersionTimestamps.npy')[()]
        df['DateAS'] = df['AvSigVersion'].map(datedictAS)

        # OS timestamp
        datedictOS = np.load('../input/malware-timestamps-2/OSVersionTimestamps.npy')[()]
        df['DateOS'] = df['Census_OSVersion'].map(datedictOS)

        df['Lag1'] = df['DateAS'] - df['DateOS']
        df['Lag1'] = df['Lag1'].map(lambda x: x.days//7)
        df['Lag1'] = df['Lag1']/52.0
        df['Lag1'] = df['Lag1'].astype('float32')
        df['Lag1'].fillna(0,inplace=True)
        
        if data!=0:
            if data==1:
                df['Lag5'] = datetime(2018,7,26) - df['DateAS'] # TRAIN
            elif data==2:
                df['Lag5'] = datetime(2018,9,27) - df['DateAS'] #PUBLIC TEST
            elif data==3:
                df['Lag5'] = datetime(2018,10,27) - df['DateAS'] #PRIVATE TEST
            df['Lag5'] = df['Lag5'].map(lambda x: x.days//1)
            df.loc[ df['Lag5']<0, 'Lag5' ] = 0
            df['Lag5'] = df['Lag5']/365.0
            df['Lag5'] = df['Lag5'].astype('float32')
            df['Lag5'].fillna(0,inplace=True)

        del df['DateAS'], df['DateOS']
        del datedictAS, datedictOS
        x=gc.collect()
    
    # NUMERIC ENCODE NE VARIABLES
    for col in NE:
        nm = col+'_NE'
        df[nm] = df[col].astype('float32')
        df[nm] /= np.std(df[nm])
    new = list(set(df.columns)-set(old))
    ret = []
    for x in new:
        if str(df[x].dtype)=='category': # if cat
            if add==1: OHE.append(x)
        else: 
            ret.append(x)
            df[x].fillna(df[x].mean(),inplace=True)
    if verbose==1:
        print('Engineered',len(new),'new features!')
    return ret
