
#

def genID():
    #generate 6 random lower-letters and 8 digital numbers
    import random
    import string
    return ''.join(random.sample(string.ascii_lowercase, 6)) + ''.join(random.sample(string.digits, 8))

#rename files in ./images/downloaded/

import os
import re

dir='./images/downloaded/'
filelist = os.listdir(dir)
for file in filelist:
    if os.path.isdir(file) or not (file.endswith('.heic') or file.endswith('.jpg') or file.endswith('.jpeg')):
        continue
    os.rename(dir+file, dir+re.sub('.*(\.heic|\.jpg|\.jpeg)', '-'+genID()+'.jpg',file))