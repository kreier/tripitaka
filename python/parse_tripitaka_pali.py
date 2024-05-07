# Parse the /tripitaka/pli/ms/ folders for JSON files, create a Books.json

import os, sys, json, nltk

# Check execution location, exit if not in /python
if os.getcwd()[-6:] != "python":
    print("This script must be executed inside the /python folder.")
    exit()

booklist = []
output = ""
number_pages = 1
current_line = 0
current_column = 0

def import_booklist(sourcefolder):
    global booklist
    if sourcefolder[-1] != "/":
        sourcefolder += "/"
    booklistfile = sourcefolder + "Books.json"
    print(f"Import the books listed in {booklistfile}: ", end="")
    if not os.path.isfile(booklistfile):
        print("This file does not exist.")
        return
    f = open(booklistfile)
    list_books = json.load(f)
    nr_books = 0
    for book in list_books:
        # print(sourcefolder + book)
        nr_books += 1
        booklist.append(sourcefolder + book + ".json")
    print(f"Found {nr_books} books")
    # booklist = ["../bible/kjv/Genesis.json"]

def investigate(source, folder):
    number_files = 0
    number_folders = 0
    current_folder = "/"
    files_in_folder = 0
    for root, dirs, files in os.walk(source + folder):
        for filename in files:
            if filename.endswith(".json"):
                number_files += 1
                if current_folder != root:
                    number_folders += 1
                    # if files_in_folder > 0:
                    #     print(number_files - files_in_folder)
                    # print(root[len(source):], end=" ") 
                    current_folder = root
                    files_in_folder = number_files
    # print(number_files - files_in_folder)
    return number_files, number_folders



if __name__ == "__main__":
    print('Parse the 3 folders abhidhamma, sutta and vinaya in tripitaka/pli/ms')
    print("Create a Books.json files in this root folder.")
    sourcefolder = "../tripitaka/pli/ms"
    print(len(sourcefolder))
    # directory = os.getcwd()[:-7] +  "/md"
    print("start parsing ...")
    current_folder = ""
    folder = ""
    current_json_files = 0
    total_files = 0
    total_folders = 0
    folders_sutta = 0
    folders_abhidhamma = 0
    folders_vinaya = 0
    files_sutta = 0
    files_abhidhamma = 0
    files_vinaya = 0
    for root, dirs, files in os.walk(sourcefolder):
        for filename in files:
            if filename.endswith(".json"):
                total_files += 1
                if root != current_folder: # found a new folder
                    if current_json_files > 0: # exclude the start condition for first line
                        folder = current_folder[19:]
                        print(f"{folder}/: {current_json_files} files")
                        total_folders += 1
                        if folder[1:6] == "sutta":
                            folders_sutta += 1
                        if folder[1:6] == "vinay":
                            folders_vinaya += 1
                        if folder[1:6] == "abhid":
                            folders_abhidhamma += 1
                    current_json_files = 1
                    current_folder = root
                else:
                    current_json_files += 1
                folder = root[19:]
                if folder[1:6] == "sutta":
                    files_sutta += 1
                if folder[1:6] == "vinay":
                    files_vinaya += 1
                if folder[1:6] == "abhid":
                    files_abhidhamma += 1                    
    print(f"{folder}/: {current_json_files} files")
    folders_abhidhamma +=1
    # files_abhidhamma += current_json_files
    
    print(f"\nIn total we have {total_files} files in {total_folders} folders.")
    print(f"Folders Vinaya: {folders_vinaya}      with {files_vinaya} files.")
    print(f"Folders Sutta: {folders_sutta}      with {files_sutta} files.")
    print(f"Folders Abhidhamma: {folders_abhidhamma}  with {files_abhidhamma} files.")

    print("\nImproved version with a function: ")
    f = [ "vinaya", "sutta", "abhidhamma"]
    for folder in f:
        number_files, number_folders = investigate("../tripitaka/pli/ms/", folder)
        print(f"Folder {folder} contains {number_files} files in {number_folders} folders.")
                # print(os.path.join(root, filename))       
            # print(root, " - ", dirs, " - ", filename)
