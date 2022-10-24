detailed_class_info = pd.read_csv('../input/stage_1_detailed_class_info.csv')
detailed_class_info.groupby('class').count()
