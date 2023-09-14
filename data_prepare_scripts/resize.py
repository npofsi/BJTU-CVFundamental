from PIL import Image
from pillow_heif import register_heif_opener
import os
import re
register_heif_opener()

#get filelist in ./image
filelist = os.listdir('./images')

def genID():
    #generate 6 random lower-letters and 8 digital numbers
    import random
    import string
    return ''.join(random.sample(string.ascii_lowercase, 6)) + ''.join(random.sample(string.digits, 8))

#resize
for file in filelist:
    #skip dirs and not heic files
    if os.path.isdir(file) or not (file.endswith('.heic') or file.endswith('.jpg') or file.endswith('.jpeg')):
        continue

    filepath = './images/' + file
    #open heic images
    image = Image.open(filepath)
    #get width and height
    width, height = image.size
    #rewrite width and height(max of them is 1024)
    replace_width = 1024 if width > height else int(width * 1024 / height)
    replace_height = 1024 if height > width else int(height * 1024 / width)
    #resize
    image = image.resize((replace_width, replace_height))
    #save in ./image/processed/ as jpeg
    image.save('./images/processed/' + re.sub('.*(\.heic|\.jpg)', '-'+genID()+'.jpg',file), 'JPEG')
