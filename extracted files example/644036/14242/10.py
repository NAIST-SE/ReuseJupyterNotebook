# Missing "Young for you"
gold_teams = ['FraudSquad','2 uncles and 3 puppies','T.U.V', 'Lions','The Zoo',
              'Grand Rookie(Done!Good luck to everyone!)）', 'S.A.R.M.A', 'AlKo', 'M5',
              'Flying Whales','邦盛科技小分队','YuyaYamamoto','MaYa','Mr Lonely ♬','spongebob',
              'Taemyung Heo','conundrum.ai & Evgeny', 'クソザコちゃうねん','Our AUC says nothing to us',
              'bird and fish', '天行健,君子以自强不息 地势坤,君子以厚德载物']

gold_df = df[gold_teams]
gold_scores = [0.945884, 0.944210, 0.942580, 0.942453, 0.942391, 0.942314, 0.942268, 0.942129, 0.941750,
              0.941638, 0.941413, 0.941338, 0.941153, 0.941096, 0.941011, 0.940934, 0.940756, 0.940730,
              0.940526, 0.940250, 0.940076]

gold_scores_df = pd.DataFrame(index=gold_teams,
                             data=gold_scores,
                             columns=['Private Score'])
