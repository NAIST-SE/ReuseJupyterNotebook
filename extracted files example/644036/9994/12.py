import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning) 
sns.pairplot(bmd_with_stats.dropna(),
             vars=['mean_meter_reading','min_meter_reading',
                   'max_meter_reading','square_feet','year_built'],
             hue='primary_use')
plt.show()
