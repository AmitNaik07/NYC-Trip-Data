import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_predict	
from sklearn.linear_model import LinearRegression

green_list =pd.read_csv('/Users/amitnaik/Documents/CapitalOne/green_output.csv')

clean_RCID =green_list[~((green_list.RateCodeID>=1) & (green_list.RateCodeID<=6))].index                                    	# cleaning RateCodeID since 99 is an outlier 
green_list.loc[clean_RCID, 'RateCodeID'] =2	
green_list.Fare_amount = green_list.Fare_amount.abs()
green_list.MTA_tax = green_list.MTA_tax.abs()
green_list.Tolls_amount = green_list.Tolls_amount.abs()
green_list.improvement_surcharge = green_list.improvement_surcharge.abs()
green_list.Total_amount = green_list.Total_amount.abs()

green_list['Trip_type '] = green_list['Trip_type '].replace(np.NaN,1)

green_list =green_list.drop(['VendorID','lpep_pickup_datetime','Lpep_dropoff_datetime','Store_and_fwd_flag','Pickup_longitude','Pickup_latitude','Dropoff_longitude','Dropoff_latitude','Extra','Tolls_amount','Ehail_fee', 'Trip_type '],axis =1)

tip =green_list[(green_list['Total_amount']>=2.5)]
green_list =green_list[(green_list['Total_amount']>=2.5)]	
tip['Tip_percentage'] = (tip.Tip_amount/tip.Total_amount) * 100
tips =pd.DataFrame()
tips =tip['Tip_percentage']
tips =tips.values.reshape((1490167,1))

lm =LinearRegression()
model = lm.fit(green_list,tips)
predictions = lm.predict(green_list)
print(predictions)[0:5]																											#predicting the next 5 values of tip percentage
print "The accuracy is: ", lm.score(green_list,tips)
