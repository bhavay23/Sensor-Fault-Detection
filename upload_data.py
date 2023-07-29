from pymongo.mongo_client import MongoClient
import pandas as pd
import json


#uniform resource identifier
uri = "mongodb+srv://bhavay_bukkal:mongodbbhavay@1@cluster0.2fetiek.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

#Create database name and collection name
DATABASE_name = "pwskills"
COLLECTION_NAME = "waferfault"

#Now drop the data into database
client[DATABASE_NAME][COLLECTION_NAME]= json_record

# read data as a dataframe
df = pd.read_csv("C:\Users\bhava\OneDrive\Desktop\sensor-fault-detection\sensor-fault-detection\notebooks\wafer_23012020_041211.csv")

#converting to json
json_record = json.load(df.T.to_json)

