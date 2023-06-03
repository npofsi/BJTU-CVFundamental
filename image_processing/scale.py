import os
from PIL import Image

SCALE = 1024
ROOT=".\\..\\data\\bjtu-dataset-mixed\\"

source_dataset_path = os.path.join(ROOT, "SourceDataset\\")
target_dataset_path = os.path.join(ROOT, "ResizedDataset_%.0fp\\"%SCALE)
setName =["train\\", "test\\"]

def resize(image, size, scale):
    width, height = size
    if(width > height):
        replace_width = scale
        replace_height = int(height*scale/width)
    else:
        replace_height = scale
        replace_width = int(width*scale/height)
    return replace_width, replace_height

def del_alpha_tun(image):
    background = Image.new("RGB", image.size, (255, 255, 255))
    channels = image.split()
    if(len(channels)==4):
        background.paste(image, mask = channels[3])
    else:
        background.paste(image)
    return background

if not os.path.exists(target_dataset_path):
    os.makedirs(target_dataset_path)

for cate in setName:
    now_data_path = os.path.join(source_dataset_path, cate)
    target_data_path = os.path.join(target_dataset_path, cate)
    if not os.path.exists(target_data_path):
        os.makedirs(target_data_path)
    files = os.listdir(now_data_path)
    for file in files:
        image = Image.open(os.path.join(now_data_path, file))
        image = image.resize(resize(image, image.size, SCALE))
        image.load()
        del_alpha_tun(image).save(os.path.join(target_data_path, file), 'JPEG', optimize=True)


        

