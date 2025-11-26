import os
import re


folder_path = os.getcwd()


correct_format = re.compile(r"([A-Z]{3,5}-\d{3,4})", re.IGNORECASE)


missing_dash_format = re.compile(r"([A-Z]{3,5})(\d{3,4})", re.IGNORECASE)


unwanted_prefixes = ["*****"]

for root, _, files in os.walk(folder_path):
    for file in files:
        old_path = os.path.join(root, file)
        filename, ext = os.path.splitext(file)


        ext = ext.lower()


        for prefix in unwanted_prefixes:
            filename = filename.replace(prefix, "").strip()


        match = correct_format.search(filename)
        if match:
            series_id = match.group(1).upper()  # 统一大写
        else:

            fix_match = missing_dash_format.match(filename)
            if fix_match:
                series_id = f"{fix_match.group(1).upper()}-{fix_match.group(2)}"
            else:
                series_id = "unknow"

        title = filename.replace(series_id.replace("-", ""), "").strip().replace("_", " ")
        title = re.sub(r"\s+", " ", title)  


        if title:
            new_filename = f"{series_id} {title}{ext}"
        else:
            new_filename = f"{series_id}{ext}"

        new_path = os.path.join(root, new_filename)

        if old_path != new_path:
            print(f"rename: {file} → {new_filename}")
            os.rename(old_path, new_path)

print("done")
