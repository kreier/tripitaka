import os
import json
import xml.etree.ElementTree as ET

# Set the path to the base directory
import_dictionary = "./nwt_xml"  
export_dictionary = "./nwt"

def list_xml_files(base_dir):
    xml_files = {}
    
    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(base_dir):
        # Filter for XML files
        xml_files_in_dir = [file for file in files if file.endswith('.xml')]
        
        # If there are XML files in the current folder, store them
        if xml_files_in_dir:
            xml_files[root] = xml_files_in_dir
    
    return xml_files

# Get the list of XML files to be converted to JSON
result = list_xml_files(import_dictionary)

# Parsing the XML files
namespace = { 'dtb': 'http://www.daisy.org/z3986/2005/dtbook/' }

for folder, files in result.items():
    book = folder.replace("\\","/").split("/")[-1]
    print(f"Processing {book} ", end="")

    # Initialize the JSON structure
    book_json = {}
    book_json["book"] = book
    book_json["chapters"] = []

    number_chapters = 0
    number_verses = 0

    for file in files:                      # chapters are in separate files in XML, but combined in JSON for one file per book
        # print(f"Parsing {folder}/{file}")
        # Parse the XML file
        tree = ET.parse(f"{folder}/{file}")
        root = tree.getroot()
        
        # Extract the book name and chapter number from the file name
        chapter = file.replace(".xml", "").split("_")
        chapter_json = {}
        chapter_json["chapter"] = chapter[-1].lstrip("0")  # remove leading zeros
        chapter_json["verses"] = []
        
        double_nbsp = "\u00A0\u00A0"  # Two consecutive non-breaking spaces
        # Extract the verses from the XML file
        for verse_element in root.findall('.//dtb:span[@class="sentence"]', namespaces=namespace):
            verse_text = verse_element.text
            if double_nbsp in verse_text:
                len_verse_number = verse_text.find(double_nbsp)
                verse_number = verse_text[:len_verse_number]
                verse_text = verse_text[len_verse_number+2:]
            else:
                verse_number = "1"   
            
            # Initialize the verse JSON structure
            verse_json = {}
            verse_json["verse"] = verse_number
            verse_json["text"] = verse_text

            # Append the verse to the chapter JSON structure
            chapter_json["verses"].append(verse_json)
            number_verses += 1
        
        # Append the chapter to the book JSON structure
        book_json["chapters"].append(chapter_json)
        number_chapters += 1
        
    # Export the JSON structure to a file
    book_string = json.dumps(book_json, ensure_ascii=False, indent=4)
    output_file_path = os.path.join(export_dictionary, f"{book}.json")
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(book_string)
    print(f"with {number_chapters} chapters and {number_verses} verses")

print(f"Parsed {len(result)} folders/books with {sum([len(files) for files in result.values()])} XML files/chapters.")
