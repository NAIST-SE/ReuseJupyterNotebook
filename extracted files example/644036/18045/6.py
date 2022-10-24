fig, ax = plt.subplots()
tt.query('drift == False and signal in @anchors') \
    .groupby('open_channels') \
    .plot(x='time', y='signal', style='.', figsize=(15, 5), ax=ax)
plt.show()
