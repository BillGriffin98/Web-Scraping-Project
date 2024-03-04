from bs4 import BeautifulSoup
import requests

def count_hyperlinks_in_wikipedia(wikipedia_title):
    # Construct the Wikipedia URL
    wikipedia_url = f'https://en.wikipedia.org/wiki/{wikipedia_title.replace(" ", "_")}'
    
    # Fetch the page
    response = requests.get(wikipedia_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <a> tags (hyperlinks)
    hyperlinks = soup.find_all('a')

    # Count the number of hyperlinks
    num_hyperlinks = len(hyperlinks)
    
    return num_hyperlinks
