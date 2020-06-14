#Method to choose which hackathon objects to return for the devpostURL searchs.
# WILL COMPLETE IN SUMMER QUARTER
import requests
import sys
import re
from bs4 import BeautifulSoup

def scrapeDevpostHackathonPages():
    with open("devpostURLS.txt", "r") as url:
        search_page_results = requests.get(url).text
        #Soup object to find all Hackathon titles and choose which to keep.
        seachPageSoup = BeautifulSoup(search_page_results, 'html.parser')
    