# Parse the /tripitaka/pli/ms/ folders for JSON files, create a Books.json

import os, json, csv

# Check execution location, exit if not in /python
if os.getcwd()[-6:] != "python":
    print("This script must be executed inside the /python folder.")
    exit()

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
    list_output = []
    # files_in_folder = 0
    for root, dirs, files in os.walk(source + folder):
        for filename in files:
            if filename.endswith(".json"):
                number_files += 1
                list_output.append([root[len(source):], filename[:-5]])
                if current_folder != root:
                    number_folders += 1
                    # if files_in_folder > 0:
                    #     print(number_files - files_in_folder)
                    # print(root[len(source):], end=" ") 
                    current_folder = root
                    # files_in_folder = number_files
    # print(number_files - files_in_folder)
    header_list = ['path', 'file']
    # print(list_output)
    filename = source + folder + '.csv'
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header_list)
        writer.writerows(list_output)
    print(f"Wrote {source}{folder}.json")
    return number_files, number_folders



if __name__ == "__main__":
    f = [ "vinaya", "sutta", "abhidhamma"]
    sourcefolder = "../tripitaka/pli/ms/"
    print(f'\nParse the 3 folders {f} in {sourcefolder}')
    for folder in f:
        number_files, number_folders = investigate(sourcefolder, folder)
        print(f"Folder {folder} contains {number_files} files in {number_folders} folders.")




                # print(os.path.join(root, filename))       
            # print(root, " - ", dirs, " - ", filename)
