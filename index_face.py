import sys
import boto3
client = boto3.client("rekognition")
def indexFace():
	response = client.index_faces(
	    CollectionId='raspox3',
	    Image={
	        'S3Object': {
	            'Bucket': 'raspo',
	            'Name': str(sys.argv[1])
	        }
	    },
            MaxFaces = 1,
	    ExternalImageId=str(sys.argv[2]),
	    DetectionAttributes=[
	        'DEFAULT','ALL'
	    ]
            )
print(str(sys.argv))	    
indexFace()
