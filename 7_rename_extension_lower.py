import os


directory = os.getcwd()


for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
        name, ext = os.path.splitext(filename) 
        new_filename = name + ext.lower() 

        if filename != new_filename:  # 避免重复重命名
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            os.rename(old_path, new_path)
            print(f"rename: {filename} → {new_filename}")

print("done")
