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
# tree = ET.parse(f"{list(result.keys())[0]}/{list(result.values())[0][0]}")
namespaces = { 'dtb': 'http://www.daisy.org/z3986/2005/dtbook-2005-3.dtd' }
for folder, files in result.items():
    book = folder.replace("\\","/").split("/")[-1]
    print(f"Processing {book}")

    # Initialize the JSON structure
    book_json = {}
    book_json["book"] = book
    book_json["chapters"] = []

    for file in files:
        print(f"Parsing {folder}/{file}")
        # Parse the XML file
        tree = ET.parse(f"{folder}/{file}")
        root = tree.getroot()
        
        # Extract the book name and chapter number from the file name
        chapter = file.replace(".xml", "").split("_")
        chapter_json = {}
        chapter_json["chapter"] = chapter[-1]
        chapter_json["verses"] = []
        
        # Extract the verses from the XML file
        for verse_element in root.findall(".//dtb:span[@class='sentence']", namespaces):
            verse_number = verse_element.attrib["id"]   # get rid of the leading p prefix
            verse_text = verse_element.text        # get the leading vers number                  
            
            # Initialize the verse JSON structure
            verse_json = {}
            verse_json["verse"] = verse_number
            verse_json["text"] = verse_text

            # Append the verse to the chapter JSON structure
            chapter_json["verses"].append(verse_json)
        
        # Append the chapter to the book JSON structure
        book_json["chapters"].append(chapter_json)
        
        # Export the JSON structure to a file
        book_string = json.dumps(book_json, ensure_ascii=False, indent=4)
        output_file_path = os.path.join(export_dictionary, f"{book}.json")
        with open(output_file_path, "w", encoding="utf-8") as file:
            file.write(book_string)

# Display the results
# for folder, files in result.items():
#     print(f"Folder: {folder}")
#     chapter_count = len(files)
#     print(f"Number of XML files: {chapter_count}")  
    # for file in files:
    #     print(f"  - {file}")

print(f"Total number of folders: {len(result)} with total {sum([len(files) for files in result.values()])} XML files")

print(f"Lets parse one XML example from {import_dictionary} with the first folder and first file")

from lxml import etree

# Step 1: Parse the XML file
xml_file = "./nwt_xml/Genesis/0001.xml"  # Replace with your file path
tree = etree.parse(xml_file)
root = tree.getroot()

# Step 2: Define the namespace if the XML uses one
namespaces = {
    'dtb': 'http://www.daisy.org/z3986/2005/dtbook/'  # Adjust this URL based on the namespace in your file
}

# Step 3: Find the <p1> element and get its 'id' attribute
p1_element = root.find(".//dtb:p1", namespaces)
if p1_element is not None and 'id' in p1_element.attrib:
    p1_id = p1_element.attrib['id']
    print(f"p1 id: {p1_id}")
else:
    print("No <p1> element with an 'id' attribute found.")

# Step 4: Find all <span> elements with class="sentence"
span_elements = root.findall(".//dtb:span[@class='sentence']", namespaces)

# Step 5: Print the spans' content
# print("Spans with class='sentence':")
# for span in span_elements:
#     print(span.text)


'''
import xml.etree.ElementTree as ET
tree = ET.parse(f"{list(result.keys())[0]}/{list(result.values())[0][0]}")
root = tree.getroot()
print(f"Root tag: {root.tag}")
print(f"Root attrib: {root.attrib}")
print(f"Root text: {root.text}")
'''

'''
# Export to JSON

book_json = {}
book_json["book"] = "Genesis"
book_json["chapters"] = []      # Initialize an empty list - can be taken from the XML file name
book_json["chapters"].append({
    "chapter": "1",
    "verses": []
})
book_json["chapters"][0]["verses"].append({
    "verse": "1",
    "text": "In the beginning God created the heaven and the earth."
})

book_string = json.dumps(book_json, ensure_ascii=False, indent=4)

output_file_path = os.path.join(export_dictionary, "Genesis.json")
with open(output_file_path, "w", encoding="utf-8") as file:
    file.write(book_string)
'''
