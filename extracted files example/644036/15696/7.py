plt.rcParams["font.size"] = "7"
n_weeks = (datetime.date.today() - datetime.date(2019, 10, 10)).days #/ 7 # Num days of the comp
n_weeks = int(n_weeks)
fig, axes = plt.subplots(n_weeks, 1, figsize=(15, 25), sharex=True)
#plt.subplots_adjust(top=8, bottom=2)
for x in range(n_weeks):
    date2 = df.loc[df.index.date == datetime.date(2019, 10, 10) + datetime.timedelta(x+1)].index.min()
    num_teams = len(df.ffill().loc[date2].dropna())
    max_cutoff = df.ffill().loc[date2] < 0.019
    df.ffill().loc[date2].loc[max_cutoff].plot(kind='hist',
                               bins=50,
                               ax=axes[x],
                               title='{} ({} Teams)'.format(date2.date().isoformat(),
                                                            num_teams),
                                              xlim=(0.012, 0.019))
    y_axis = axes[x].yaxis
    y_axis.set_label_text('')
    y_axis.label.set_visible(False)
