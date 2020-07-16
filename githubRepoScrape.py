import requests
import sys
import re

res = open("projectLinksScraped.txt", "w")

def individualProject(argument):
    reg = "<a target=\"_blank\".*href=\"(.*?)\""
    project = requests.get(str(argument.strip())).text
    links = re.findall(reg, str(project))
    for i in range(len(links)):
        res.write(links[i]+'\n')

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
    hackathonNum = 0
    for line in f.readlines():
        hackathonNum += 1
        print("New URL #" + str(hackathonNum) + ": " + str(line.strip()))
        index = 2
        scrapeProjectLinks(line)
        nextPage = str(line.strip()+"?page="+str(index))
        print("Next URL: " + nextPage)
        reg1 = "(There are no submissions which match your criteria.)"
        reg2 = "(The hackathon managers haven't published this gallery yet, but hang tight!)"
        while(re.search(reg1, requests.get(nextPage).text) is None and re.search(reg2, requests.get(nextPage).text) is None):
            print("Success " + str(index) + ": " + nextPage)
            scrapeProjectLinks(nextPage)
            index += 1
            nextPage = str(line.strip()+"?page="+str(index))

    
driverFunction()
res.close()