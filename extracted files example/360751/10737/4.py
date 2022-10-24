c = nlp_sm('What capital city is the prettiest?') 
d = nlp_sm('Which country has the nicest people?')
e = nlp_sm('Why are aliens so smart?')

print("\n", c.similarity(d),
        c.similarity(e))
