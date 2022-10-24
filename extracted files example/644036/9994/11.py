# Aggregate some meter reading stats
meter_reading_stats = train.groupby('building_id')['meter_reading'].agg(['mean','max','min']).reset_index()
bmd_with_stats = pd.merge(bmd, meter_reading_stats, on=['building_id']).rename(columns={'mean':'mean_meter_reading',
                                                                       'max':'max_meter_reading',
                                                                       'min':'min_meter_reading'})
