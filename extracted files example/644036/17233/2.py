plt.style.use('bmh')
plt.rcParams["font.size"] = "25"
team_over_time = df.ffill() \
    .count(axis=1)

lr = LinearRegression()
_ = lr.fit(np.array(pd.to_numeric(team_over_time.index).tolist()).reshape(-1, 1),
           team_over_time.values)

teamcount_df = pd.DataFrame(team_over_time)

teamcount_pred_df = pd.DataFrame(index=pd.date_range('11-20-2019','01-20-2020'))

lr = LinearRegression()
_ = lr.fit(np.array(pd.to_numeric(team_over_time[-100:].index).tolist()).reshape(-1, 1),
           team_over_time[-100:].values)

teamcount_pred_df['Forecast Using Recent Data'] = lr.predict(np.array(pd.to_numeric(teamcount_pred_df.index).tolist()).reshape(-1, 1))

plt.rcParams["font.size"] = "12"
ax =df.ffill() \
    .count(axis=1) \
    .plot(figsize=(20, 8),
          title='Forecasting the Final Number of Teams',
         color=color_pal[5], lw=5,
         xlim=('11-01-2019','01-20-2020'))
teamcount_pred_df['Forecast Using Recent Data'].plot(ax=ax, style='.-.', alpha=0.5, label='Regression Using last 1000 observations')
ax.set_ylabel('Number of Teams')
teamcount_pred_df.plot(ax=ax, style='.-.', alpha=0.5)
plt.axvline('1-8-2020', color='orange', linestyle='-.')
plt.text('1-8-2020', 900,'Merger Deadline',rotation=-90)
plt.axvline('1-15-2020', color='orange', linestyle='-.')
plt.text('1-15-2020', 500,'Deadline',rotation=-90)
plt.show()
