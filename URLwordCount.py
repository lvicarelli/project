  def countWords(URL):
    # "http://www.sandia.gov/~sjplimp/docs/txt2html/example.txt"
    # call it wiet 'countWords( your URL )
    
    def importPage(URL):
        from urllib.request import urlopen
        textfile = urlopen(URL).read()
        page = ''
        for line in textfile:
            page += (chr(line))
        return page

    def wordCounter(page):
        counterWords = 0
        for eachWord in (page.split()):
            if eachWord.isalpha() or not eachWord.isdigit():
                counterWords += 1
        print("This document has " + str(counterWords) + " words")
        return counterWords
    
    importPage(URL)
    wordCounter(page)