df_test2['ones'] = 1
dynamicPlot(df_test2,'ones',title='Original submission')
dynamicPlot(df_test2,'AvSigVersion2',start=datetime(2018,9,1),end=datetime(2018,11,29),inc_dy=1,top2=4, dots=True)
