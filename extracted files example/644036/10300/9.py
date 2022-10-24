# Average values by genre

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(30, 15))

color1 = list(plt.rcParams['axes.prop_cycle'])[1]['color']
genre_popularity = {}
for genre in genre_list:
    genre_popularity[genre] = train.loc[train[genre] == 1]['popularity'].mean()
pd.DataFrame(genre_popularity, index=['Average Popularity']) \
    .T.sort_values('Average Popularity') \
    .plot(kind='barh', color=color1, title='Average Popularity by Genre', ax=ax1, legend=False)

# Find the popularity of each genre
color2 = list(plt.rcParams['axes.prop_cycle'])[2]['color']
genre_budget = {}
for genre in genre_list:
    genre_budget[genre] = train.loc[train[genre] == 1]['budget'].mean()
pd.DataFrame(genre_budget, index=['Average Budget']) \
    .T.sort_values('Average Budget') \
    .plot(kind='barh', color=color2, title='Average Budget by Genre', ax=ax2, legend=False)

color4 = list(plt.rcParams['axes.prop_cycle'])[4]['color']
genre_revenue = {}
for genre in genre_list:
    genre_revenue[genre] = train.loc[train[genre] == 1]['revenue'].mean()
pd.DataFrame(genre_revenue, index=['Average Revenue']) \
    .T.sort_values('Average Revenue') \
    .plot(kind='barh', color=color4, title='Average Revenue by Genre', ax=ax3, legend=False)
plt.show()
