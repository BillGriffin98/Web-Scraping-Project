import requests

def get_birth_year_from_wikidata(wikidata_id):
    # API endpoint for Wikidata
    wikidata_api_url = 'https://www.wikidata.org/w/api.php'
    
    # Parameters for the API request
    params = {
        'action': 'wbgetentities',
        'ids': wikidata_id,
        'format': 'json',
        'props': 'claims'
    }
    
    # Make the API request
    response = requests.get(wikidata_api_url, params=params)
    data = response.json()
    
    # Extract birth year from the response
    if 'entities' in data and wikidata_id in data['entities']:
        entity = data['entities'][wikidata_id]
        if 'claims' in entity and 'P569' in entity['claims']:
            birth_date_claim = entity['claims']['P569'][0]
            if 'mainsnak' in birth_date_claim and 'datavalue' in birth_date_claim['mainsnak']:
                birth_date_value = birth_date_claim['mainsnak']['datavalue']
                if 'value' in birth_date_value and 'time' in birth_date_value['value']:
                    birth_year = birth_date_value['value']['time']
                    return int(birth_year[1:5])  # Extract the year from the datetime format
    # Return None if birth year is not found
    return None

def get_century_from_year(year):
    if year is None:
        return None
    # Calculate the century
    century = (int(year) - 1) // 100 + 1
    return century
