import os
import apikey 
import requests
import json
import pyeuropeana.apis as apis
import pyeuropeana.utils as utils

# Woo hoo saving Europeana API key 
# hey queen remove ur api key before committing lmao
apikey.save("EUROPEANA_API_KEY", "MY_API_KEY")
europeana_api_key = apikey.load("EUROPEANA_API_KEY")
os.environ['EUROPEANA_API_KEY'] = europeana_api_key

# getting info from MET Museum API
url = 'https://collectionapi.metmuseum.org/public/collection/v1/search?q=pina'
response = requests.get(url)
resp_met_data = response.json()
    
print(resp_met_data)

# Grab data from Europeana 
resp_euro = apis.entity.suggest(
    # searches the term pina, a textile
    text = 'pina',
    TYPE = 'concept'
)
print(resp_euro)

# Pls work pls work pls work lol

# bruh moment okay not returning 2 files just one
# combining two API results into one dictionary
combined_api_results = {
    "MET Museum": resp_met_data,
    "Europeana": resp_euro
}

# Writing into JSON 
with open('met_and_europeana.json', 'w') as json_file:
    json.dump(combined_api_results, json_file, indent=4)

print("API data has been written to 'met_and_europeana.json' (YAY!)")