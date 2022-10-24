tt.query('Date == @max_date')[['Place','Max_Cases_Per_100kPop',
                               'Max_Fatalities_Per_100kPop','Max_Confirmed_Cases',
                               'Population_final',
                              'Days_Since_First_Case',
                              'Confirmed_Cases_Diff']] \
    .drop_duplicates() \
    .sort_values('Max_Cases_Per_100kPop', ascending=False)
