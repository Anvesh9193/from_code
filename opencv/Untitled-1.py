import os
""" def replace (folder_path, old, new):
    for path,subdirs,files in os.walk(folder_path):
        for names in files:
            if(old.lower in name.lower()):
                file_path = os.path.join(path,name)
                new_name = os.path.join(path,name.lower().replace(old,new))
                os.rename(file_path,new_name) """
             
  
 # Function to rename multiple files 
from shutil import *
path_1 = "D:\python\Session1\Session1"
path = os.chdir("path_1")
i= 0
for file in os.listdir(path):
    new_filename = "Session1_trial{}.png".format(i)
    os.rename(file, new_filename)
    i=i+1 


imagecount=0
for root, dirs, files in os.walk(path):
    for images in files:
        imagecount+= 1
print("no of images :",imagecount)