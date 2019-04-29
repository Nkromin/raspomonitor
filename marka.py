import os
s = "test"
s1 = s+'.jpg'
os.system("raspistill -o "+s1+" -t 3000")
print("Identifying blob within collection")
os.system("python3 search_index_face.py "+s1)


