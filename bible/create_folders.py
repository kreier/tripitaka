import os
import json

# Paths to the JSON file and target directory
source_folder_list = "./nwt/Books.json"
target_directory = "./nwt_xml"

# Load folder names from the JSON file
with open(source_folder_list, "r") as file:
    folder_names = json.load(file)

# Create folders in the target directory if they don't exist
for folder_name in folder_names:
    folder_path = os.path.join(target_directory, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder_path}")
    else:
        print(f"Folder already exists: {folder_path}")
