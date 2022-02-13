import os
from shutil import copy, move, Error

ext = (
    ".jpg",
    ".jpeg",
    ".jfif",
    ".pjpeg",
    ".pjp" ".png",
    ".avif",
    ".gif",
    ".PNG",
    ".JPG",
    ".JPEG",
)
# dir_src = r"/path/to/folder/with/subfolders"
dir_src = r"/Users/pxi/Documents/Family_and_other"
dir_dst = r"/Users/pxi/Documents/Family_and_other_combined"

# dir_src = r"/Users/pxi/Documents/GitHub/pybots/imgs"
# dir_dst = r"/Users/pxi/Documents/GitHub/pybots/combined"
dup_counter = 0
for root, _, files in os.walk(dir_src):
    for file in files:
        if file.endswith(ext):
            file_path = os.path.join(root, file)
            try:
                move(file_path, dir_dst)
                print(f'moved: {file_path}')
            except Error:
                print(f'duplicate: {file_path}')
                dup_counter += 1
                os.remove(file_path)
            # copy(os.path.join(root, file), dir_dst)
            # move(os.path.join(root, file), dir_dst)
            # print(file)
print(f'duplicates found: {dup_counter}')
