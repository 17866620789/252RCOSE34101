import os


directory = os.getcwd()


for root, _, files in os.walk(directory):
    for filename in files:
        new_filename = filename.upper()  


        old_path = os.path.join(root, filename)
        new_path = os.path.join(root, new_filename)

        if filename != new_filename:
            os.rename(old_path, new_path)
            print(f"rename: {filename} → {new_filename}")

print("done")
