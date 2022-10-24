test.set_index('Date')[['Place','ConfirmedCases_pred','ConfirmedCases']].query('Place == "US_Maryland"').plot(figsize=(15, 5))
plt.show()

test.set_index('Date')[['Place','ConfirmedCases_pred','ConfirmedCases']].query('Place == "Bhutan"').plot(figsize=(15, 5))
plt.show()
