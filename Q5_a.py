import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
from datetime import datetime
import dateutil.parser

d= datetime.now()

green_list =pd.read_csv('/Users/amitnaik/Documents/CapitalOne/green_output.csv')

green_list['Dropoff_dt'] = green_list.Lpep_dropoff_datetime.apply(lambda x:dt.datetime.strptime(x,"%Y-%m-%d %H:%M:%S"))
green_list['Pickup_dt'] = green_list.lpep_pickup_datetime.apply(lambda x:dt.datetime.strptime(x,"%Y-%m-%d %H:%M:%S"))
green_list['Pickup_hour'] = green_list.Pickup_dt.apply(lambda x:x.hour)

green_list['Trip_duration'] =((green_list.Dropoff_dt - green_list.Pickup_dt).apply(lambda x:x.total_seconds()/60.))
green_list['Speed'] =green_list.Trip_distance / (green_list.Trip_duration/60)													#to get the speed in mph
print(green_list["Speed"].median())																								#printing average of speeds

new_speed = green_list[(~(green_list.Speed.isnull())) | (green_list.Speed<100)]													#removing outliers

'''  
This part of code is used to find index of weeks ranging from 1-7, 8-14 and so on.

green_list['Date'] =[d.day for d in green_list["Pickup_dt"]]                 												    #getting just the date
one =pd.DataFrame()																												#creating empty data frames
one =green_list.loc[(green_list['Date']>=1) & (green_list["Date"]<8)]															#getting data frame for days 1-7
two =pd.DataFrame()
two =green_list.loc[(green_list['Date']>=8) & (green_list["Date"]<15)]
three =pd.DataFrame()
three =green_list.loc[(green_list['Date']>=15) & (green_list["Date"]<22)]
four =pd.DataFrame()
four =green_list.loc[(green_list['Date']>=22) & (green_list["Date"]<=30)]

'''											
s1 =new_speed.loc[0:341474]
s2 =new_speed.loc[341475:702674]
s3 =new_speed.loc[702675:1065953]
s4 =new_speed.loc[1065954:1494926]

m1 =s1["Speed"].median()
m2 =s2["Speed"].median()
m3 =s3["Speed"].median()
m4 =s4["Speed"].median()

y =[m1,m2,m3,m4]
x =[1,2,3,4]
plt.scatter(x,y, label='skitscat', color='k', s=25, marker="o")																	#plotting speed as a function of hours
plt.xlabel('Weeks')
plt.ylabel('Speed (mph)')
plt.title('Speed per Week')
plt.show()

#---------------------------------------------------------

plt.plot(green_list["Speed"])																									#plotting speed as a function of hours
plt.xlabel('Hours (24 hours)')
plt.ylabel('Speed (mph)')
plt.title('Hourly distribution of Speed')
plt.ylim([0,40])
plt.xlim([0,23])
plt.show()
