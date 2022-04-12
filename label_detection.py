import boto3
import os
import json
from decimal import Decimal 
from save_to_dynamo import save_to_dynamo

client = boto3.client('rekognition')

label_dict = dict()

labels_to_store = dict()

def find_label(bucket_name, key_name):
    
    label_dict = client.detect_labels(Image={'S3Object': {'Bucket': bucket_name,'Name': key_name}}, MaxLabels=5)
    
    for label in label_dict['Labels']:
    
        label_name = label['Name']
        conf = label['Confidence']
        
        conf = Decimal(conf)
        
        labels_to_store[label_name] = {"Confidence" : (conf)}


    
    save_to_dynamo(labels_to_store, key_name)