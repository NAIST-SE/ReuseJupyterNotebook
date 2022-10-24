plt.rcParams["font.size"] = "7"
n_days = (datetime.date.today() - datetime.date(2019, 5, 29)).days # Num days of the comp
fig, axes = plt.subplots(n_days, 1, figsize=(15, 10), sharex=True)
plt.subplots_adjust(top=8, bottom=2)
for x in range(n_days):
    date2 = df.loc[df.index.date == datetime.date(2019, 5, 29) + datetime.timedelta(x)].index.min()
    num_teams = len(df.ffill().loc[date2].dropna())
    max_cutoff = df.ffill().loc[date2] < 5
    df.ffill().loc[date2].loc[max_cutoff].plot(kind='hist',
                               bins=100,
                               ax=axes[x],
                               title='{} ({} Teams)'.format(date2.date().isoformat(),
                                                            num_teams))
    y_axis = axes[x].yaxis
    y_axis.set_label_text('')
    y_axis.label.set_visible(False)
