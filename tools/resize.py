

#copy Cleaned_Dataset to Cleaned_Dataset_...p
# just copy file strcuture
# Path: tools\resize.py

import os
from PIL import Image

scale = 32

root="C:\\Left\\Workspace\\BJTU-CVFundamental\\"
dataset_path = os.path.join(root, "data\\bjtu-dataset-mixed\\Cleaned_Dataset\\")
cates =["train\\", "test\\"]

target_path = os.path.join(root, "data\\bjtu-dataset-mixed\\Cleaned_Dataset_{}p\\".format("%.0f"%scale))
if not os.path.exists(target_path):
    os.makedirs(target_path)


cot=0
for cate in cates:
    now_data_path = os.path.join(dataset_path, cate)
    target_data_path = os.path.join(target_path, cate)
    if not os.path.exists(target_data_path):
        os.makedirs(target_data_path)
    #resize all images in from now_root to target_root
    files = os.listdir(now_data_path)
    for file in files:
        cot+=1
        #resize file
        image = Image.open(os.path.join(now_data_path, file))
        
        #get width and height
        width, height = image.size
        #rewrite width and height(resize higher one to scale)
        if(width>height):
          replace_width = scale
          replace_height = int(height*scale/width)
        else:
          replace_height = scale
          replace_width = int(width*scale/height)
        #resize
        image = image.resize((replace_width, replace_height))

        image.load()

        background = Image.new("RGB", image.size, (255, 255, 255))

        channels = image.split()
        if(len(channels)==4):
          background.paste(image, mask = channels[3])
        else:
          background.paste(image)
        #save
        background.save(os.path.join(target_data_path, file), 'JPEG', optimize=True)
        print("{} files resized".format(cot))

print("Resize Done!")

        

