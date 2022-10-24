# get spacy vector
lgword = nlp_lg("and")
lgvec =   ",".join(lgword.vector[0:10].round(5).astype(str))

# get glove vector
glv = pd.read_csv('../input/embeddings/glove.840B.300d/glove.840B.300d.txt', header=None, sep=' ', skiprows=2, nrows=5, index_col=[0])
glvec = glv.loc['and', 0:10].round(5).astype(str).str.cat(sep=' ')

print(lgword.vector.shape[0], "\n",
      lgvec, "\n",
      glv.shape[1], "\n",
      glvec)
