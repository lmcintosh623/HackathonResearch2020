# msg = "I got this!"
# Hackathon Research Project Webscrape first draft 
# Target:   mlh.io list of hackathon names
# Author: Lukas McIntosh

import requests
from bs4 import BeautifulSoup


page_data_2018 = requests.get('https://mlh.io/seasons/na-2018/events').text
soup2018 = BeautifulSoup(page_data_2018, 'html.parser')             #soup2018 object used to view 2018 Hackathons 
page_data_2019 = requests.get('https://mlh.io/seasons/na-2019/events').text
soup2019 = BeautifulSoup(page_data_2019, 'html.parser')             #soup2019 object used to view 2019 Hackathons


# Example input
# <h3 class="event-name" itemprop="name">Hackital</h3>

hackathonCount = 0
hackathons = []

print("==========2018 Hackathons========== ")
    #stores hackathon names from 2018  
for h3 in soup2018.findAll('h3', { 'class' : 'event-name'}):
    nameStr = [h3.text.strip()]
    hackathons.append(nameStr)
    hackathonCount += 1
print("---------->" + str(hackathonCount) + " hackathons from 2018<----------")
temp = hackathonCount

    #stores hackathon names from 2019
for h3 in soup2019.findAll('h3', { 'class' : 'event-name'}):
    nameStr = [h3.text.strip()]
    hackathons.append(nameStr)
    hackathonCount += 1
print("---------->" + str(hackathonCount-temp) + " hackathons from 2019<----------")

    #prints all names and then the number of hackathons total
for hackathon in hackathons:
    print(hackathon)
print(str(hackathonCount) + " hackathons in 2018 and 2019 lists total")