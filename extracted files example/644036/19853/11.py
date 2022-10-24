fig, axs = plt.subplots(1, 2, figsize=(15, 5))
tt[['Place','Past_7Days_Confirmed_Change_of_Total','Past_7Days_Fatalities_Change_of_Total',
    'Past_7Days_ConfirmedCases_Max','Past_7Days_ConfirmedCases_Min',
   'Past_7Days_Fatalities_Max','Past_7Days_Fatalities_Min']] \
    .drop_duplicates() \
    .sort_values('Past_7Days_Confirmed_Change_of_Total')['Past_7Days_Confirmed_Change_of_Total'] \
    .plot(kind='hist', bins=50, title='Distribution of Pct change confirmed past 7 days', ax=axs[0])
tt[['Place','Past_21Days_Confirmed_Change_of_Total','Past_21Days_Fatalities_Change_of_Total',
    'Past_21Days_ConfirmedCases_Max','Past_21Days_ConfirmedCases_Min',
   'Past_21Days_Fatalities_Max','Past_21Days_Fatalities_Min']] \
    .drop_duplicates() \
    .sort_values('Past_21Days_Confirmed_Change_of_Total')['Past_21Days_Confirmed_Change_of_Total'] \
    .plot(kind='hist', bins=50, title='Distribution of Pct change confirmed past 21 days', ax=axs[1])
plt.show()

fig, axs = plt.subplots(1, 2, figsize=(15, 5))
tt[['Place','Past_7Days_Fatalities_Change_of_Total']] \
    .drop_duplicates()['Past_7Days_Fatalities_Change_of_Total'] \
    .plot(kind='hist', bins=50, title='Distribution of Pct change confirmed past 7 days', ax=axs[0])
tt[['Place', 'Past_21Days_Fatalities_Change_of_Total']] \
    .drop_duplicates()['Past_21Days_Fatalities_Change_of_Total'] \
    .plot(kind='hist', bins=50, title='Distribution of Pct change confirmed past 21 days', ax=axs[1])
plt.show()
