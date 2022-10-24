PLOT = False
if PLOT:
    for x in tt['Place'].unique():
        try:
            fig, ax = plt.subplots(1, 4, figsize=(15, 2))
            tt.query('Place == @x') \
                .query('ConfirmedCases > 0') \
                .set_index('Date')['Cases_Log_Percent_Pop'] \
                .plot(title=f'{x} confirmed log pct pop', ax=ax[0])
            tt.query('Place == @x') \
                .query('ConfirmedCases > 0') \
                .set_index('Date')['Cases_Percent_Pop'] \
                .plot(title=f'{x} confirmed cases', ax=ax[1])
            tt.query('Place == @x') \
                .query('Fatalities > 0') \
                .set_index('Date')['Fatalities_Log_Percent_Pop'] \
                .plot(title=f'{x} confirmed log pct pop', ax=ax[2])
            tt.query('Place == @x') \
                .query('Fatalities > 0') \
                .set_index('Date')['Fatalities_Percent_Pop'] \
                .plot(title=f'{x} confirmed cases', ax=ax[3])
        except:
            pass
        plt.show()
