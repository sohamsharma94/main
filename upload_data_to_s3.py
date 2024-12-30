import boto3
import boto3.session
import pandas as pd
from io import StringIO
import os 

session=boto3.session.Session()

s3_obj=session.resource('s3')

path='s3://airportdataset'

df=pd.read_csv(r'C:\Users\Lenovo\Downloads\Airline_Data_Ingestion_Project\airports.csv')

airport_df=df[['airport_id','city','state']]
state_df=df[['state','name']]

airport_df.to_csv(path+'/airport_mstr.csv')
state_df.to_csv(path+'/state_mstr.csv')

# print(airport_df.head(),state_df.head())
# s3_obj=boto3.client('s3')

# s3_obj.upload_file(Filename=airport_df.to_csv(StringIO()),
#                    Bucket='airlinedataset',
#                    Key='airports.csv')

