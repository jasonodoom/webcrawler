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
    dictionary = keywords.split()
    htmlOne  = urlopen(seedOne).read()
    htmlTwo = urlopen(seedTwo).read()
    #limitOne= htmlOne.read(5000) #Close the connection after 5000 bytes
    #limitTwo=htmlTwo.read(5000)
    #limitOne.close()
    #limitTwo.close()

    treeOne = etree.fromstring(htmlOne) # Parse the HTML
    treeTwo = etree.fromstring(htmlTwo)
    seedList=[]
    for x in treeOne.iterfind(".//a"):
        seedList.append(seedOne)
        seedList.append((x.get("href")))
        for x in treeTwo.iterfind(".//a"):
            seedList.append(seedTwo)
            seedList.append((x.get("href")))
            #print(seedList)
            for word in keywords:
                if word in seedList:
                    with open("1.html", "w+") as f:
                        f.write(word)
                        print(word)
                        
                        
                            
            
print(crawl())
 

