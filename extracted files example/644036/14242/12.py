gold_scores_df.sort_values('Private Score', ascending=True). \
    plot(kind='barh',
         xlim=(0.94, 0.946),
         figsize=(15, 10),
         title='Final Private Board Scores of Gold Teams',
         color='lightgoldenrodyellow')
plt.show()
