import boto3
import sys
import json
import sqlite3
from datetime import datetime
conn = sqlite3.connect('mark.db')
collection_name = "ANything_here"
image_file = str(sys.argv[1])
now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

def search_faces_by_image():
    # assumes aws default region and credentials
    rekognition_client = boto3.client('rekognition')
    with open(image_file, 'rb') as image:
        rekognition_response = rekognition_client.search_faces_by_image(
            Image={'Bytes': image.read()},
            CollectionId=collection_name)
    try:
        output = rekognition_response['FaceMatches'][0]['Face']['ExternalImageId']
        #print(output)
        conn.execute("INSERT INTO ATT(NAME,DATE)  VALUES(?, ?)",(output, formatted_date))
        conn.commit()
        conn.close()
        print("uploaded to database successfully")
    except IndexError:
        print("User not registered, please register first. Contact Dept")
search_faces_by_image()
''' module fetches image result + stores into mark.db '''
