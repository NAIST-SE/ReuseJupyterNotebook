anchors = [-2.5002, -1.2502, -0.0002, 1.2498, 2.4998, 3.7498]
tt.query('drift == False and signal in @anchors').groupby(['signal','open_channels'])[['time']].count()
