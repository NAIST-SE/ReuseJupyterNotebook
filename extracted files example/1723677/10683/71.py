# LOAD BEST SAVED NET
from keras.models import load_model

# PREDICT TEST
pred = np.zeros((len(df_test),1))
print('Predicting test...')
model = load_model('bestNet0.h5')
idx = 0; chunk = 1000000
if Debug: chunk = 5000
ct2 = 1;
while idx < len(df_test):
    idx2 = min(idx + chunk, len(df_test) )
    idx = range(idx, idx2)
    pred[idx] += model.predict( [df_test.iloc[idx][col] for col in OHE] + [df_test.iloc[idx][NUM]] )
    print(' part '+str(ct2)+' done')
    ct2 += 1
    idx = idx2
del model
x = gc.collect()
