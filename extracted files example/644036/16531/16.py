train.groupby('installation_id') \
    .count()['event_id'].sort_values(ascending=False).head(5)
