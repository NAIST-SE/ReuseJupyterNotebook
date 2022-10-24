tt['Date_7Days_Since_First_Case'] = tt['Place'].map(tt.loc[tt['Days_Since_First_Case'] == 7] \
    .set_index('Place')['Date'] \
    .to_dict())
tt['Date_14Days_Since_First_Case'] = tt['Place'].map(tt.loc[tt['Days_Since_First_Case'] == 14] \
    .set_index('Place')['Date'] \
    .to_dict())
tt['Date_21Days_Since_First_Case'] = tt['Place'].map(tt.loc[tt['Days_Since_First_Case'] == 21] \
    .set_index('Place')['Date'] \
    .to_dict())
tt['Date_28Days_Since_First_Case'] = tt['Place'].map(tt.loc[tt['Days_Since_First_Case'] == 28] \
    .set_index('Place')['Date'] \
    .to_dict())
tt['Date_35Days_Since_First_Case'] = tt['Place'].map(tt.loc[tt['Days_Since_First_Case'] == 35] \
    .set_index('Place')['Date'] \
    .to_dict())
tt['Date_60Days_Since_First_Case'] = tt['Place'].map(tt.loc[tt['Days_Since_First_Case'] == 60] \
    .set_index('Place')['Date'] \
    .to_dict())

tt['Date_7Days_Since_Ten_Cases'] = tt['Place'].map(tt.loc[tt['Days_Since_Ten_Cases'] == 7] \
    .set_index('Place')['Date'] \
    .to_dict())
tt['Date_14Days_Since_Ten_Cases'] = tt['Place'].map(tt.loc[tt['Days_Since_Ten_Cases'] == 14] \
    .set_index('Place')['Date'] \
    .to_dict())
tt['Date_21Days_Since_Ten_Cases'] = tt['Place'].map(tt.loc[tt['Days_Since_Ten_Cases'] == 21] \
    .set_index('Place')['Date'] \
    .to_dict())
tt['Date_28Days_Since_Ten_Cases'] = tt['Place'].map(tt.loc[tt['Days_Since_Ten_Cases'] == 28] \
    .set_index('Place')['Date'] \
    .to_dict())
tt['Date_35Days_Since_Ten_Cases'] = tt['Place'].map(tt.loc[tt['Days_Since_Ten_Cases'] == 35] \
    .set_index('Place')['Date'] \
    .to_dict())
tt['Date_60Days_Since_Ten_Cases'] = tt['Place'].map(tt.loc[tt['Days_Since_Ten_Cases'] == 60] \
    .set_index('Place')['Date'] \
    .to_dict())


tt['Date_7Days_Since_First_Fatal'] = tt['Place'].map(tt.loc[tt['Days_Since_First_Fatal'] == 7] \
    .set_index('Place')['Date'] \
    .to_dict())
tt['Date_14Days_Since_First_Fatal'] = tt['Place'].map(tt.loc[tt['Days_Since_First_Fatal'] == 14] \
    .set_index('Place')['Date'] \
    .to_dict())
tt['Date_21Days_Since_First_Fatal'] = tt['Place'].map(tt.loc[tt['Days_Since_First_Fatal'] == 21] \
    .set_index('Place')['Date'] \
    .to_dict())
tt['Date_28Days_Since_First_Fatal'] = tt['Place'].map(tt.loc[tt['Days_Since_First_Fatal'] == 28] \
    .set_index('Place')['Date'] \
    .to_dict())
tt['Date_35Days_Since_First_Fatal'] = tt['Place'].map(tt.loc[tt['Days_Since_First_Fatal'] == 35] \
    .set_index('Place')['Date'] \
    .to_dict())
tt['Date_60Days_Since_First_Fatal'] = tt['Place'].map(tt.loc[tt['Days_Since_First_Fatal'] == 60] \
    .set_index('Place')['Date'] \
    .to_dict())
