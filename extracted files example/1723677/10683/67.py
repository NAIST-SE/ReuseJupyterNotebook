from keras.models import Model
from keras.layers import Dense, Input, concatenate, BatchNormalization, Activation, Dropout, Embedding, Reshape
from keras.callbacks import LearningRateScheduler
from keras.optimizers import Adam

df_train_Y = df_train['HasDetections']
del df_train['HasDetections']
x=gc.collect()

#SPLIT TRAIN AND VALIDATION SET
chunk = len(df_train)//5
idx = range(chunk*0,chunk//2)
idx2 = range(chunk//2,chunk)
idx3 = range(chunk,chunk*3)
idx4 = range(chunk*3,chunk*5)
X_val1 = df_train.loc[idx]
Y_val1 = df_train_Y.loc[idx]
X_val2 = df_train.loc[idx2]
Y_val2 = df_train_Y.loc[idx2]
X_train1 = df_train.loc[idx3]
Y_train1 = df_train_Y.loc[idx3]
X_train2 = df_train.loc[idx4]
Y_train2 = df_train_Y.loc[idx4]
del df_train, df_train_Y
x=gc.collect()
