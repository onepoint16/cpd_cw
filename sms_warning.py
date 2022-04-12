import boto3
import os
import json 

sns = boto3.client('sns')

def send_message(key_name):
    
    number = '+447850246290'

    message = " is not wearing correct PPE"
    
    message = key_name + message
        
    sns.publish(PhoneNumber = number, Message = message)
    
    print("sms has sent")
        
    