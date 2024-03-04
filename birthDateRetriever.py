import requests  # Importing the requests library for making HTTP requests

def get_birth_year_from_wikidata(wikidata_id):
    """
    Retrieves the birth year of a person from Wikidata using their Wikidata ID.

    Args:
        wikidata_id (str): The Wikidata ID of the person.

    Returns:
        int or None: The birth year of the person if found, else None.
    """
    # API endpoint for Wikidata
    wikidata_api_url = 'https://www.wikidata.org/w/api.php'
    
    # Parameters for the API request
    params = {
        'action': 'wbgetentities',  # Action to get entities
        'ids': wikidata_id,          # Wikidata ID of the person
        'format': 'json',            # Response format
        'props': 'claims'            # Requesting claims (statements) about the entity
    }
    
    # Make the API request
    response = requests.get(wikidata_api_url, params=params)  # Sending a GET request to the Wikidata API
    data = response.json()  # Converting the response to JSON format
    
    # Extract birth year from the response
    if 'entities' in data and wikidata_id in data['entities']:  # Checking if the entity exists in the response
        entity = data['entities'][wikidata_id]  # Getting the entity data
        if 'claims' in entity and 'P569' in entity['claims']:  # Checking if 'P569' (birth date property) exists
            birth_date_claim = entity['claims']['P569'][0]  # Getting the first claim for 'P569'
            if 'mainsnak' in birth_date_claim and 'datavalue' in birth_date_claim['mainsnak']:
                # Checking if 'mainsnak' and 'datavalue' exist
                birth_date_value = birth_date_claim['mainsnak']['datavalue']  # Getting the datavalue
                if 'value' in birth_date_value and 'time' in birth_date_value['value']:
                    # Checking if 'value' and 'time' exist
                    birth_year = birth_date_value['value']['time']  # Getting the datetime value
                    return int(birth_year[1:5])  # Extracting the year from the datetime format and returning it
    # Return None if birth year is not found
    return None

def get_century_from_year(year):
    """
    Calculates the century from a given year.

    Args:
        year (int or None): The year for which to calculate the century.

    Returns:
        int or None: The century of the given year if not None, else None.
    """
    if year is None:  # If the year is None, return None
        return None
    # Calculate the century
    century = (int(year) - 1) // 100 + 1  # Using integer division to get the century
    return century  # Return the calculated century
