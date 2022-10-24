from sklearn.linear_model import LinearRegression, ElasticNet

for myplace in tt['Place'].unique():
    try:
        # Confirmed Cases
        fig, axs = plt.subplots(1, 2, figsize=(15, 3))
        dat = tt.query('Place == @myplace and Days_Since_Ten_Cases >= 0')[['Days_Since_Ten_Cases','ConfirmedCases_Log']].dropna()
        X = dat['Days_Since_Ten_Cases']
        y = dat['ConfirmedCases_Log']
        y = y.cummax()
        dat_all = tt.query('Place == @myplace and Days_Since_Ten_Cases >= 0')[['Days_Since_Ten_Cases','ConfirmedCases_Log']]
        X_pred = dat_all['Days_Since_Ten_Cases']
        en = ElasticNet()
        en.fit(X.values.reshape(-1, 1), y.values)
        preds = en.predict(X_pred.values.reshape(-1, 1))
        tt.loc[(tt['Place'] == myplace) & (tt['Days_Since_Ten_Cases'] >= 0), 'ConfirmedCases_Log_Pred1'] = preds
        tt.loc[(tt['Place'] == myplace), 'ConfirmedCases_Pred1'] = tt['ConfirmedCases_Log_Pred1'].apply(np.expm1)
        # Cap at 10 % Population
        pop_myplace = tt.query('Place == @myplace')['Population_final'].values[0]
        tt.loc[(tt['Place'] == myplace) & (tt['ConfirmedCases_Pred1'] > (0.05 * pop_myplace)), 'ConfirmedCases_Pred1'] = (0.05 * pop_myplace)
        ax = tt.query('Place == @myplace').set_index('Date')[['ConfirmedCases','ConfirmedCases_Pred1']].plot(figsize=(15, 5), title=myplace, ax=axs[0])
        # Fatalities
        # If low count then do percent of confirmed:
        dat = tt.query('Place == @myplace and Days_Since_Ten_Cases >= 0')[['Days_Since_Ten_Cases','Fatalities_Log']].dropna()
        if len(dat) < 5:
            tt.loc[(tt['Place'] == myplace), 'Fatalities_Pred1'] = tt.loc[(tt['Place'] == myplace)]['ConfirmedCases_Pred1'] * 0.0001
        elif tt.query('Place == @myplace')['Fatalities'].max() < 5:
            tt.loc[(tt['Place'] == myplace), 'Fatalities_Pred1'] = tt.loc[(tt['Place'] == myplace)]['ConfirmedCases_Pred1'] * 0.0001
        else:
            X = dat['Days_Since_Ten_Cases']
            y = dat['Fatalities_Log']
            y = y.cummax()
            dat_all = tt.query('Place == @myplace and Days_Since_Ten_Cases >= 0')[['Days_Since_Ten_Cases','Fatalities_Log']]
            X_pred = dat_all['Days_Since_Ten_Cases']
            en = ElasticNet()
            en.fit(X.values.reshape(-1, 1), y.values)
            preds = en.predict(X_pred.values.reshape(-1, 1))
            tt.loc[(tt['Place'] == myplace) & (tt['Days_Since_Ten_Cases'] >= 0), 'Fatalities_Log_Pred1'] = preds
            tt.loc[(tt['Place'] == myplace), 'Fatalities_Pred1'] = tt['Fatalities_Log_Pred1'].apply(np.expm1)

            # Cap at 0.0001 Population
            pop_myplace = tt.query('Place == @myplace')['Population_final'].values[0]
            tt.loc[(tt['Place'] == myplace) & (tt['Fatalities_Pred1'] > (0.0001 * pop_myplace)), 'Fatalities_Pred1'] = (0.0001 * pop_myplace)

        ax = tt.query('Place == @myplace').set_index('Date')[['Fatalities','Fatalities_Pred1']].plot(figsize=(15, 5), title=myplace, ax=axs[1])
        plt.show()
    except:
        print(f'============= FAILED FOR {myplace} =============')
