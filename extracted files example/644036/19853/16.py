tt.query("Place == 'Italy'").set_index('Date')[['ConfirmedCases']] \
    .dropna().plot(figsize=(15, 5), title='Italy Confirmed Cases')
plt.show()
tt.query("Place == 'Italy'").set_index('Date')[['ConfirmedCases_Log']] \
    .dropna().plot(figsize=(15, 5), title='Italy Fatalities')
plt.show()
