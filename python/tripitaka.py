# Examine the pali tripitaka text in JSON format

import os, sys, json, nltk

# Check execution location, exit if not in /python
if os.getcwd()[-6:] != "python":
    print("This script must be executed inside the /python folder.")
    exit()

jsonlist = []
output = ""
number_pages = 1
current_line = 0
current_column = 0
list_books = []

def import_jsonfiles_list(sourcefolder):
    global jsonlist
    if sourcefolder[-1] != "/":
        sourcefolder += "/"
    jsonlistfile = sourcefolder + "Books.json"
    print(f"Import the data listed in {jsonlistfile}: ", end="")
    if not os.path.isfile(jsonlistfile):
        print("This file does not exist.")
        return
    f = open(jsonlistfile)
    list_jsonfiles = json.load(f)
    nr_jsonfiles = 0
    for jsonfile in list_jsonfiles:
        # print(sourcefolder + book)
        nr_jsonfiles += 1
        jsonlist.append(sourcefolder + jsonfile + ".json")
    print(f"Found {nr_jsonfiles} json files")

def extend_print(bookname, nr_chapter, nr_verse, text_verse):
    global output, current_line, current_column
    if nr_verse == '1':
        remaining_txt = f"|{nr_chapter}| " + text_verse + " "
    else:
        remaining_txt = f"{nr_verse} " + text_verse + " "
    while len(remaining_txt) > 0:
        if current_column + len(remaining_txt) < 79:
            output += remaining_txt
            current_column += len(remaining_txt)
            remaining_txt = ""
        else:
            max_length = 79 - current_column
            max_string = remaining_txt[:max_length]
            # find rightmost space in this string
            last_space = max_string.rfind(' ')
            if last_space > 0:
                output += remaining_txt[:last_space]
                remaining_txt = remaining_txt[last_space+1:]
            output += "\n"
            current_line += 1
            current_column = 0
        if current_line > 49:
            add_pagebreak()
            output += f"{bookname} {nr_chapter}:{nr_verse} \n\n"

def add_pagebreak():
    global output, current_line, number_pages
    if current_line < 49:
        for i in range(49 - current_line):
            output += "\n"
    output += "\n"
    output += f"                                       {number_pages}\n"
    output += "\n"
    output += "---\n"
    output += "\n"
    current_line = -2
    number_pages += 1

def decrypt(key):
    # determine internal name for book, chapter and verse - but sometimes chapter is missing!
    colon = key.find(":")
    substring = key[colon+1:]
    dot = substring.find(".")
    internal_verse = substring[:dot]
    substring = key[:colon]
    dot = substring.find(".")
    if dot == -1:   # there is no dot - no chapter!
        internal_bookname = substring
        internal_chapter = "1"
    else:
        internal_bookname = substring[:dot]
        internal_chapter = substring[dot+1:]
    return internal_bookname, internal_chapter, internal_verse


def parse_list():
    global output, current_line, current_column
    number_json       = 0
    number_books      = 0
    number_chapters   = 0
    number_verses     = 0
    number_sentences  = 0
    number_words      = 0
    number_letters    = 0
    current_book      = ""
    current_chapter   = ""
    current_verse     = "1"
    current_page      = 0
    verseline       = ""
    fix_html_b      = 0
    for jsonname in jsonlist: # here referring to each json file of the 7288
        f = open(jsonname)
        jsonfile = json.load(f)
        number_json += 1
        # print(f"json: {jsonname}  - book: {current_book} {current_chapter}:{current_verse}")
        for key in jsonfile: # the key is the indication of book, chapter, verse
            textline = jsonfile[key]
            if textline.find("<b>") > 0:
                b = textline.find("<b>")
                textline = textline[:b] + textline[b+3:]
                b = textline.find("</b>")
                textline = textline[:b] + textline[b+4:]
                fix_html_b += 1
                # print(textline)
            key_book, key_chapter, key_verse = decrypt(key)
            if current_book != key_book:
                if len(verseline) > 0:
                    extend_print(current_book, current_chapter, current_verse, verseline)
                    output += "\n\n"
                    current_line += 2
                verseline = ""
                current_book = key_book
                current_chapter = key_chapter
                current_verse = key_verse
                if not current_book in list_books:
                    number_books += 1
                    list_books.append(current_book)
                    output += current_book + "\n\n"
                    current_line += 2
                    # print(f"New book: {key_book} on page {current_page}")
            if current_chapter != key_chapter:
                number_chapters += 1
                extend_print(current_book, current_chapter, current_verse, verseline)
                verseline = ""
                current_chapter = key_chapter
                current_verse = key_verse
                # print(".", end="")
            if current_verse != key_verse:
                number_verses += 1
                extend_print(current_book, current_chapter, current_verse, verseline)
                # print("old: ", current_book, current_chapter, current_verse, verseline, " - new: ", key, key_book, key_chapter, key_verse, )
                current_verse = key_verse
                verseline = ""
            verseline += textline
            # print(f"{key}  - book: {internal_bookname} {internal_chapter}:{internal_verse}")
            # extend_print(current_book, current_chapter, current_verse, textline)
            sentences = nltk.sent_tokenize(textline)
            for sentence in sentences:
                number_sentences += 1
                sentence = sentence.replace('’','')
                wordlist = nltk.word_tokenize(sentence)
                for word in wordlist:
                    if word != "." and word != "," and word != ":" and word != ";" and word != "’" and word != "?":
                        number_words += 1
                        number_letters += len(word)
                        # print(word, end="_")
            # Check for change in page numbers
            if number_pages > current_page:
                current_page = number_pages
                if current_page % 100 == 0:
                    print(f"pages: {number_pages} json-nr: {number_json}", end=" ")
                    print(f"location: {current_book} {current_chapter}:{current_verse}", end=" ")
                    print(f"books: {number_books} chapters:{number_chapters} verses: {number_verses}", end=" ")
                    print(f"words: {number_words} characters: {number_letters} length:{len(output)}")
        f.close()
        # output += "\n\n\n"   # remnant from the bible - each json represents a book. Not so tripitaka
        current_column = 0
    print(f"Parsed: {number_books} books.")
    print(f"Parsed: {number_chapters} chapters.")
    print(f"Parsed: {number_verses} verses.")
    print(f"Parded: {number_sentences} sentences.")
    print(f"Parsed: {number_words} words.")
    print(f"Parsed: {number_letters} letters or characters.")
    print(f"Parsed: {number_pages} pages 80x50.")
    print(f"Fixed {fix_html_b} html tags <b> and </b>")

if __name__ == "__main__":
    # if len(sys.argv) < 2:
    #     print("You did not provide a path to a folder with a Books.json in it as argument. Put it as a parameter after examine.py")
    #     exit()
    # sourcefolder = sys.argv[1]
    sourcefolder = "../tripitaka/pli/ms"
    import_jsonfiles_list(sourcefolder)
    if len(jsonlist) > 0:
        parse_list()
    with open("tripitaka.txt", "w") as text_file:
        text_file.write(output)
    print(f"Exported tripitata.txt with {len(output)} characters.")
    # print(list_books)
