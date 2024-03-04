import requests

def is_human_entity(wikidata_id):
    # API endpoint for Wikidata
    url = f"https://www.wikidata.org/wiki/Special:EntityData/{wikidata_id}.json"

    try:
        # Send GET request
        response = requests.get(url)
        data = response.json()

        # Check if entity exists and has an "instance of" property
        if "entities" in data and wikidata_id in data["entities"]:
            entity = data["entities"][wikidata_id]
            if "claims" in entity and "P31" in entity["claims"]:
                for claim in entity["claims"]["P31"]:
                    if "mainsnak" in claim and "datavalue" in claim["mainsnak"]:
                        value = claim["mainsnak"]["datavalue"]["value"]
                        if value["id"] == "Q5":  # Q5 corresponds to human
                            return True

        # If no human claim found, return False
        return False

    except requests.exceptions.RequestException as e:
        print("Error making API request:", e)
        return False
