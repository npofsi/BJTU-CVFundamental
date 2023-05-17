import os
import re
import random
import string
from tqdm import tqdm
root="C:\\Left\\Workspace\\BJTU-CVFundamental\\"
dataset_path = os.path.join(root, "data\\bjtu-dataset-mixed\\Dataset\\")
cates =["train", "test"]

target_path = os.path.join(root, "data\\bjtu-dataset-mixed\\Cleaned_Dataset\\")
if not os.path.exists(target_path):
    os.makedirs(target_path)

school_tags = ["zxb","nm","sy","tsg","mhb","sjz","tyht"]
other_tags = ["all_souls","ashmolean","balliol","bodleian","christ_chruch","cornmarket","hertford","jesus","keble","magdalen","new","oriel","oxford","pitt_rivers","radcliffe_camera","trinity","worcester"]
all_tags = school_tags + other_tags
counts=[0 for i in range(len(all_tags))]
def genID():
    #generate 6 random lower-letters and 8 digital numbers

    return ''.join(random.sample(string.digits, 10))


for cate in cates:
    cate_path=os.path.join(dataset_path, cate)
    target_cate_path=os.path.join(target_path, cate)
    if not os.path.exists(target_cate_path):
        os.makedirs(target_cate_path)
    #copy file from cate_path to target_cate_path
    for c, tag in enumerate(all_tags):
        plist = os.listdir(cate_path)
        count = 0

        for file in tqdm(plist):
            
            file_path = os.path.join(cate_path, file)
            
            #skip dirs and json
            if os.path.isdir(file_path) or file.endswith('.json'):
                continue

            #filtering file start with tag use regex
            if re.match('{}(-|_).*'.format(tag), file, re.IGNORECASE):
                changed_file = '{}-{}.jpg'.format(tag,genID())
                target_file_path = os.path.join(target_cate_path, changed_file)
                os.system("copy /b \"{}\" \"{}\"".format(file_path, target_file_path))
                count += 1
                #print("copy /b \"{}\" \"{}\"".format(file_path, target_file_path))

        counts[c]+=(count)

for i in range(len(all_tags)):
    print("{}:{}".format(all_tags[i],counts[i]))

print("Total images:{}".format(sum(counts)))
print("{}".format(str(counts)))