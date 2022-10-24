# Read in data
train = pd.read_csv("../input/covid19-global-forecasting-week-3/train.csv")
test = pd.read_csv("../input/covid19-global-forecasting-week-3/test.csv")

tt = pd.concat([train, test], sort=False)
tt = train.merge(test, on=['Province_State','Country_Region','Date'], how='outer')

# concat Country/Region and Province/State
def name_place(x):
    try:
        x_new = x['Country_Region'] + "_" + x['Province_State']
    except:
        x_new = x['Country_Region']
    return x_new
tt['Place'] = tt.apply(lambda x: name_place(x), axis=1)
# tt = tt.drop(['Province_State','Country_Region'], axis=1)
tt['Date'] = pd.to_datetime(tt['Date'])
tt['doy'] = tt['Date'].dt.dayofyear
tt['dow'] = tt['Date'].dt.dayofweek
tt['hasProvidence'] = ~tt['Province_State'].isna()


country_meta = pd.read_csv('../input/covid19-forecasting-metadata/region_metadata.csv')
tt = tt.merge(country_meta, how='left')

country_date_meta = pd.read_csv('../input/covid19-forecasting-metadata/region_date_metadata.csv')
#tt = tt.merge(country_meta, how='left')

tt['HasFatality'] = tt.groupby('Place')['Fatalities'].transform(lambda x: x.max() > 0)
tt['HasCases'] = tt.groupby('Place')['ConfirmedCases'].transform(lambda x: x.max() > 0)

first_case_date = tt.query('ConfirmedCases >= 1').groupby('Place')['Date'].min().to_dict()
ten_case_date = tt.query('ConfirmedCases >= 10').groupby('Place')['Date'].min().to_dict()
hundred_case_date = tt.query('ConfirmedCases >= 100').groupby('Place')['Date'].min().to_dict()
first_fatal_date = tt.query('Fatalities >= 1').groupby('Place')['Date'].min().to_dict()
ten_fatal_date = tt.query('Fatalities >= 10').groupby('Place')['Date'].min().to_dict()
hundred_fatal_date = tt.query('Fatalities >= 100').groupby('Place')['Date'].min().to_dict()

tt['First_Case_Date'] = tt['Place'].map(first_case_date)
tt['Ten_Case_Date'] = tt['Place'].map(ten_case_date)
tt['Hundred_Case_Date'] = tt['Place'].map(hundred_case_date)
tt['First_Fatal_Date'] = tt['Place'].map(first_fatal_date)
tt['Ten_Fatal_Date'] = tt['Place'].map(ten_fatal_date)
tt['Hundred_Fatal_Date'] = tt['Place'].map(hundred_fatal_date)

tt['Days_Since_First_Case'] = (tt['Date'] - tt['First_Case_Date']).dt.days
tt['Days_Since_Ten_Cases'] = (tt['Date'] - tt['Ten_Case_Date']).dt.days
tt['Days_Since_Hundred_Cases'] = (tt['Date'] - tt['Hundred_Case_Date']).dt.days
tt['Days_Since_First_Fatal'] = (tt['Date'] - tt['First_Fatal_Date']).dt.days
tt['Days_Since_Ten_Fatal'] = (tt['Date'] - tt['Ten_Fatal_Date']).dt.days
tt['Days_Since_Hundred_Fatal'] = (tt['Date'] - tt['Hundred_Fatal_Date']).dt.days

# Merge smoking data
smoking = pd.read_csv("../input/smokingstats/share-of-adults-who-smoke.csv")
smoking = smoking.rename(columns={'Smoking prevalence, total (ages 15+) (% of adults)': 'Smoking_Rate'})
smoking_dict = smoking.groupby('Entity')['Year'].max().to_dict()
smoking['LastYear'] = smoking['Entity'].map(smoking_dict)
smoking = smoking.query('Year == LastYear').reset_index()
smoking['Entity'] = smoking['Entity'].str.replace('United States', 'US')

tt = tt.merge(smoking[['Entity','Smoking_Rate']],
         left_on='Country_Region',
         right_on='Entity',
         how='left',
         validate='m:1') \
    .drop('Entity', axis=1)

# Country data
country_info = pd.read_csv('../input/countryinfo/covid19countryinfo.csv')


tt = tt.merge(country_info, left_on=['Country_Region','Province_State'],
              right_on=['country','region'],
              how='left',
              validate='m:1')

# State info from wikipedia
us_state_info = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states_by_population')[0] \
    [['State','Population estimate, July 1, 2019[2]']] \
    .rename(columns={'Population estimate, July 1, 2019[2]' : 'Population'})
#us_state_info['2019 population'] = pd.to_numeric(us_state_info['2019 population'].str.replace('[note 1]','').replace('[]',''))

tt = tt.merge(us_state_info[['State','Population']],
         left_on='Province_State',
         right_on='State',
         how='left')

tt['pop'] = pd.to_numeric(tt['pop'].str.replace(',',''))
tt['pop'] = tt['pop'].fillna(tt['Population'])
tt['pop'] = pd.to_numeric(tt['pop'])

tt['pop_diff'] = tt['pop'] - tt['Population']
tt['Population_final'] = tt['Population']
tt.loc[~tt['hasProvidence'], 'Population_final'] = tt.loc[~tt['hasProvidence']]['pop']

tt['Confirmed_Cases_Diff'] = tt.groupby('Place')['ConfirmedCases'].diff()
tt['Fatailities_Diff'] = tt.groupby('Place')['Fatalities'].diff()
max_date = tt.dropna(subset=['ConfirmedCases'])['Date'].max()
tt['gdp2019'] = pd.to_numeric(tt['gdp2019'].str.replace(',',''))
