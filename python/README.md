# Parse JSON files of KJV and Tripitaka

## King James Version

The parsing works on a Book basis. In the respective folder of the translation you want to investigate you need a file `Books.json` that lists all the different books that are combined into your library, as is the case with the 66 books of the bible.

For each of the individual books you need a matching `.json` file that contains the chapters and verses. Then the script can read all the content, compile it on pages with 80x50 characters of a new `kjv.txt` and export some statistics. 

In our case you can start it with

``` sh
(venv) user@server:~$ python examine.py ../bible/kjv
```

After a few seconds you should see the result:

``` sh
Import the books listed in ../bible/kjv/Books.json: Found 66 books
Number pages: 100
Number pages: 200
Number pages: 300
Number pages: 400
Number pages: 500
Number pages: 600
Number pages: 700
Number pages: 800
Number pages: 900
Number pages: 1000
Parsed: 66 Books.
Parsed: 1189 Chapters.
Parsed: 31102 Verses.
Parded: 35049 Sentences.
Parsed: 790573 Words.
Parsed: 3223201 Letters.
Parsed: 1062 Pages 80x50.
```

## Tripitaka
