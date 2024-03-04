import requests

def get_wikidata_id_from_wikipedia(wikipedia_title):
    # API endpoint for MediaWiki
    mediawiki_api_url = 'https://en.wikipedia.org/w/api.php'
    
    # Parameters for the API request
    params = {
        'action': 'query',
        'titles': wikipedia_title,
        'prop': 'pageprops',
        'format': 'json',
        'redirects': 'true'
    }
    
    # Make the API request
    response = requests.get(mediawiki_api_url, params=params)
    data = response.json()
    
    # Extract Wikidata ID from the response
    if 'query' in data and 'pages' in data['query']:
        for page_id, page_info in data['query']['pages'].items():
            if 'pageprops' in page_info and 'wikibase_item' in page_info['pageprops']:
                wikidata_id = page_info['pageprops']['wikibase_item']
                return wikidata_id
    
    # Return None if Wikidata ID is not found
    return None


