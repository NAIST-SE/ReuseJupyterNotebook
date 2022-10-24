import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)
plt.rcParams["font.size"] = "10"
n_weeks = (datetime.date(2020, 5, 10) - datetime.date(2020, 2, 27)).days / 7 # Num days of the comp
n_weeks = int(n_weeks)
#n_weeks = 5
fig, axes = plt.subplots(n_weeks, 1, figsize=(15, 20), sharex=True)
#plt.subplots_adjust(top=8, bottom=2)
for x in range(n_weeks):
    date2 = df.loc[df.index.date == datetime.date(2020, 2, 28) + datetime.timedelta(x*7+1)].index.min()
    num_teams = len(df.ffill().loc[date2].dropna())
    max_cutoff = df.ffill().loc[date2] < 5
#     df.ffill().loc[date2].loc[max_cutoff].plot(kind='hist',
#                                bins=500,
#                                ax=axes[x],
#                                title='{} ({} Teams)'.format(date2.date().isoformat(),
#                                                             num_teams),
#                                               xlim=(0.93, 0.95))
    df.ffill().loc[date2].loc[max_cutoff] \
        .where(df.ffill().loc[date2].loc[max_cutoff] > 0.9) \
        .dropna().plot(kind='hist', bins=100, ax=axes[x],
                       title='{} ({} Teams)'.format(date2.date().isoformat(), num_teams))
#     pd.Series(df.ffill().loc[date2].loc[max_cutoff] \
#               .round(4) \
#               .value_counts()) \
#     .sort_index() \
#     .plot(ax=axes[x],
#           kind='bar',
#           title='{} ({} Teams)'.format(date2.date().isoformat(), num_teams))
    y_axis = axes[x].yaxis
    y_axis.set_label_text('')
    y_axis.label.set_visible(False)
    axes[x].grid(False)
