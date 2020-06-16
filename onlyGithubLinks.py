import requests
import sys
import re
from bs4 import BeautifulSoup

fr = open("githubURLsWorkplace.txt", "r")
fw = open("GithubLinksScraped.txt", "w")
reg = "(https?://github.*$)"

for line in fr.readlines(): 
    if "/github.com" in line:
        fw.write(str(line))

fr.close()
fw.close()