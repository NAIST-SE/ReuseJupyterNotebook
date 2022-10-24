for myplace in constant_fatal_places:
    fig, axs = plt.subplots(1, 2, figsize=(15, 3))
    ax = tt.query('Place == @myplace').set_index('Date')[['ConfirmedCases','ConfirmedCases_Pred1']].plot(figsize=(15, 5), title=myplace, ax=axs[0])
    ax = tt.query('Place == @myplace').set_index('Date')[['Fatalities','Fatalities_Pred1']].plot(figsize=(15, 5), title=myplace, ax=axs[1])
    plt.show()
