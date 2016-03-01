#!/usr/bin/python

import urllib.request
from urllib.request import urlopen 
from lxml import etree
from lxml import html


def crawl():
    '''Crawls given webpages, saves to disk and searches them. Recommended use with WikiPedia.'''
    seedOne = input("Please enter  the first seed URL: \n")
    print("You entered: \n" + seedOne)
    seedTwo= input("\nPlease enter the second seed URL: \n")
    print("You entered:\n " +  seedTwo)
    keywords=input("\nPlease enter keywords related to your link: ")
    print('\nPlease sit tight while I process your request......')
    dictionary = keywords.lower()
    htmlOne  = urlopen(seedOne).read()
    htmlTwo = urlopen(seedTwo).read()
    treeOne = etree.fromstring(htmlOne) # Parse the HTML
    treeTwo = etree.fromstring(htmlTwo)
    linkList=[]
    with urllib.request.urlopen(seedOne) as response:
        seedOnehtml = response.read()
        for x in seedOnehtml:
            holdOneTree = treeOne.iterfind(".//a")
    with urllib.request.urlopen(seedTwo) as response:
        seedTwohtml = response.read()
        for x in seedTwohtml:
            holdTwoTree = treeTwo.iterfind(".//a")
        sourceCombo = seedOnehtml + seedTwohtml
        for i, line in enumerate(sourceCombo):
            with open("1_%i.html" %i, "a+") as f: #writing to multiple files that are cre*typedated instantly with this naming scheme .
                f.write((repr(sourceCombo)))
                if i >= 500: #Stops generating  files at this number.
                    break
                for x in holdOneTree:
                    linkList.append(seedOne)
                    linkList.append((x.get("href")))
                    break
                for x in holdTwoTree:
                    linkList.append(seedTwo)
                    linkList.append((x.get("href")))
                    break
                for i, line in enumerate(linkList):
                    with open("linkList.txt", "a+") as Fin:
                        Fin.write((repr(str(linkList))))
                        if i >= 1: #Stops creating files at this number.
                            break
                        with open('linkList.txt', 'r') as Fin:
                            for line in Fin:
                                if line in dictionary:
                                    dictionary + line
                                    print(dictionary)
                       


print(crawl())


