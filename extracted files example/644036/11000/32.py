# Unfreeze the model and search for a good learning rate
learn.unfreeze()
learn.lr_find()
fig = learn.recorder.plot(return_fig=True)
fig.set_size_inches(15,5)
