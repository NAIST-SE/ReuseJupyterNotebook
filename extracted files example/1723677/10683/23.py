data = pd.read_csv('../input/google-safe-browsing-transparency-report-data/data.csv')
data['WeekOf'] = data['WeekOf'].map(lambda x: datetime.strptime(x,'%Y-%m-%d').date())
datedictAS = np.load('../input/malware-timestamps/AvSigVersionTimestamps.npy')[()]
weekdictAS={}
for x in datedictAS: 
    weekdictAS[x] = (datedictAS[x] - timedelta(days= -7+1+datedictAS[x].weekday())).date()
df_train['WeekOf'] = df_train['AvSigVersion'].map(weekdictAS)
df_train = pd.merge(df_train, data, on='WeekOf', how='left')
print('GOOGLE DATA')
data.sample(5)
