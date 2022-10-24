train.groupby('PlayId').first()['Yards'] \
    .plot(kind='hist',
          figsize=(15, 5),
          bins=50,
          title='Distribution of Yards Gained (Target)')
plt.show()
