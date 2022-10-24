latest_summary_stats = tt.query('Date == @max_date') \
    [['Country_Region',
      'Place',
      'Max_Cases_Per_100kPop',
      'Max_Fatalities_Per_100kPop',
      'Max_Confirmed_Cases',
      'Population_final',
      'Days_Since_First_Case',
      'Days_Since_Ten_Cases']] \
    .drop_duplicates()
