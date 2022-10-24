import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

sns.jointplot('budget_log', 'revenue_log', train.loc[train['budget_log'] > 1], kind='reg')
plt.show()
