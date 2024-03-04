from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import matplotlib as mpl
import csv
from birthDateRetriever import get_birth_year_from_wikidata, get_century_from_year
from noteworthiness import count_hyperlinks_in_wikipedia

from wikidataID import get_wikidata_id_from_wikipedia
from isHuman import is_human_entity


wikipedia_url = f'https://en.wikipedia.org/wiki/Burials_and_memorials_in_Westminster_Abbey'
    
response = requests.get(wikipedia_url)

# Collects all the text from the Wikipedia page and formats it as HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Get all the lists from the main body of the text
allLists = soup.find(id="bodyContent").find_all("ul")
allLinks = []
linkToScrape = []

for i in range (0,16):
    allLinks = allLists[i].find_all("a")
    for link in allLinks:
    # We are only interested in other wiki articles
        if link['href'].find("/wiki/") == -1:
            continue

    # Use this link to scrape
        wikipedia_title = link.get('href')[6:]
        wikidata_id = get_wikidata_id_from_wikipedia(wikipedia_title)
        if wikidata_id and is_human_entity(wikidata_id) and get_birth_year_from_wikidata(wikidata_id) != None:
            linkToScrape.append([link.get('title'), link.get('href'), wikidata_id, get_birth_year_from_wikidata(wikidata_id), get_century_from_year(get_birth_year_from_wikidata(wikidata_id)), count_hyperlinks_in_wikipedia(wikipedia_title)])
print(linkToScrape)

with open('file.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(linkToScrape)
