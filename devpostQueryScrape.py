# Author: Lukas McIntosh
# Program: A python script used to search devpost with string provided from hackathon.txt and then web scrapes hackathon 
#          project page url into text doc 'hackathonProjectURL'
# Purpose: to perform research on developement phase longevity of hackathons in the U.S (in 2018 and 2019)
# Date: 5/20/20
#   URL: https://devpost.com/hackathons?utf8=%E2%9C%93&search=INSERTSEARCHHERE&challenge_type=all&sort_by=Recently+Added
#
#   Sanitize the input (elements of the list from hackathonNamess.txt) and inject into INSERTSEARCHHERE
#       -write conditional to check date posted? 
#       -start scraping github links
#
#   Notes on formatting:
#       - special characters: / @ : ; ? ! # $ % ^ & ( ) + = , / ' \ | { } [ ]
#       - Translation table:
#               .   /  =  '%2F'
#               .   ?  =  '%3F'
#               .   @  =  '%40'
#               .   !  =  '%21'
#               .   #  =  '%23'
#               .   $  =  '%24'
#               .   %  =  '%25'
#               .   ^  =  '%5E'
#               .   &  =  '%26'
#               .   (  =  '%28'
#               .   )  =  '%29'
#               .   +  =  '%2B'
#               .   =  =  '%3D'
#               .   ,  =  '%2C'            
#               .   '  =  '%27'
#               .   \  =  '%5C'
#               .   |  =  '%7C'
#               .   {  =  '%7B'
#               .   }  =  '%7D'
#               .   [  =  '%5B'
#               .   ]  =  '%5D'
#
#       -  Notes on whitespaces: 
#               .   when there are multiple spaces, another + sign is added
#               .   Ex1) input:  "Hack The Six" --> desired output: "Hack+The+Six"
#               .   Ex2) input:  "Hack  The  Six" --> output: "Hack++The++Six"
#               ** Only performs + when encounters two spaces directly in a row
#               .   Ex3) input:  "Hack , The , Six" --> output: "Hack+%2C+The+%2C+Six"
#               .   
import requests
import sys
import re
from bs4 import BeautifulSoup

#   URL: https://devpost.com/hackathons?utf8=%E2%9C%93&search=INSERTSEARCHHERE&challenge_type=all&sort_by=Recently+Added
#
#   Sanitize the input (elements of the list from hackathonNamess.txt) and inject into INSERTSEARCHHERE
#       -write conditional to check date posted? 
#       -start scraping github links
#   USE THE ABOVE TABLE TO TRANSLATE THE NAMES IN HACKATHON.TXT AND INSERT INTO URLS

def translateToURLFormat():
    f.open("devpostURLS.txt", "w")
    with open("hackathonNames.txt", "r") as tmp:
        for line in tmp:
            temp = line.strip()
            #print("OGString: " + temp + ",   returned string: " + processName(temp))

            line = tmp.readline()

def processName(argument):
    for crctr in argument:
        temp = isInvalidChar(crctr)
        #print("current character --> " + crctr)
        if temp != 'isValidChar':
            argument = argument.replace(crctr, temp)
            #print("arg with values replaced = " +argument.replace(crctr, temp))  
            #print("New character --> " + temp)
    return argument
          

def isInvalidChar(argument):
    switcher = {
        '/'  : '%2F',
        '?'  :  '%3F',
        '@'  :  '%40',
        '!'  :  '%21',
        '#'  :  '%23',
        '$'  :  '%24',
        '%'  :  '%25',
        '^'  :  '%5E',
        '&'  :  '%26',
        '('  :  '%28',
        ')'  :  '%29',
        '+'  :  '%2B',
        '='  :  '%3D',
        ','  :  '%2C',  
        '\'' :  '%27',
        '\''  :  '%5C',
        '|'  :  '%7C',
        '{'  :  '%7B',
        '}'  :  '%7D',
        '['  :  '%5B',
        ']'  :  '%5D',
        ' '  :  '+'
    }
    result = switcher.get(argument, 'isValidChar')
    return result

translateToURLFormat()
