#!/usr/bin/python

from urllib.request import urlopen 
from lxml import etree
from lxml import html


def crawl():
    '''Crawls given webpages searching for keywords. If keywords are found
in the webpage, it will write to disk. Recommended use with Wikipedia.'''
    seedOne = input("Please enter  the first seed URL: \n")
    print("You entered: \n" + seedOne)
    seedTwo= input("\nPlease enter the second seed URL: \n")
    print("You entered:\n " +  seedTwo)
    keywords=input("\nPlease enter keywords related to your link: ")
    print('\nPlease sit tight, this will take a while to process......')
    dictionary = keywords.split()
    htmlOne  = urlopen(seedOne).read()
    htmlTwo = urlopen(seedTwo).read()
    treeOne = etree.fromstring(htmlOne) # Parse the HTML
    treeTwo = etree.fromstring(htmlTwo)
    seedList=[]
    for x in treeOne.iterfind(".//a"):
        seedList.append(seedOne)
        seedList.append((x.get("href")))
        for x in treeTwo.iterfind(".//a"):
            seedList.append(seedTwo)
            seedList.append((x.get("href")))
            filew = open("1.html", "a+")
            for i, line in enumerate(seedList):
                with open("1_%i.html" %i, "a+") as f: #writing to multiple files that are created instantly with this naming scheme . 
                    f.write((repr(seedList )))
                    if i >= 500: #Stops creating files at this number.
                        break
                    for word in f:
                        if word in keywords:
                            dictionary.append(word)
                            
                                                 
            
print(crawl())
 

