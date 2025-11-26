import os
import shutil
from PIL import Image


source_folder = os.getcwd()  
static_folder = os.path.join(source_folder, "***")
animated_folder = os.path.join(source_folder, "****")


os.makedirs(static_folder, exist_ok=True)
os.makedirs(animated_folder, exist_ok=True)


total_files = len(os.listdir(source_folder))
count = 0

for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)


    if filename.lower().endswith(".*"):
        try:
            with Image.open(file_path) as img:
                if getattr(img, "is_*", False):
                    shutil.move(file_path, os.path.join(animated_folder, filename))
                else:
                    shutil.move(file_path, os.path.join(static_folder, filename))
            count += 1
            print(f"[{count}/{total_files}] do: {filename}")
        except Exception as e:
            print(f"skip {filename}，error: {e}")

print("done")

