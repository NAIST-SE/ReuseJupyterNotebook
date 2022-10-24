latest_summary_stats.query('Place != "Diamond Princess"') \
    .query('Country_Region != "China"') \
    .plot(y='Max_Cases_Per_100kPop',
          x='Days_Since_Ten_Cases',
          style='.',
          figsize=(15, 5))
