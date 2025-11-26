import os


TARGET_FOLDER = os.getcwd()


files = [f for f in os.listdir(TARGET_FOLDER) if os.path.isfile(os.path.join(TARGET_FOLDER, f))]

print("list:")
for file in files:
    print(file)

