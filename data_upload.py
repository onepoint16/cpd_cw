import boto3
import os
import time

s3 = boto3.resource('s3')
BUCKET = "mybuckets2003045"

data_dir = "/usr/bin/sg_code/cpd_cw/images"
# "/home/ec2-user/environment/images/images/"

photos = os.listdir(data_dir)

count = 0

for photo in photos:
    path = os.path.join(data_dir, photo)
    s3.Bucket(BUCKET).upload_file(path, photo)
    count =+ 1
    time.sleep(30)
    
    if( count == 5):
        break
    
print("All done")