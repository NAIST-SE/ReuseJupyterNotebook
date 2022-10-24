plt.rcParams["font.size"] = "7"
n_weeks = (datetime.date(2019, 10, 3) - datetime.date(2019, 7, 14)).days / 7 # Num days of the comp
n_weeks = int(n_weeks)
fig, axes = plt.subplots(n_weeks, 1, figsize=(15, 25), sharex=True)
#plt.subplots_adjust(top=8, bottom=2)
for x in range(n_weeks):
    date2 = df.loc[df.index.date == datetime.date(2019, 7, 15) + datetime.timedelta(x*7+1)].index.min()
    num_teams = len(df.ffill().loc[date2].dropna())
    max_cutoff = df.ffill().loc[date2] < 5
    df.ffill().loc[date2].loc[max_cutoff].plot(kind='hist',
                               bins=500,
                               ax=axes[x],
                               title='{} ({} Teams)'.format(date2.date().isoformat(),
                                                            num_teams),
                                              xlim=(0.9, 0.96))
    y_axis = axes[x].yaxis
    y_axis.set_label_text('')
    y_axis.label.set_visible(False)
