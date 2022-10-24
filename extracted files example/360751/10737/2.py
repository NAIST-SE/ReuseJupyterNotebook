nlp_sm = sp.load('en_core_web_sm')
smword = nlp_sm("and")
smvec = ",".join(smword.vector[0:10].round(5).astype(str))

print(smword.vector.shape[0], "\n",
       smvec)
