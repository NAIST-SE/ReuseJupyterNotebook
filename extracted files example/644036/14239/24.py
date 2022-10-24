average_of_feat['pos_neg_diff'] = np.abs(average_of_feat[0] - average_of_feat[1])
average_of_feat.sort_values('pos_neg_diff', ascending=True) \
    .tail(20).set_index('feature')['pos_neg_diff'].plot(kind='barh',
                                                        title='Top 20 feature with biggest difference in mean between positive and negative class',
                                                       figsize=(15, 7),
                                                       color='grey')
plt.show()
