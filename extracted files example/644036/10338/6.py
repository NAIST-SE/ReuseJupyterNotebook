# Distribution of Target in Training Set
plt.style.use('ggplot')
plot = train_labels.groupby('Target') \
    .count()['patientId'] \
    .plot(kind='bar', figsize=(10,4), rot=0)
