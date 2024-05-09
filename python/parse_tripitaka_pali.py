# Parse the /tripitaka/pli/ms/ folders for JSON files, create a Books.json

import os, json, csv

# Check execution location, exit if not in /python
if os.getcwd()[-6:] != "python":
    print("This script must be executed inside the /python folder.")
    exit()

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
    list_output.sort()
    # print(list_output)
    filename = source + folder + '.csv'
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header_list)
        writer.writerows(list_output)
    print(f"Wrote {source}{folder}.csv")
    return number_files, number_folders

def convert_csv_to_json(pitakas):
    global sourcefolder
    jsonlist = []
    for pitaka in pitakas:
        csvfile = sourcefolder + pitaka + ".csv"
        with open(csvfile) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[0] != "path":
                    jsonfile = row[0] + "/" + row[1]
                    jsonlist.append(jsonfile)
    jsonfilelist = sourcefolder + "Books.json"
    with open(jsonfilelist, "w", encoding="utf-8", newline='\r\n') as final:
        json.dump(jsonlist, final, indent=0)
    print(f"Exported list of {len(jsonlist)} json source files to {jsonfilelist}.")

if __name__ == "__main__":
    # f = ["vinaya", "sutta", "abhidhamma"]
    f = ["vinaya"]
    sourcefolder = "../tripitaka/pli/ms/"
    print(f'\nParse the 3 folders {f} in {sourcefolder}')
    for folder in f:
        number_files, number_folders = investigate(sourcefolder, folder)
        print(f"Folder {folder} contains {number_files} files in {number_folders} folders.")
    convert_csv_to_json(f)
