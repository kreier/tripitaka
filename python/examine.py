# Examine a given text in JSON format for a defined search criteria

import os, sys, json

# Check execution location, exit if not in /timeline/python
if os.getcwd()[-6:] != "python":
    print("This script must be executed inside the python folder.")
    exit()

booklist = []

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
        print(sourcefolder + book)
        nr_books += 1
        booklist.append(sourcefolder + book + ".json")
    print(f"Found {nr_books} books")
    # booklist = ["../bible/kjv/Genesis.json"]

def parse_list():
    global booklist
    number_books      = 0
    number_chapters   = 0
    number_verses     = 0
    number_words      = 0
    number_letters    = 0
    number_pages      = 0
    for book in booklist:
        f = open(book)
        book = json.load(f)
        number_books += 1
        for chapter in book['chapters']:
            number_chapters += 1
            for verse in chapter['verses']:
                number_verses += 1
                print(verse['text'])
        f.close()
    print(f"Parsed: {number_books} Books.")
    print(f"Parsed: {number_chapters} Chapters.")
    print(f"Parsed: {number_verses} Verses.")
    print(f"Parsed: {number_words} Words.")
    print(f"Parsed: {number_letters} Letters.")
    print(f"Parsed: {number_pages} Pages 40x25.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("You did not provide a path to a folder with a Books.json in it as argument. Put it as a parameter after examine.py")
        exit()
    sourcefolder = sys.argv[1]
    import_booklist(sourcefolder)
    if len(booklist) > 0:
        parse_list()
