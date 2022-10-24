def plot_year_over_year(item, store):
    sample = train.loc[(train['store'] == store) & (train['item'] == item)].set_index('date')
    pv = pd.pivot_table(sample, index=sample.index.month, columns=sample.index.year,
                        values='sales', aggfunc='sum')
    ax = pv.plot(figsize=(15,3), title=fake_store_names[store] + ' - ' + fake_items[item])
    ax.set_xlabel("Month")
plot_year_over_year(1, 1)
plot_year_over_year(1, 2)
plot_year_over_year(20, 5)
plot_year_over_year(20, 6)
