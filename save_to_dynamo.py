import boto3

dynamodb = boto3.client('dynamodb')

def save_to_dynamo (dictionary, key_name):
    
    labels = []
    
    for k in dictionary:
        
        info = "Label: " + k + ", Confidence Score: " + str(dictionary[k]['Confidence'])
        
        labels.append(info)
        
    dynamodb.put_item(TableName='cwDatabaseS2003045-myDynamoDBTable-1WHPKTW5U62P9', Item = {"ImageName": {"S": key_name}, "Labels":{"SS": labels}})
        
    print("item have been added to database")
    
    
