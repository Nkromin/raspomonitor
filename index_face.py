import sys
import boto3
client = boto3.client("rekognition")
def indexFace():
	'''index_faces indexes stored faces in an image to a collection that has already been created ok '''
	response = client.index_faces(
	    CollectionId='put_anything_here', #refer to createcollection.py
	    Image={
	        'S3Object': {
	            'Bucket': 'put_anything_here_2', #refer to createnewbucket.py
	            'Name': str(sys.argv[1])
	        }
	    },
            MaxFaces = 1, #decides the no of faces to index;in this case it will only index the clearest face
	    ExternalImageId=str(sys.argv[2]), #indexes the image with an externalID
	    DetectionAttributes=[
	        'DEFAULT','ALL'
	    ]
            )
#print(str(sys.argv))	    
indexFace()
