'''The Driver code to execute the search_in_thecollection.py'''
import os
s = "test"
s1 = s+'.jpg'
os.system("raspistill -o "+s1+" -t 3000") #Taking Single Image from RaspberryPI Camera
print("Identifying face within collection")
os.system("python3 search_index_face.py "+s1)


