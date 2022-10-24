# Example of flat prop
tt.query("Place == 'China_Chongqing'").set_index('Date')['ConfirmedCases'].dropna().plot(figsize=(15, 5))
plt.show()
