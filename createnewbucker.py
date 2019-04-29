import boto3
s3 = boto3.resource('s3')
bucket = s3.create_bucket(
    ACL='public-read-write',
    Bucket='raspo'
)
