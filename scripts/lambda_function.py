import json
from ppe_rekognition import find_ppe
from label_detection import find_label

def lambda_handler(event, context):
    
    record = json.loads(event['Records'][0]['body'])
    
    message = json.loads(record['Message'])
    
    records = message['Records'][0]
    
    object_key = records['s3']['object']['key']
    
    
    bucket_name = records['s3']['bucket']['name']
    
        
    find_ppe(bucket_name, object_key)
    
        
    find_label(bucket_name, object_key)
        
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

