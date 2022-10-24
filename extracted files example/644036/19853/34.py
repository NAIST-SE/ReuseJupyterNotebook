for myplace in tt['Place'].unique():
    try:
        # Confirmed Cases
        fig, axs = plt.subplots(1, 2, figsize=(15, 3))
        ax = tt.query('Place == @myplace').set_index('Date')[['ConfirmedCases','ConfirmedCases_Pred']].plot(title=myplace, ax=axs[0])
        ax = tt.query('Place == @myplace').set_index('Date')[['Fatalities','Fatalities_Pred']].plot(title=myplace, ax=axs[1])
        plt.show()
    except:
        print(f'============= FAILED FOR {myplace} =============')
