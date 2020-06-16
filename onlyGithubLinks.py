import requests
import sys
import re
from bs4 import BeautifulSoup

fr = open("totalLinksScraped.txt", "r")
fw = open("GithubLinksScraped.txt", "w")

for line in fr.readlines(): 
    if "/github.com" in line:
        fw.write(str(line).split()[0] + "/commits/master\n")

fr.close()
fw.close()