import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('.\\nwt_xml\\Genesis\\0001.xml')
root = tree.getroot()

# Define a recursive function to print the XML tree
def print_tree(element, level=0):
    indent = "  " * level
    print(f"{indent}<{element.tag}>: {element.text.strip() if element.text else ''}")
    for child in element:
        print_tree(child, level + 1)
    print(f"{indent}</{element.tag}>")

# Print the entire tree starting from the root
# print_tree(root)

# Define the namespace mapping (adjust if your file uses different prefixes)
namespaces = {'dtb': 'http://www.daisy.org/z3986/2005/dtbook/'}

# Locate the 'doctitle' element via its hierarchy
doctitle = root.find('.//dtb:doctitle', namespaces)

# Print the content of the 'doctitle' element if found
if doctitle is not None:
    print("Doctitle content:", doctitle.text)
else:
    print("No doctitle element found.")




# Define the sequence to search for
target_sequence = "\u00A0\u00A0"  # Two consecutive non-breaking spaces

# Function to find the sequence in XML
def find_double_nbsp(element):
    for subelement in element.iter():
        if subelement.text and target_sequence in subelement.text:
            # print(f"Found in <{subelement.tag}>: {subelement.text}")
            print(f"I found the sequence at position {subelement.text.find(target_sequence)}")

# Search for the sequence in the XML file
find_double_nbsp(root)




''' old code for showing the unicode sequence 
# Function to examine special Unicode characters
def examine_unicode(element):
    for subelement in element.iter():
        if subelement.text:  # Check if the element has text content
            print(f"Text in <{subelement.tag}>: {subelement.text}")
            for char in subelement.text:
                # Print the character and its Unicode code point
                print(f"Character: '{char}' -> Unicode: U+{ord(char):04X}")

# Examine the XML document
examine_unicode(root)

'''