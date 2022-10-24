tt.query('Province_State == "Maryland"').set_index('Date') \
    [['ConfirmedCases','Confirmed_Cases_Diff']].plot(figsize=(15,5 ))
