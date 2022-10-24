df = pd.DataFrame({"text": [tokens.text for tokens in d], 
                   "lemmatized": [tokens.lemma_ for tokens in d],
                   "part of speech": [tokens.pos_ for tokens in d],
                  "stop word": [tokens.is_stop for tokens in d]})
display(df)                 
sp.displacy.render(d, style='dep', jupyter=True, options={'compact':60})
