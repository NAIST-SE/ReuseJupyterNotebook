fig, ax1 = plt.subplots(figsize=(15, 5))

tt.query('Days_Since_Ten_Cases > 0') \
    .query('Place != "Diamond Princess"') \
    .dropna(subset=['Cases_Percent_Pop']) \
    .query('Days_Since_Ten_Cases < 40') \
    .groupby('Place') \
    .plot(x='Days_Since_Ten_Cases',
          y='Cases_Log_Percent_Pop',
          style='.-',
          figsize=(15, 5),
          alpha=0.2,
          ax=ax1,
         title='Days since 10 Cases by Percent of Population with Cases')
ax1.get_legend().remove()
plt.show()

fig, ax2 = plt.subplots(figsize=(15, 5))
tt.query('Days_Since_Ten_Fatal > 0') \
    .query('Place != "Diamond Princess"') \
    .dropna(subset=['Cases_Percent_Pop']) \
    .query('Days_Since_Ten_Fatal < 100') \
    .groupby('Place') \
    .plot(x='Days_Since_Ten_Fatal',
          y='Cases_Log_Percent_Pop',
          style='.-',
          figsize=(15, 5),
          alpha=0.2,
         title='Days since 10 Fatailites by Percent of Population with Cases',
         ax=ax2)
ax2.get_legend().remove()
plt.show()
