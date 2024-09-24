import os
import shutil
import re

src_dir = 'orgimg'
dst_dir = 'ans_imgs'

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

for i in os.listdir(src_dir):
    match = re.match(r'tid_\d+_(\w+)\.png', i)
    if match:
        class_name = match.group(1)
        class_dir = os.path.join(dst_dir, class_name)
        if not os.path.exists(class_dir):
            os.makedirs(class_dir)
        src_file = os.path.join(src_dir, i)
        target = os.path.join(class_dir, i)
        try:
            shutil.copy2(src_file, target)
            print(f"{src_dir} => {target} Completed!")
        except Exception as e:
            print(e)
