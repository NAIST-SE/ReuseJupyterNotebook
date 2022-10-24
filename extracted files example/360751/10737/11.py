#%% import
import numpy as np
import pandas as pd
import spacy as sp
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score


# get data and make json format for spacy
train = pd.read_csv('../input/train.csv', nrows=10_000)  ## using part of the data again
texts = train.question_text.tolist()
cats = train.target.apply(lambda t: {'cats': {'Insincere': t == 1}}).tolist()
train_texts, dev_texts, train_cats, dev_cats = train_test_split(texts, cats, 
        test_size=0.2, random_state=90)
train_data = list(zip(train_texts, train_cats))
print("Example format \n", train_data[0:10])


#%% set up the pipeline
nlp_bl = sp.blank('en') 
nlp_bl.vocab.vectors.name = 'spacy_pretrained_vectors'
textcat = nlp_bl.create_pipe('textcat')
nlp_bl.add_pipe(textcat, last=True)
textcat.add_label('Insincere')


# train
n_iter = 10
other_pipes = [pipe for pipe in nlp_bl.pipe_names if pipe != 'textcat']
with nlp_bl.disable_pipes(*other_pipes):  #only train textcat
    optimizer = nlp_bl.begin_training()
    print("Training the model...")
    for i in range(n_iter):
        losses = {}
        batches = sp.util.minibatch(train_data, size=sp.util.compounding(4., 32., 1.001))
        for batch in batches:
            texts, annotations = zip(*batch)
            nlp_bl.update(texts, annotations, sgd=optimizer, drop=0.2,
                        losses=losses)
        print("iter {} loss: {:4f}".format(i, losses['textcat']))

        
# evaluate model
preds = []
docs = (nlp_bl(text) for text in dev_texts)
for doc in docs:
    pred = doc.cats['Insincere']
    preds.append(pred)
    
truths = [val['Insincere'] for val in [dc['cats'] for dc in dev_cats]]

#%% find best threshold
best_thresh = 0.0
best_score = 0.0
for thresh in np.arange(0, 1, 0.01):
    score = f1_score(truths, preds > thresh)
    if score > best_score:
        best_thresh = thresh
        best_score = score
print(best_thresh, best_score)
