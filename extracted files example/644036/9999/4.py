def plot_year_over_year_dow(item, store):
    sample = train.loc[(train['store'] == store) & (train['item'] == item)].set_index('date')
    pv = pd.pivot_table(sample, index=sample.index.weekday, columns=sample.index.year,
                        values='sales', aggfunc='sum')
    ax = pv.plot(figsize=(15,3), title=fake_store_names[store] + ' - ' + fake_items[item])
    ax.set_xlabel("Day of Week")
plot_year_over_year_dow(1, 1)
plot_year_over_year_dow(1, 2)
plot_year_over_year_dow(20, 5)
plot_year_over_year_dow(20, 6)
