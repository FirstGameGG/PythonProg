import os
import re

folder_path = r'C:\Users\iamfi\Pictures\Camera Roll\Camera Roll'  # Replace with the path to your folder

for filename in os.listdir(folder_path):
    print("Original filename:", filename)
    match = re.match(r'.*IMG_(\d+)$', filename)
    if match:
        new_filename = 'IMG_' + match.group(1)
        print("New filename:", new_filename)
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
