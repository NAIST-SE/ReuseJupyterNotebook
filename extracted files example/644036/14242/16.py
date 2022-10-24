# plt.style.use('ggplot')
# team_over_time = df.ffill() \
#     .count(axis=1)

# lr = LinearRegression()
# _ = lr.fit(np.array(pd.to_numeric(team_over_time.index).tolist()).reshape(-1, 1),
#            team_over_time.values)

# teamcount_df = pd.DataFrame(team_over_time)

# teamcount_pred_df = pd.DataFrame(index=pd.date_range('07-15-2019','10-05-2019'))
# teamcount_pred_df['Forecast Using All Data'] = lr.predict(np.array(pd.to_numeric(teamcount_pred_df.index).tolist()).reshape(-1, 1))

# lr = LinearRegression()
# _ = lr.fit(np.array(pd.to_numeric(team_over_time[-5000:].index).tolist()).reshape(-1, 1),
#            team_over_time[-5000:].values)

# teamcount_pred_df['Forecast Using Recent Data'] = lr.predict(np.array(pd.to_numeric(teamcount_pred_df.index).tolist()).reshape(-1, 1))

# plt.rcParams["font.size"] = "12"
# ax =df.ffill() \
#     .count(axis=1) \
#     .plot(figsize=(20, 8),
#           title='Forecasting the Final Number of Teams',
#          color=color_pal[5], lw=5,
#          xlim=('07-13-2019','10-02-2019'))
# teamcount_pred_df['Forecast Using All Data'].plot(ax=ax, style='.-.', alpha=0.5, label='Regression Using All Data')
# teamcount_pred_df['Forecast Using Recent Data'].plot(ax=ax, style='.-.', alpha=0.5, label='Regression Using last 1000 observations')
# ax.set_ylabel('Number of Teams')
# teamcount_pred_df.plot(ax=ax, style='.-.', alpha=0.5)
# plt.axvline('09-23-2019', color='orange', linestyle='-.')
# plt.text('09-23-2019', 4000,'Merger Deadline',rotation=-90)
# plt.axvline('10-1-2019', color='orange', linestyle='-.')
# plt.text('10-1-2019', 4000,'Original Deadline',rotation=-90)
# plt.axvline('10-3-2019', color='orange', linestyle='-.')
# plt.text('10-3-2019', 4000,'Extended Deadline',rotation=-90)
# plt.show()
