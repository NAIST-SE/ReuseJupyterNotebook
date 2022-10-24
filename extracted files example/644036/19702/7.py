tt.query('Date == @max_date') \
    .query('Place != "Diamond Princess"') \
    .query('Cases_Log_Percent_Pop > -10000') \
    ['Cases_Log_Percent_Pop'].plot(kind='hist', bins=500)
plt.show()
