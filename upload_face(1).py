import sys
import boto3
s3 = boto3.resource('s3')
valo = str(sys.argv[1])
print(str(sys.argv[1]))
data = open(valo, 'rb')
s3.Bucket('raspo').put_object(Key=valo, Body=data)
print("Image Uploaded to Hash(e1.s3)")


