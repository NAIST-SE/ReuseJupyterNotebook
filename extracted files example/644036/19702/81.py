myplace = 'US_Virgin Islands'
dat = tt.query('Place == @myplace and Days_Since_Ten_Cases >= 0')[['Place','Days_Since_Ten_Cases','ConfirmedCases']].dropna()
