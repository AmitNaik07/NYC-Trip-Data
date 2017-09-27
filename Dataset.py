import csv
import pandas as pd
import requests           #sudo pip install requests
from contextlib import closing
import matplotlib.pyplot as plt

green_url = 'https://s3.amazonaws.com/nyc-tlc/trip+data/green_tripdata_2015-09.csv'               # url string obtained from using 'Inspect' option on browser
#yellow_url ='https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2015-09.csv'

with requests.Session() as s:
    download = s.get(green_url)																   	  # downloading file

    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    green_list = list(cr)
    with open('/Users/amitnaik/Documents/CapitalOne/green_output.csv', "wb") as csv_file:
    	writer = csv.writer(csv_file, delimiter=',')
        for line in green_list:
            writer.writerow(line)																  #writing downloaded data line wise to local filesystem

green_list =pd.read_csv('Users/Documents/green_output.csv') 
print "Number of rows loaded are: " , len(green_list.index)										  #printing number of rows
print "Number of columns loaded are: " , len(green_list.columns)                                  #printing number of columns											 	
