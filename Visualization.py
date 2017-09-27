import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
from tabulate import tabulate             
import seaborn as sns
import numpy as np
import matplotlib.animation as animation

green_list =pd.read_csv('/Users/Documents/green_output.csv')

green_list['Pickup_dt'] = green_list.lpep_pickup_datetime.apply(lambda x:dt.datetime.strptime(x,"%Y-%m-%d %H:%M:%S"))
green_list['Pickup_hour'] = green_list.Pickup_dt.apply(lambda x:x.hour)
#green_list['Dropoff_dt'] = green_list.Lpep_dropoff_datetime.apply(lambda x:dt.datetime.strptime(x,"%Y-%m-%d %H:%M:%S"))

fig,ax = plt.subplots(1,1,figsize=(10,5))																					#plotting the mean and median on a single graph
table_list =green_list.pivot_table(index='Pickup_hour', values='Trip_distance',aggfunc=('mean','median')).reset_index()     # pivot table to aggregate the trip distance by hour

table_list.columns = ['Hour','Mean Trip Distance','Median Trip Distance']
table_list[['Mean Trip Distance','Median Trip Distance']].plot(ax=ax)
print tabulate(table_list.values.tolist(),["Hour","Mean Trip distance","Median Trip Distance"])				    #printing tabular version of graph
																			        
plt.title('Trip distance by pickup hour')
plt.xlabel('Hours (24 hour format)')
plt.ylabel('Distance (miles)')
plt.xlim([0,23])													    # 24 hour format
plt.show()

trips =green_list[(green_list.RateCodeID==2) | (green_list.RateCodeID==3)]						    # 2 represents JFK while 3 represnts Newark airports
print "Number of trips that originate or terminate at NYC are:", len(trips.index)

fare_amount =trips.Fare_amount.mean()
print "Average fare amount for tips to and fro the airports are: $",fare_amount

amt =trips.mean()
#print(amt[16])														    # mean comes out to be approximately 1.68
print "Average mode of payment while going to and fro airports is cash."					            # 2 refers to credit card mode of payment

v_air =trips.Trip_distance
v_nonair =green_list.loc[~green_list.index.isin(v_air), "Trip_distance"]						    # taking the complement of v_air


trips.Pickup_hour.value_counts(normalize=True).sort_index().plot()							    # plotting hourly distribution
green_list.loc[~green_list.index.isin(v_air.index),'Pickup_hour'].value_counts(normalize=True).sort_index().plot()
plt.xlabel('Hours (24 hours)')
plt.ylabel('Trip count')
plt.title('Hourly distribution of Trips')
plt.legend(['Airport trips','Non-airport trips'],bbox_to_anchor=(.05, 1), loc=2, borderaxespad=0.)
plt.show()

clean_RCID =green_list[~((green_list.RateCodeID>=1) & (green_list.RateCodeID<=6))].index                                    # cleaning RateCodeID since 99 is an outlier 
green_list.loc[clean_RCID, 'RateCodeID'] =2										    # 2 was seen as the most common cash method

df = green_list.pivot_table(index='Pickup_hour', columns='RateCodeID', values='Fare_amount', aggfunc=np.median)        	    # plotting heat map
																															# get another heatmap which provides extra information)
sns.heatmap(df, annot=True, fmt=".1f")
plt.show()
