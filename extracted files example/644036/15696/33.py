train.groupby('SnapHandoffSeconds')['Yards'].mean().plot(kind='barh',
                                                         color=color_pal[1],
                                                         figsize=(15, 5),
                                                         title='Average Yards Gained by SnapHandoff Seconds')
plt.show()
