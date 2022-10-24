# LOAD TRAIN META DATA
df = pd.read_csv('../input/melanoma-merged-external-data-512x512-jpeg/marking.csv')
df.rename({'image_id':'image_name'},axis=1,inplace=True)
df.head()
