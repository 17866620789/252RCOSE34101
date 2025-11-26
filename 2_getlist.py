import os


TARGET_FOLDER = os.getcwd()


files = []
for root, _, filenames in os.walk(TARGET_FOLDER):
    for filename in filenames:
        files.append(os.path.join(root, filename)) 


print("list:")
for file in files:
    print(file)

