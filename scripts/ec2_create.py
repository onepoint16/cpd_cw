import boto3

client = boto3.client('ec2', region_name="us-east-1") 

response = client.run_instances(
    ImageId= 'ami-08e4e35cccc6189f4',
    InstanceType= 't2.small',
    MaxCount=1,
    MinCount=1,
    KeyName = 'vockey' )
    
    