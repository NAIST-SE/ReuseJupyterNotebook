ins = []; outs = {}
# CREATE AN EMBEDDING FOR EACH CATEGORY VARIABLE
for k in inps.keys():
    x = Input(shape=(1,))
    ins.append(x)
    y = np.int(inps[k])
    x = Embedding(y, y, input_length=1)(x)
    x = Reshape(target_shape=(y, ))(x)
    outs[k]=x 
    
# ORGANIZE EMBEDDINGS INTO GROUPS
all = set(inps.keys())
used = []
outs2 = []
for k in groups:
    g = [outs[x] for x in set(k).intersection(all)]
    used += list(set(k).intersection(all))
    x = concatenate(g)
    s = sum([inps[x] for x in set(k).intersection(all)])
    x = Dense(s//2,kernel_initializer='he_uniform')(x)
    x = BatchNormalization()(x)
    x = Activation('elu')(x)
    outs2.append(x)
g = [outs[x] for x in all-set(used)]
x = concatenate(g)
s = sum([inps[x] for x in all-set(used)])
x = Dense(s//2,kernel_initializer='he_uniform')(x)
x = BatchNormalization()(x)
x = Activation('elu')(x)
outs2.append(x)

# ORGANIZE FREQUENCY ENCODED AND NUMERICS INTO A GROUP
x = Input(shape=(len(NUM), ))
ins.append(x)
x = Dense(len(NUM)//2,kernel_initializer='he_uniform')(x)
x = BatchNormalization()(x)
x = Activation('elu')(x) 

# CONNECT GROUPS TO DENSE LAYERS
x = concatenate(outs2+[x])
x = Dense(100,kernel_initializer='he_uniform')(x)
x = Dropout(0.2)(x)
x = BatchNormalization()(x)
x = Activation('elu')(x)
x = Dense(100,kernel_initializer='he_uniform')(x)
x = Dropout(0.2)(x)
x = BatchNormalization()(x)
x = Activation('elu')(x)
x = Dense(100,kernel_initializer='he_uniform')(x)
x = Dropout(0.2)(x)
x = BatchNormalization()(x)
x = Activation('elu')(x)
x = Dense(1,activation='sigmoid')(x)

model = Model(inputs=ins, outputs=x)
model.compile(optimizer=Adam(lr=0.01), loss='binary_crossentropy', metrics=['accuracy'])
#annealer = LearningRateScheduler(lambda x: 1e-2 * 0.95 ** x)
