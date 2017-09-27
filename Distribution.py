import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import lognorm
import numpy as np

green_list =pd.read_csv('/Users/Documents/green_output.csv')
											
v = green_list.Trip_distance 																					# create a vector to contain Trip Distance

v[~((v-v.median()).abs()>3*v.std())].hist(bins=30) 																# removing outliers 
plt.xlabel('Trip Distance (miles)')
plt.ylabel('Frequency')
plt.title('Histogram of Trip Distance')

scatter,loc,mean = lognorm.fit(green_list.Trip_distance.values,scale=green_list.Trip_distance.mean(), loc=0)    # applying lognorm fit
pdf_fitted = lognorm.pdf(np.arange(0,12,.1),scatter,loc,mean)
plt.plot(np.arange(0,12,0.1),600000*pdf_fitted,'r')      														# limits from 0 to 12 with a step size of 0.1
plt.legend(['Lognormal Fit','Data'])

plt.show()
