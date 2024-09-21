import os
from pathlib import Path
import logging
import shutil

filespath = "C:/Users/hunte/Desktop/learn/categories/automation/randomfiles/"


subdirecectoriespath = "C:/Users/hunte/Desktop/learn/categories/automation"

filespath_list = os.listdir(filespath)
dir_list = os.walk(subdirecectoriespath)
for x in filespath_list:
    if x.endswith(".jpg") or x.endswith(".png"):
        
        if not os.path.isdir(subdirecectoriespath+"/images"):
            os.makedirs(subdirecectoriespath+"/images")
        shutil.move(filespath+x, subdirecectoriespath+"/images/"+x)
        logging.info(filespath+x+" moved to "+subdirecectoriespath+"/images")



        pass
    elif x.endswith(".pdf"):
        
        if not os.path.isdir(subdirecectoriespath+"/documents"):
            os.makedirs(subdirecectoriespath+"/documents")
        shutil.move(filespath+x, subdirecectoriespath+"/documents/"+x)
        logging.info(x+" moved to "+subdirecectoriespath+"/documents")
        pass
    elif x.endswith(".mp4") or x.endswith(".mov"):
    
        if not os.path.isdir(subdirecectoriespath+"/videos"):
            os.makedirs(subdirecectoriespath+"/videos")
        shutil.move(filespath+x, subdirecectoriespath+"/videos/"+x)
        logging.info(filespath+x+" moved to "+subdirecectoriespath+"/videos")
        pass
    elif x.endswith(".wav") or x.endswith(".mp3"):
        
        if not os.path.isdir(subdirecectoriespath+"/audios"):
            os.makedirs(subdirecectoriespath+"/audios")
        shutil.move(filespath+x, subdirecectoriespath+"/audios/"+x)
        logging.info(x+" moved to "+subdirecectoriespath+"/audios")
        pass
    else:
        print("There are no files in the filespath variable")
        break
    


    

        
