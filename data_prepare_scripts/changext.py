#Change file extensions in images/dataset_release from .jpg to .png recursively
#
# Usage: python changext.py
#recursively

import os
import re

rdir='./images/dataset_release/'
dirlist = os.listdir(rdir)

for dir in dirlist:
    if os.path.isdir(rdir+dir):
        filelist = os.listdir(rdir+dir)
        for file in filelist:
            if not os.path.isdir(rdir+dir+'/'+file) and (file.endswith('.jpg') or file.endswith('.jpeg')):
                os.rename(rdir+dir+'/'+file, rdir+dir+'/'+re.sub('\.jpg', '.png',file))
            #if json file then change its content
            if not os.path.isdir(rdir+dir+'/'+file) and file.endswith('.json'):
                with open(rdir+dir+'/'+file, 'r') as f:
                    content = f.read()
                with open(rdir+dir+'/'+file, 'w') as f:
                    f.write(re.sub('\.jpg', '.png',content))
        


    
