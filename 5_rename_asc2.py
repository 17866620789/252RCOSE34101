import os
import re


folder_path = os.getcwd()


for filename in os.listdir(folder_path):
    old_path = os.path.join(folder_path, filename)

    
    if os.path.isfile(old_path):
        
        ext = os.path.splitext(filename)[1]

        new_filename = ''.join(re.findall(r'[\u4e00-\u9fff]+', filename)) + ext

        new_path = os.path.join(folder_path, new_filename)

        if old_path != new_path and new_filename:
            os.rename(old_path, new_path)
            print(f'rename : {filename} → {new_filename}')

print("done")

