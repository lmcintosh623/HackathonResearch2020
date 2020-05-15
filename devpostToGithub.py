
import requests
import sys
import re
from bs4 import BeautifulSoup

projectLink = requests.get('https://bytehacks2018.devpost.com/submissions').text
soupProjects = BeautifulSoup(projectLink, 'html.parser')

for link in soupProjects.findAll('a', { 'class' : 'block-wrapper-link fade link-to-software'}, href=True ):
    print (link['href'])