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





if __name__ == "__main__":
    print('Parse the 3 folders abhidhamma, sutta and vinaya in tripitaka/pli/ms')
    print("Create a Books.json files in this root folder.")
    sourcefolder = "../tripitaka/pli/ms"
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
    nr_json = 0
    for root, dirs, files in os.walk(sourcefolder):
        for filename in files:
            if filename.endswith(".json"):
                nr_json += 1
            # if not filename.startswith("."):
                total_files += 1
                if root != current_folder:
                    if current_json_files > 0:
                        folder = current_folder[19:]
                        print(f"{folder}/: {current_json_files} files")
                        total_folders += 1
                        if folder[1:6] == "sutta":
                            folders_sutta += 1
                            files_sutta += 1
                        if folder[1:6] == "vinay":
                            folders_vinaya += 1
                            files_vinaya += 1
                        if folder[1:6] == "abhid":
                            folders_abhidhamma += 1
                            files_abhidhamma += 1
                    current_json_files = 1
                    current_folder = root
                else:
                    current_json_files += 1
                    if folder[1:6] == "sutta":
                        files_sutta += 1
                    if folder[1:6] == "vinay":
                        files_vinaya += 1
                    if folder[1:6] == "abhid":
                        files_abhidhamma += 1                    
    print(f"{folder}/: {current_json_files} files")
    folders_abhidhamma +=1
    files_abhidhamma += current_json_files
    
    print(f"\nIn total we have {total_files} files in {total_folders} folders.")
    print(f"Folders Vinaya: {folders_vinaya}      with {files_vinaya} files.")
    print(f"Folders Sutta: {folders_sutta}      with {files_sutta} files.")
    print(f"Folders Abhidhamma: {folders_abhidhamma}  with {files_abhidhamma} files.")
    print(f"Does this allign with a total of {nr_json} JSON files?")
                # print(os.path.join(root, filename))       
            # print(root, " - ", dirs, " - ", filename)
