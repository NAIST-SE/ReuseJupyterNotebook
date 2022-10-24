if AdjustPrivateScore==1:
    df_test2.loc[ df_test2['Date']>datetime(2018,11,20,4,0) ,'HasDetections'] = 0
elif AdjustPrivateScore==2:
    df_test2['X'] = df_test2['Date'] - datetime(2018,11,20,4,0) 
    df_test2['X'] = df_test2['X'].map(lambda x: x.total_seconds()/86400)
    df_test2['X'].fillna(0,inplace=True)
    s = 5.813888
    df_test2['F'] = 1.0
    df_test2['F'] = 1 - df_test2['X']/s
    df_test2.loc[df_test2['X']<=0,'F'] = 1.0
    df_test2.loc[df_test2['X']>s,'F'] = 0
    df_test2['HasDetections'] *= df_test2['F']
