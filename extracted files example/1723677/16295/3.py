ct = train.shape[0]

# INPUTS TO ROBERTA
ids = np.ones((ct,MAX_LEN),dtype='int32')
att = np.zeros((ct,MAX_LEN),dtype='int32')
tok = np.zeros((ct,MAX_LEN),dtype='int32')
# QUESTION ANSWER TARGETS
tar1 = np.zeros((ct,MAX_LEN),dtype='int32')
tar2 = np.zeros((ct,MAX_LEN),dtype='int32')
# SEGMENTATION TARGETS
tar3 = np.zeros((ct,MAX_LEN),dtype='int32')
# SENTIMENT TARGETS
tar4 = np.zeros((ct),dtype='int32')
# CHAR CENTERS
cha = np.zeros((ct,MAX_LEN),dtype='float32')

for k in range(train.shape[0]):
    
    # FIND TEXT / SELECTED_TEXT OVERLAP
    text1 = " "+" ".join(train.loc[k,'text'].split())
    text2 = " ".join(train.loc[k,'selected_text'].split())
    idx = text1.find(text2)
    chars = np.zeros((len(text1)))
    chars[idx:idx+len(text2)]=1
    if text1[idx-1]==' ': chars[idx-1] = 1 
    enc = tokenizer.encode(text1)
            
    # FIND OFFSETS, CHAR CENTERS
    off = []; ii=0; ct = 0
    for i,t in enumerate(enc.ids):
        w = tokenizer.decode([t])
        off.append((ii,ii+len(w)))
        ii += len(w)
        cha[k,i] = ct + len(w)/2.
        ct += len(w)
        
    # FIND SELECTED TEXT TOKENS
    tks = []
    for i,(a,b) in enumerate(off):
        sm = np.sum(chars[a:b])
        if sm>0: tks.append(i)
        
    # CREATE ROBERTA INPUTS
    stok = sentiment_id[train.loc[k,'sentiment']]
    ids[k,:len(enc.ids)+2] = [0] + enc.ids + [2]
    att[k,:len(enc.ids)+2] = 1
    if DO_QUES_ANS: # USE THIS FOR QUESTION ANSWER 
        ids[k,len(enc.ids)+2:len(enc.ids)+5] = [2] + [stok] + [2]
        att[k,len(enc.ids)+2:len(enc.ids)+5] = 1
        
    # CREATE ROBERTA TARGETS
    if len(tks)>0:
        tar1[k,tks[0]+1] = 1
        tar2[k,tks[-1]+1] = 1
    for j in range(len(tks)):
        tar3[k,tks[j]+1] = 1
    tar4[k] = sentiment_tar[train.loc[k,'sentiment']]
