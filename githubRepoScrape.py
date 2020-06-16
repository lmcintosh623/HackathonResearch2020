import requests
import sys
import re

res = open("projectLinksScraped.txt", "w")

def individualProject(argument):
    reg = "<a target=\"_blank\".*href=\"(.*?)\""
    project = requests.get(str(argument.strip())).text
    links = re.findall(reg, str(project))
    for i in range(len(links)):
        res.write(links[i])

def scrapeProjectLinks(argument):
    reg = "<a class=\"block-wrapper-link fade link-to-software\" href=\"(.*?)\">"
    hackathon = requests.get(str(argument.strip())).text
    results = re.findall(reg, str(hackathon))
    #print(results)
    for i in range(len(results)):
        print("Iteration " + str(i))
        individualProject(results[i])



def driverFunction():
    f = open("listOfValidHackathonURLs.txt", "r") 
    for line in f.readlines():
        scrapeProjectLinks(line)
    f.close()
    
driverFunction()
res.close()