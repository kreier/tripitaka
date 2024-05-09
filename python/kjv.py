# Examine the kjv text in JSON format for a defined search criteria

import os, sys, json, nltk, csv

# Check execution location, exit if not in /python
if os.getcwd()[-6:] != "python":
    print("This script must be executed inside the /python folder.")
    exit()

booklist = []
output = ""
number_pages   = 1
current_line   = 0
current_column = 0
content_detail = [["book", "chapters", "verses", "sentences", "words", "letters", "pages"]]

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

def extend_print(bookname, nr_chapter, nr_verse, text_verse):
    global output, current_line, current_column
    pagebreak = False
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
            output += bookname + " " + nr_chapter + "\n\n"
            pagebreak = True
    return pagebreak

def add_pagebreak():
    global number_pages, output, current_line
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

def parse_list():
    global booklist, number_pages, output, current_column
    number_books      = 0
    number_chapters   = 0
    number_verses     = 0
    number_sentences  = 0
    number_words      = 0
    number_letters    = 0
    current_chapters  = 0
    current_verses    = 0
    current_sentences = 0
    current_words     = 0
    current_letters   = 0
    current_pages     = 1
    # output += "\n"*25
    # output += "                      Project 'examine large textbodies'\n"
    # add_pagebreak()
    for book in booklist:
        f = open(book)
        book = json.load(f)
        book_name = book['book']
        output += book_name + "\n\n"
        number_books += 1
        for chapter in book['chapters']:
            number_chapters += 1
            nr_chapter = chapter['chapter']
            for verse in chapter['verses']:
                number_verses += 1
                nr_verse = verse['verse']
                pb = extend_print(book_name, nr_chapter, nr_verse, verse['text'])
                if number_pages % 100 == 0 and pb:
                    print(f"pages: {number_pages} chapters: {number_chapters} verses: {number_verses} words: {number_words}")
                sentences = nltk.sent_tokenize(verse['text'])
                for sentence in sentences:
                    number_sentences += 1
                    sentence = sentence.replace('’','')
                    wordlist = nltk.word_tokenize(sentence)
                    for word in wordlist:
                        if word != "." and word != "," and word != ":" and word != ";" and word != "’" and word != "?":
                            number_words += 1
                            number_letters += len(word)
                            # print(word, end="_")
        f.close()
        output += "\n\n\n"
        current_column = 0
        current_chapters   = number_chapters  - current_chapters
        current_verses     = number_verses    - current_verses
        current_sentences  = number_sentences - current_sentences
        current_words      = number_words     - current_words
        current_letters    = number_letters   - current_letters
        current_pages      = number_pages     - current_pages
        content_detail.append([book_name, current_chapters, current_verses, current_sentences, current_words, current_letters, current_pages])
        current_chapters   = number_chapters
        current_verses     = number_verses
        current_sentences  = number_sentences
        current_words      = number_words
        current_letters    = number_letters
        current_pages      = number_pages

    print(f"Parsed: {number_books} Books.")
    print(f"Parsed: {number_chapters} Chapters.")
    print(f"Parsed: {number_verses} Verses.")
    print(f"Parded: {number_sentences} Sentences.")
    print(f"Parsed: {number_words} Words.")
    print(f"Parsed: {number_letters} Letters.")
    print(f"Parsed: {number_pages} Pages 80x50.")

if __name__ == "__main__":
    # if len(sys.argv) < 2:
    #     print("You did not provide a path to a folder with a Books.json in it as argument. Put it as a parameter after examine.py")
    #     exit()
    # sourcefolder = sys.argv[1]
    sourcefolder = "../bible/kjv"
    import_booklist(sourcefolder)
    if len(booklist) > 0:
        parse_list()
    with open("kjv.txt", "w") as text_file:
        text_file.write(output)
    # print(content_detail)
    with open("kjv_details.csv", "w", newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(content_detail)
