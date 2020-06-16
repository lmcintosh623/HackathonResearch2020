import requests
import sys
import re
from bs4 import BeautifulSoup

fr = open("totalLinksScraped.txt", "r")
fw = open("GithubLinksScraped.txt", "w")
reg = "(https://github.com.*)"
currList = fr.readlines()
fr.close()

projectLinks = re.findall(reg, str(currList))
for i in range(len(projectLinks)):
    fw.write(str(projectLinks[i]))

fw.close()