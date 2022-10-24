import scipy.optimize as opt

def sigmoid(t, M, beta, alpha):
    return M / (1 + np.exp(-beta * (t - alpha)))


for myplace in tt['Place'].unique():


    pop = tt.loc[tt['Place'] == myplace]['Population_final'].values[0]

    BOUNDS=(0, [pop, 2.0, 100])

    xin = tt.query('Place == @myplace').dropna(subset=['ConfirmedCases'])['doy'].values
    yin = tt.query('Place == @myplace').dropna(subset=['ConfirmedCases'])['ConfirmedCases'].values
    popt, pcov = opt.curve_fit(sigmoid,
                               xin,
                               yin,
                               bounds=BOUNDS)

    M, beta, alpha = popt
    print(M, beta, alpha)
    x = tt.loc[tt['Place'] == myplace]['doy'].values
    tt.loc[tt['Place'] == myplace, 'ConfirmedCases_forecast'] = sigmoid(x, M, beta, alpha)

    xin = tt.query('Place == @myplace').dropna(subset=['Fatalities'])['doy'].values
    yin = tt.query('Place == @myplace').dropna(subset=['Fatalities'])['Fatalities'].values
    popt, pcov = opt.curve_fit(sigmoid,
                               xin,
                               yin,
                               bounds=BOUNDS)

    M, beta, alpha = popt
    print(M, beta, alpha)
    x = tt.loc[tt['Place'] == myplace]['doy'].values
    tt.loc[tt['Place'] == myplace, 'Fatalities_forecast'] = sigmoid(x, M, beta, alpha)

    fig, axs = plt.subplots(1, 2, figsize=(15, 3))
    ax = tt.query('Place == @myplace').set_index('Date')[['ConfirmedCases','ConfirmedCases_forecast']].plot(title=myplace, ax=axs[0])
    ax = tt.query('Place == @myplace').set_index('Date')[['Fatalities','Fatalities_forecast']].plot(title=myplace, ax=axs[1])
    plt.show()
