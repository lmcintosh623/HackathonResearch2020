from datetime import date
import requests
import re
from bs4 import BeautifulSoup

def monthDict(argument):
    switcher = {
            'Jan' : 1,
            'Feb' : 2,
            'Mar' : 3, 
            'Apr' : 4,
            'May' : 5,
            'Jun' : 6,
            'Jul' : 7,
            'Aug' : 8,
            'Sep' : 9,
            'Oct' : 10,
            'Nov' : 11,
            'Dec' : 12
        }
    return switcher.get(argument, "Invalid Month")

githubLinks = open("GithubLinksScraped.txt", "r")
dateDifferenceData = []

fullList = githubLinks.read().split()
for i in range(len(fullList)):
    print("Iteration " + str(i) + " " + fullList[i])
    commitPage = requests.get(fullList[i]).text
    commitList = []
    pageSoup = BeautifulSoup(commitPage, 'html.parser')
    for div in pageSoup.findAll('div' , {'class':'commit-group-title'}):
        commitList.append(div.text.strip()[11:23])
    if(len(commitList) >= 2):
        if(len(commitList[0]) == 12):
            #print("case 1")
            month1 = monthDict(str(commitList[0])[0:3])
            if(month1 == "Invalid Month"):
                print("Invalid month, breaking from program")
                break
            day1 = str(commitList[0])[4:6]
            year1 = str(commitList[0])[8:12]
            if(len(commitList[1]) == 12):
                month2 = monthDict(str(commitList[1])[0:3])
                if(month2 == "Invalid Month"):
                    print("Invalid month, breaking from program")
                    break
                day2 = str(commitList[1])[4:6]
                year2 = str(commitList[1])[8:12]
            else:
                month2 = monthDict(str(commitList[1])[0:3])
                if(month2 == "Invalid Month"):
                    print("Invalid month, breaking from program")
                    break
                day2 = str(commitList[1])[4:5]
                year2 = str(commitList[1])[7:11]
            #print("First date: " + str(month1) + "/" + str(day1) + "/" + str(year1))
            date1 = date(int(year1),int(month1),int(day1))
            date2 = date(int(year2),int(month2),int(day2))
            difference = date1 - date2
            dateDifferenceData.append(difference.days)
            #print("Difference in number of days: " + str(difference.days))

        else:
            print("case 2")
            month1 = monthDict(str(commitList[0])[0:3])
            if(month1 == "Invalid Month"):
                print("Invalid month, breaking from program")
                break
            day1 = str(commitList[0])[4:5]
            year1 = str(commitList[0])[7:11]
            #print("First date: " + str(month1) + "/" + str(day1) + "/" + str(year1))
            if(len(commitList[1]) == 12):
                month2 = monthDict(str(commitList[1])[0:3])
                if(month2 == "Invalid Month"):
                    print("Invalid month, breaking from program")
                    break
                day2 = str(commitList[1])[4:6]
                year2 = str(commitList[1])[8:12]
            else:
                month2 = monthDict(str(commitList[1])[0:3])
                if(month2 == "Invalid Month"):
                    print("Invalid month, breaking from program")
                    break
                day2 = str(commitList[1])[4:5]
                year2 = str(commitList[1])[7:11]
            date1 = date(int(year1),int(month1),int(day1))
            date2 = date(int(year2),int(month2),int(day2))
            difference = date1 - date2
            dateDifferenceData.append(difference.days)
            #print("Difference in number of days: " + str(difference.days))
    else:
        #Return 0 as there is only one commit date
        #print("ONE ARG CASE")
        dateDifferenceData.append(0)
    f = open("commitDateDifferences.txt", "w")
    f.write(str(dateDifferenceData))
    f.close()
