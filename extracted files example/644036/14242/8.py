fi = pd.DataFrame(index=clf.feature_names_)
fi['importance'] = clf.feature_importances_
fi.loc[fi['importance'] > 0.1].sort_values('importance').plot(kind='barh', figsize=(15, 25), title='Feature Importance')
plt.show()
