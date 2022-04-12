import boto3
import os
import json
from sms_warning import send_message

client = boto3.client('rekognition')

ppe_dict = dict()

def find_ppe(bucket, key_name):

    ppe_dict = client.detect_protective_equipment(
    Image={
        'S3Object': {
            'Bucket': bucket,
            'Name': key_name
        }
    },
    SummarizationAttributes={
        'MinConfidence': 0.70,
        'RequiredEquipmentTypes': [
            'FACE_COVER', 'HAND_COVER',
        ]
    })
    
    not_wearing = ppe_dict['Summary']['PersonsWithoutRequiredEquipment']
    
    indeterminate = ppe_dict['Summary']['PersonsIndeterminate']
    
    print(not_wearing)
    
    if (not_wearing):
        print("Would send SMS notification now")
        send_message(key_name)
    elif(indeterminate):
        print("Machine unsure of equipment")
    else:
        print("all good to start working")

    
        
    
        
    
