import os
s = input("Enter Roll no")
s1 = s+'.jpg'
os.system("raspistill -o "+s1+" -t 3000")
print("Image Succesfully captured")
print("uploading image to s3")
os.system("python3 upload_face.py "+s1)
print("indexing face")
os.system("python3 index_face.py "+s1+" "+s)
print("face indexed to collection:id raspox")

