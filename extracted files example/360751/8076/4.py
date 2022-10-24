doc = text.loc[text.toxic == 1, 'comment_text'].tolist()
text_model = mk.Text(doc)
for i in range(10):
    print(text_model.make_sentence())
