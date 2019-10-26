import boto3
'''This Collection is used later by aws rekog to inde'''
COLLECTION = 'put_anything_here'
rekog = boto3.client("rekognition")  #rekognition is the service we would use for facial identification
respo = rekog.create_collection(CollectionId=COLLECTION)
