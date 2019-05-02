# Introduction :

When attendance is done manually it generally wastes a lot of productive time of the class. This proposed solution for the current problem is through automation of attendance system using face recognition. Face is the primary identification for any human. This project describes the method of detecting and recognizing the face in real-time using Raspberry Pi. 


# Problem Statement :

Normally, person is remaining present in the fields taken care by the authority by taking their presence manually. Even though so many cases are there in every field where fault attendance can be made easily and wrong result can be presented to the higher authority. So in order to find the maximum accuracy, automatic system should be developed that can identify the person uniquely by his face, fingerprint, iris, lips print etc. Suppose we are taking example of the college in which class room only 90% students are present and teacher making 92% present because 2% fault is made by the other student then it will present the wrong information to the higher authorities. Also if a student is present in the class, there are chances that he can be marked absent.
So the problem is even student is not present in the class room even though his present is made by the other student. So in order to minimize the errors made we have developed a facial identification system using raspberry pi which will give almost 100% accurate result.


# Solution :

As an implementation of the proposed system we will develop an application which will help us to identify the existing students from the class and make student present or absent on the basis of facial identification from the stored reference of face images. The system we are going to design is based on facial recognition using Raspberry pi, python, AWS services and a camera. In this system matching of face from stored face images is being used. 


# Modules :

## The modules that will be used are as follows:
    • Registration Module
    • Search Module
## Mandatory modules are:
    • Create Bucket
    • Create Collection
## The Registration Module further comprises of four sub modules:
    • Camera Input
    • Upload Images
    • Index Faces
## The Search Module comprises of one sub module:
    • Search Faces
    • Add to Database

# Requirments :

## Hardware Requirements:
    • Raspberry pi 3B
    • Raspberry pi camera module 5 MP
    • SD Card flashed with raspbian os
    • An Active Internet Connection
## Software Requirements :
    • Python 3.6+
    • AWS CLI
    • SQLite3
   
# Installation
Install and Configure AWS CLI : https://devopsmates.com/install-configure-aws-cli-amazon-web-services-command-line-interface/

# Execution and Output :
    python3 regis.py
   ![](https://user-images.githubusercontent.com/22393734/57092049-28138c80-6d28-11e9-8ab6-95c586e6edb0.png)
   
    python3 marka.py
   ![alt text](https://user-images.githubusercontent.com/22393734/57092050-28138c80-6d28-11e9-8d5b-250e6b7f8bbb.png)
  
