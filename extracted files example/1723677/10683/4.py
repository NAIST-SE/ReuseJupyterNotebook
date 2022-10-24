cols3 = []
# ENGINEERED FEATURES #6, #7, #8, #9, #10
FE = ['Census_OSVersion', 'Census_OSBuildRevision', 'Census_InternalBatteryNumberOfCharges', 'AvSigVersion', 'Lag1']
for col in FE:
    cols3 += encode_FE(df_train, col)
    encode_FE(df_test, col)
    
# ENGINEERED FEATURES #11, #12
FE2 = ['CountryIdentifier', 'Census_InternalBatteryNumberOfCharges']
for col in FE2:
    cols3 += encode_FE2(df_train, df_test, col)
