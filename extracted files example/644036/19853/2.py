# Correcting population for missing countries
# Googled their names and copied the numbers here
pop_dict = {'Angola': int(29.78 * 10**6),
            'Australia_Australian Capital Territory': 423_800,
            'Australia_New South Wales': int(7.544 * 10**6),
            'Australia_Northern Territory': 244_300,
            'Australia_Queensland' : int(5.071 * 10**6),
            'Australia_South Australia' : int(1.677 * 10**6),
            'Australia_Tasmania': 515_000,
            'Australia_Victoria': int(6.359 * 10**6),
            'Australia_Western Australia': int(2.589 * 10**6),
            'Brazil': int(209.3 * 10**6),
            'Canada_Alberta' : int(4.371 * 10**6),
            'Canada_British Columbia' : int(5.071 * 10**6),
            'Canada_Manitoba' : int(1.369 * 10**6),
            'Canada_New Brunswick' : 776_827,
            'Canada_Newfoundland and Labrador' : 521_542,
            'Canada_Nova Scotia' : 971_395,
            'Canada_Ontario' : int(14.57 * 10**6),
            'Canada_Prince Edward Island' : 156_947,
            'Canada_Quebec' : int(8.485 * 10**6),
            'Canada_Saskatchewan': int(1.174 * 10**6),
            'China_Anhui': int(62 * 10**6),
            'China_Beijing': int(21.54 * 10**6),
            'China_Chongqing': int(30.48 * 10**6),
            'China_Fujian' :  int(38.56 * 10**6),
            'China_Gansu' : int(25.58 * 10**6),
            'China_Guangdong' : int(113.46 * 10**6),
            'China_Guangxi' : int(48.38 * 10**6),
            'China_Guizhou' : int(34.75 * 10**6),
            'China_Hainan' : int(9.258 * 10**6),
            'China_Hebei' : int(74.7 * 10**6),
            'China_Heilongjiang' : int(38.31 * 10**6),
            'China_Henan' : int(94 * 10**6),
            'China_Hong Kong' : int(7.392 * 10**6),
            'China_Hubei' : int(58.5 * 10**6),
            'China_Hunan' : int(67.37 * 10**6),
            'China_Inner Mongolia' :  int(24.71 * 10**6),
            'China_Jiangsu' : int(80.4 * 10**6),
            'China_Jiangxi' : int(45.2 * 10**6),
            'China_Jilin' : int(27.3 * 10**6),
            'China_Liaoning' : int(43.9 * 10**6),
            'China_Macau' : 622_567,
            'China_Ningxia' : int(6.301 * 10**6),
            'China_Qinghai' : int(5.627 * 10**6),
            'China_Shaanxi' : int(37.33 * 10**6),
            'China_Shandong' : int(92.48 * 10**6),
            'China_Shanghai' : int(24.28 * 10**6),
            'China_Shanxi' : int(36.5 * 10**6),
            'China_Sichuan' : int(81.1 * 10**6),
            'China_Tianjin' : int(15 * 10**6),
            'China_Tibet' : int(3.18 * 10**6),
            'China_Xinjiang' : int(21.81 * 10**6),
            'China_Yunnan' : int(45.97 * 10**6),
            'China_Zhejiang' : int(57.37 * 10**6),
            'Denmark_Faroe Islands' : 51_783,
            'Denmark_Greenland' : 56_171,
            'France_French Guiana' : 290_691,
            'France_French Polynesia' : 283_007,
            'France_Guadeloupe' : 395_700,
            'France_Martinique' : 376_480,
            'France_Mayotte' : 270_372,
            'France_New Caledonia' : 99_926,
            'France_Reunion' : 859_959,
            'France_Saint Barthelemy' : 9_131,
            'France_St Martin' : 32_125,
            'Netherlands_Aruba' : 105_264,
            'Netherlands_Curacao' : 161_014,
            'Netherlands_Sint Maarten' : 41_109,
            'Papua New Guinea' : int(8.251 * 10**6),
            'US_Guam' : 164_229,
            'US_Virgin Islands' : 107_268,
            'United Kingdom_Bermuda' : 65_441,
            'United Kingdom_Cayman Islands' : 61_559,
            'United Kingdom_Channel Islands' : 170_499,
            'United Kingdom_Gibraltar' : 34_571,
            'United Kingdom_Isle of Man' : 84_287,
            'United Kingdom_Montserrat' : 4_922,
            'Botswana' : int(2.292 * 10**6),
            'Burma' : int(53.37 * 10**6),
            'Burundi': int(10.86 * 10**6),
            'Canada' : int(37.59 * 10**6),
            'MS Zaandam' : 1_829,
            'Sierra Leone': int(7.557 * 10**6),
            'United Kingdom' : int(66.65 * 10**6),
            'West Bank and Gaza' : int(4.685 * 10**6),
            'Canada_Northwest Territories': 44_826,
            'Canada_Yukon' : 35_874,
            'United Kingdom_Anguilla' : 15_094,
            'United Kingdom_British Virgin Islands' : 35_802,
            'United Kingdom_Turks and Caicos Islands' : 31_458
           }

tt['Population_final'] = tt['Population_final'].fillna(tt['Place'].map(pop_dict))

tt.loc[tt['Place'] == 'Diamond Princess', 'Population final'] = 2_670

tt['ConfirmedCases_Log'] = tt['ConfirmedCases'].apply(np.log1p)
tt['Fatalities_Log'] = tt['Fatalities'].apply(np.log1p)

tt['Population_final'] = tt['Population_final'].astype('int')
tt['Cases_Per_100kPop'] = (tt['ConfirmedCases'] / tt['Population_final']) * 100000
tt['Fatalities_Per_100kPop'] = (tt['Fatalities'] / tt['Population_final']) * 100000

tt['Cases_Percent_Pop'] = ((tt['ConfirmedCases'] / tt['Population_final']) * 100)
tt['Fatalities_Percent_Pop'] = ((tt['Fatalities'] / tt['Population_final']) * 100)

tt['Cases_Log_Percent_Pop'] = ((tt['ConfirmedCases'] / tt['Population_final']) * 100).apply(np.log1p)
tt['Fatalities_Log_Percent_Pop'] = ((tt['Fatalities'] / tt['Population_final']) * 100).apply(np.log1p)


tt['Max_Confirmed_Cases'] = tt.groupby('Place')['ConfirmedCases'].transform(max)
tt['Max_Fatalities'] = tt.groupby('Place')['Fatalities'].transform(max)

tt['Max_Cases_Per_100kPop'] = tt.groupby('Place')['Cases_Per_100kPop'].transform(max)
tt['Max_Fatalities_Per_100kPop'] = tt.groupby('Place')['Fatalities_Per_100kPop'].transform(max)
