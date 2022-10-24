team_over_time = df.ffill() \
    .count(axis=1)

lr = LinearRegression()
_ = lr.fit(np.array(pd.to_numeric(team_over_time.index).tolist()).reshape(-1, 1),
           team_over_time.values)

teamcount_df = pd.DataFrame(team_over_time)

teamcount_pred_df = pd.DataFrame(index=pd.date_range('06-03-2019','08-29-2019'))
teamcount_pred_df['teamcount_predict'] = lr.predict(np.array(pd.to_numeric(teamcount_pred_df.index).tolist()).reshape(-1, 1))

lr = LinearRegression()
_ = lr.fit(np.array(pd.to_numeric(team_over_time[-1000:].index).tolist()).reshape(-1, 1),
           team_over_time[-1000:].values)

teamcount_pred_df['teamcount_predict_recent'] = lr.predict(np.array(pd.to_numeric(teamcount_pred_df.index).tolist()).reshape(-1, 1))

plt.rcParams["font.size"] = "12"
ax =df.ffill() \
    .count(axis=1) \
    .plot(figsize=(20, 8),
          title='Forecasting the Final Number of Teams',
         color=color_pal[5], lw=5,
         xlim=('05-29-2019','08-29-2019'),
         label='Acutal Team Count by Date')
ax.set_ylabel('Number of Teams')
teamcount_pred_df['teamcount_predict'].plot(ax=ax, style='.-.', alpha=0.5, label='Regression Using All Data')
teamcount_pred_df['teamcount_predict_recent'].plot(ax=ax, style='.-.', alpha=0.5, label='Regression Using last 1000 observations')
plt.legend()
plt.axvline('08-21-2019', color='orange', linestyle='-.')
plt.text('08-21-2019', 1000,'Merger Deadline',rotation=-90)
plt.axvline('08-28-2019', color='orange', linestyle='-.')
plt.text('08-28-2019', 1000,'Final Deadline',rotation=-90)
plt.show()
