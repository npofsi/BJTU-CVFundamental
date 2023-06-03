import os
import re
import random
import string
from tqdm import tqdm


ROOT=".\\..\\data\\bjtu-dataset-mixed\\"
source_dataset_path = os.path.join(ROOT, "Dataset\\")
target_path = os.path.join(ROOT, "Cleaned_Dataset\\")

setName =["train", "test"]

if not os.path.exists(target_path):
    os.makedirs(target_path)

school_tags = ["zxb","nm","sy","tsg","mhb","sjz","tyht"]
other_tags = ["all_souls","ashmolean","balliol","bodleian","christ_church",
              "cornmarket","hertford","jesus","keble","magdalen","new","oriel",
              "oxford","pitt_rivers","radcliffe_camera","trinity","worcester"]
all_tags = school_tags + other_tags

counts=[0 for i in range(len(all_tags))]

def genID():
    return ''.join(random.sample(string.digits, 10))

for cate in setName:
    cate_path=os.path.join(source_dataset_path, cate)
    target_cate_path=os.path.join(target_path, cate)
    if not os.path.exists(target_cate_path):
        os.makedirs(target_cate_path)
    for c, tag in enumerate(all_tags):
        plist = os.listdir(cate_path)
        count = 0

        for file in tqdm(plist):
            file_path = os.path.join(cate_path, file)
            if os.path.isdir(file_path) or file.endswith('.json'):
                continue
            if re.match('{}.*'.format(tag), file, re.IGNORECASE):
                file=file.lower()
                changed_file = '{}-{}.jpg'.format(tag,genID())
                target_file_path = os.path.join(target_cate_path, changed_file)
                os.system("copy /b \"{}\" \"{}\"".format(file_path, target_file_path))
                count += 1
        counts[c]+=(count)

for i in range(len(all_tags)):
    print("{}:{}".format(all_tags[i],counts[i]))
