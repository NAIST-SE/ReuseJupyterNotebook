tt.query('Days_Since_Ten_Cases > 0') \
    .query('Place != "Diamond Princess"') \
    .dropna(subset=['Cases_Percent_Pop']) \
    .query('Days_Since_Ten_Cases < 40') \
    .plot(x='Days_Since_Ten_Cases', y='Cases_Log_Percent_Pop', style='.', figsize=(15, 5), alpha=0.2)
plt.show()
