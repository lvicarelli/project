import urllib
import re
"""Will open a page, remove all non character signs and count how many times the word 'CAT' was used in the source code of the page. It can print the the positions of the word 'CAT' on the page.
"""

def lettersOnPage(URL):
    #counting letters on a given URL
    allDataPage = urllib.request.urlopen(URL)
    word_count = 0;
    for line in allDataPage:
        for item in line:
            if chr(item).isalpha():
                #print(chr(item))
                word_count += 1            
    print(word_count)
    
#look for a word cat
def countCats(URL):
    allLetters = []
    allDataPage2 = urllib.request.urlopen(URL)
    for line in allDataPage2:
        for item in line:
            if chr(item).isalpha():
                allLetters.append(chr(item))

    allLetters = ''.join(allLetters)
    allLetters = allLetters.lower()
    allLetters = str.replace(allLetters,'cat',' CAT ')
    
    Cats =  re.findall('CAT', allLetters)
    print('A word *CAT* was used ' + str(len(Cats)) + ' times on the page')
    #print(allLetters)   
    
CatWiki = 'https://en.wikipedia.org/wiki/Cat'
countCats(CatWiki)