import boto3
s3 = boto3.resource('s3') #s3 is the service to store the images of the individual on cloud 
'''ACL is the key to remotely accessing the files on the cloud ok'''
bucket = s3.create_bucket( 
    ACL='public-read-write',
    Bucket='put_anything_here'
)
