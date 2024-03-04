import requests  # Importing requests for making HTTP requests

def get_wikidata_id_from_wikipedia(wikipedia_title):
    """
    Retrieves the Wikidata ID associated with a Wikipedia article.

    Args:
        wikipedia_title (str): The title of the Wikipedia article.

    Returns:
        str or None: The Wikidata ID if found, else None.
    """
    # API endpoint for MediaWiki
    mediawiki_api_url = 'https://en.wikipedia.org/w/api.php'
    
    # Parameters for the API request
    params = {
        'action': 'query',        # Action to perform (query)
        'titles': wikipedia_title,  # Title of the Wikipedia article
        'prop': 'pageprops',      # Property to fetch (pageprops)
        'format': 'json',         # Response format (JSON)
        'redirects': 'true'       # Follow redirects
    }
    
    # Make the API request
    response = requests.get(mediawiki_api_url, params=params)  # Sending a GET request to the MediaWiki API
    data = response.json()  # Converting the response to JSON format
    
    # Extract Wikidata ID from the response
    if 'query' in data and 'pages' in data['query']:
        for page_id, page_info in data['query']['pages'].items():
            if 'pageprops' in page_info and 'wikibase_item' in page_info['pageprops']:
                # If 'wikibase_item' is found in 'pageprops', it contains the Wikidata ID
                wikidata_id = page_info['pageprops']['wikibase_item']  # Extracting the Wikidata ID
                return wikidata_id  # Returning the Wikidata ID
    
    # Return None if Wikidata ID is not found
    return None
