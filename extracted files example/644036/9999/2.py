grouped = train.groupby(by=['item_name'])
for i, d in grouped:
    myplot = d.set_index('date').groupby('store_name')['sales'] \
        .plot(figsize=(15,2), style='.', title=str(i), legend=False)
    plt.show()
