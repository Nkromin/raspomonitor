import boto3
COLLECTION = 'raspox3'
rekog = boto3.client("rekognition")
respo = rekog.create_collection(CollectionId=COLLECTION)
