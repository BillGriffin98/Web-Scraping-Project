# Web Scraper - Westminster Abbey Burials 

This project is a Python script for scraping information about individuals buried at Westminster Abbey, London from their Wikipedia pages. It retrieves names, birth years, Wikipedia links, Wikidata IDs, century of birth, and counts of hyperlinks in the Wikipedia articles. Based on this data, we can infer that although the 18th Century accounts for the birth years of the most individuals buried at the Abbey, the most notable figures tended to be born in the 19th Century.

## Table of Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Challenges Faced](#challenges-faced)
- [Approach](#approach)


## Overview

Westminster Abbey is a historic place with many notable burials. This project aims to collect data on individuals buried there, such as their birth years and Wikipedia links. The collected data, including the count of hyperlinks in their Wikipedia articles, can be useful for historical analysis, genealogy research, or simply for exploring the history of Westminster Abbey's inhabitants. The count of hyperlinks serves as a heuristic to assess the 'noteworthiness' of the individual, providing an additional dimension for analysis.

## Technologies Used

- **BeautifulSoup**: Used to extract data from the Wikipedia page's HTML, specifically to navigate and scrape the burial information.
- **Requests**: Utilised to fetch the HTML content of the Wikipedia page on burials and memorials in Westminster Abbey.
- **Pandas**: Organised and processed the scraped burial data into a structured format, facilitating further analysis.
- **Matplotlib**: Used to create visualizations such as graphs to analyze trends in burial data, like birth years and noteworthiness.
- **Seahorse**: Used to count hyperlinks in Wikipedia articles, retrieve data from Wikidata, and validate if a Wikidata entity is about a human.
  

## Challenges Faced

### Handling Dynamic Content
Some Wikipedia pages may have dynamic content or different structures, which could lead to issues in parsing the data consistently. To overcome this, the script was designed to be flexible in handling various HTML structures and content layouts.

### Data Validation and Error Handling
The script had to validate Wikidata IDs to ensure they represented human entities with birth years. Robust error handling was implemented to handle cases of missing data or invalid URLs, preventing unexpected crashes and ensuring a smooth scraping process.

### Duplicate Entry Prevention
As the script scraped multiple Wikipedia pages, it needed to prevent duplicate entries in the final dataset. This was achieved by maintaining a set of visited Wikidata IDs and checking each ID before adding it to the dataset, ensuring each individual was included only once.

### Scalability and Efficiency
The script was designed to be efficient and scalable, capable of handling a large number of Wikipedia pages. Techniques such as batching requests and optimizing the data retrieval process were implemented to improve performance and reduce the overall execution time.


## Approach

The script uses Python along with the BeautifulSoup library for parsing HTML and the requests library for making HTTP requests. It also utilizes custom functions for retrieving data from Wikidata, counting hyperlinks in Wikipedia articles, and checking if a Wikidata entity represents a human.

Here's a brief overview of the steps:

1. Send a GET request to the Wikipedia page listing burials at Westminster Abbey.
2. Parse the HTML content of the response using BeautifulSoup.
3. Find all lists from the main body of the text.
4. Loop through each list to find links to Wikipedia articles.
5. Extract relevant information such as the title, URL, and Wikidata ID from each link.
6. Validate the Wikidata ID, ensuring it represents a human and has a birth year.
7. Collect additional information like birth year, century, and hyperlink count (as a heuristic for 'noteworthiness').
8. Write the collected data to a CSV file.


## Detailed Explanation of Main.py

The following chunk of code is responsible for scraping data from a Wikipedia page about burials and memorials in Westminster Abbey. Let's break down what each part of the code does:

### Imports
```python
from bs4 import BeautifulSoup  # Import BeautifulSoup for parsing HTML
import requests  # Import requests for making HTTP requests
import csv  # Import csv for reading and writing CSV files
from birthDateRetriever import get_birth_year_from_wikidata, get_century_from_year  # Takes a WikidataID and returns the associated birth-year
from noteworthiness import count_hyperlinks_in_wikipedia  # counts the number of hyperlinks within a Wikipedia page
from wikidataID import get_wikidata_id_from_wikipedia  # Takes a Wikipedia URL and returns its associated Wikidata ID
from isHuman import is_human_entity  # Checks if a Wikipedia page is describing a human or not.
```
This imports necessary libraries and custom functions for scraping Wikipedia data.

### Web Scraping
```python
# URL of the Wikipedia page to scrape
wikipedia_url = f'https://en.wikipedia.org/wiki/Burials_and_memorials_in_Westminster_Abbey'

# Send a GET request to the Wikipedia URL to get the page content
response = requests.get(wikipedia_url)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all lists from the main body of the text
allLists = soup.find(id="bodyContent").find_all("ul")
```
This fetches the HTML content of the Wikipedia page and parses it using BeautifulSoup to find all lists from the main body of the text.

### Data Collection and Processing
```python
# List to store information about each individual
linkToScrape = []

# Set to store visited Wikipedia IDs
visited_ids = set()

# Loop through all the lists
for i in range(0, 16):
    allLinks = allLists[i].find_all("a")  # Find all <a> tags within the current list
    for link in allLinks:
        # We are only interested in other wiki articles
        if link['href'].find("/wiki/") == -1:
            continue

        # Extract the title of the Wikipedia article
        wikipedia_title = link.get('href')[6:]

        # Get the Wikidata ID associated with the Wikipedia article
        wikidata_id = get_wikidata_id_from_wikipedia(wikipedia_title)

        # Check if the Wikidata ID is valid, is about a human, and has a birth year
        if (
            wikidata_id
            and is_human_entity(wikidata_id)
            and get_birth_year_from_wikidata(wikidata_id) is not None
            and wikidata_id not in visited_ids  # Check if the ID has been visited
        ):
            # Add the Wikidata ID to the set of visited IDs
            visited_ids.add(wikidata_id)

            # Get additional information about the individual and append to the list
            linkToScrape.append([
                link.get('title'),  # Wikipedia article title
                link.get('href'),   # Wikipedia article URL
                wikidata_id,        # Wikidata ID
                get_birth_year_from_wikidata(wikidata_id),  # Birth year
                get_century_from_year(get_birth_year_from_wikidata(wikidata_id)),  # Century
                count_hyperlinks_in_wikipedia(wikipedia_title)  # Count of hyperlinks in the Wikipedia article
            ])
```
This collects data about individuals buried at Westminster Abbey, including their birth year, century, and count of hyperlinks in their Wikipedia articles, after ensuring their Wikidata ID is valid and represents a human.

### Writing to CSV
```python
print(linkToScrape)

# Write the collected data to a CSV file
with open('file.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(linkToScrape)
```
This then prints the collected data and writes it to a CSV file named file.csv for further analysis.

## Data Visualisation 
The dataVis.py utilises Pandas, Seaborn, and Matplotlib to generate three different graphs.
![alt text](https://github.com/BillGriffin98/WebScrapingProject/blob/main/Proportion%20of%20burials%20by%20century.png)


Upon analysis, it becomes evident that the majority of individuals buried at Westminster Abbey were born in the 17th and 18th centuries, with the fewest born in the 13th and 20th centuries. This observation raises questions about the increasing frequency of burials at the Abbey from the 17th century onwards, as well as the subsequent decline in popularity after the 18th Century.

![alt text](https://github.com/BillGriffin98/WebScrapingProject/blob/main/Birth%20year%20vs%20noteworthiness.png)
This scattergraph illustrates the surge in the number of burials during the 17th century and the distribution of 'noteworthy' individuals. It is evident that only a handful of individuals have amassed extensive Wikipedia pages with numerous connections to other historical figures and events, while many others are associated with relatively fewer connections.

![alt text](https://github.com/BillGriffin98/WebScrapingProject/blob/main/Noteworthiness%20by%20Century.png)

