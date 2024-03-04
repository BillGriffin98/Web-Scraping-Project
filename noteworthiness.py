from bs4 import BeautifulSoup  # Importing BeautifulSoup for parsing HTML
import requests  # Importing requests for making HTTP requests

def count_hyperlinks_in_wikipedia(wikipedia_title):
    """
    Counts the number of hyperlinks in a Wikipedia article.

    Args:
        wikipedia_title (str): The title of the Wikipedia article.

    Returns:
        int: The number of hyperlinks in the article.
    """
    # Construct the Wikipedia URL
    wikipedia_url = f'https://en.wikipedia.org/wiki/{wikipedia_title.replace(" ", "_")}'
    
    # Fetch the page
    response = requests.get(wikipedia_url)  # Sending a GET request to the Wikipedia URL
    soup = BeautifulSoup(response.text, 'html.parser')  # Parsing the HTML content with BeautifulSoup

    # Find all <a> tags (hyperlinks) in the parsed HTML
    hyperlinks = soup.find_all('a')  # Finding all <a> tags in the parsed HTML
    
    # Count the number of hyperlinks
    num_hyperlinks = len(hyperlinks)  # Getting the length (count) of the hyperlinks
    
    return num_hyperlinks  # Returning the number of hyperlinks
