for myplace in ['Iran']:

    # Confirmed Cases
    fig, axs = plt.subplots(1, 2, figsize=(15, 3))
    dat = tt.query('Place == @myplace and Days_Since_Ten_Cases >= 0')[['Days_Since_Ten_Cases','ConfirmedCases']].dropna()
    dat = dat.iloc[-10:]
    X = dat['Days_Since_Ten_Cases']
    y = dat['ConfirmedCases']
    y = y.cummax()
    dat_all = tt.query('Place == @myplace and Days_Since_Ten_Cases >= 0')[['Days_Since_Ten_Cases','ConfirmedCases']]
    X_pred = dat_all['Days_Since_Ten_Cases']
    en = ElasticNet()
    en.fit(X.values.reshape(-1, 1), y.values)
    preds = en.predict(X_pred.values.reshape(-1, 1))
    tt.loc[(tt['Place'] == myplace) & (tt['Days_Since_Ten_Cases'] >= 0), 'ConfirmedCases_Pred1'] = preds
    # Cap at 10 % Population
    pop_myplace = tt.query('Place == @myplace')['Population_final'].values[0]
    tt.loc[(tt['Place'] == myplace) & (tt['ConfirmedCases_Pred1'] > (0.1 * pop_myplace)), 'ConfirmedCases_Pred1'] = (0.1 * pop_myplace)
    ax = tt.query('Place == @myplace').set_index('Date')[['ConfirmedCases','ConfirmedCases_Pred1']].plot(figsize=(15, 5), title=myplace, ax=axs[0])
    # Fatalities
    # If low count then do percent of confirmed:
    dat = tt.query('Place == @myplace and Days_Since_Ten_Cases >= 0')[['Days_Since_Ten_Cases','Fatalities']].dropna()
    dat = dat.iloc[-10:]
    if len(dat) < 5:
        tt.loc[(tt['Place'] == myplace), 'Fatalities_Pred1'] = tt.loc[(tt['Place'] == myplace)]['ConfirmedCases_Pred1'] * 0.001
    elif tt.query('Place == @myplace')['Fatalities'].max() < 5:
        tt.loc[(tt['Place'] == myplace), 'Fatalities_Pred1'] = tt.loc[(tt['Place'] == myplace)]['ConfirmedCases_Pred1'] * 0.001
    else:
        X = dat['Days_Since_Ten_Cases']
        y = dat['Fatalities']
        y = y.cummax()
        dat_all = tt.query('Place == @myplace and Days_Since_Ten_Cases >= 0')[['Days_Since_Ten_Cases','Fatalities']]
        X_pred = dat_all['Days_Since_Ten_Cases']
        en = ElasticNet()
        en.fit(X.values.reshape(-1, 1), y.values)
        preds = en.predict(X_pred.values.reshape(-1, 1))
        tt.loc[(tt['Place'] == myplace) & (tt['Days_Since_Ten_Cases'] >= 0), 'Fatalities_Pred1'] = preds

        # Cap at 0.0001 Population
        pop_myplace = tt.query('Place == @myplace')['Population_final'].values[0]
        tt.loc[(tt['Place'] == myplace) & (tt['Fatalities_Pred1'] > (0.0005 * pop_myplace)), 'Fatalities_Pred1'] = (0.0005 * pop_myplace)

    ax = tt.query('Place == @myplace').set_index('Date')[['Fatalities','Fatalities_Pred1']].plot(figsize=(15, 5), title=myplace, ax=axs[1])
    plt.show()
