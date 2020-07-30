# Using API Keys

# Import the dependencies and API key
import requests
import json
from config import api_key

# Assign the base URL
# Remember to attach the http protocol to the front of the URL
baseURL = "http://api.openweathermap.org/data/2.5/forecast"

# Construct the parameter and API key for the request
parameters = {'APPID':api_key, 'q':'Seattle,US'}

# Create the request
response = requests.get(baseURL, params=parameters)

# Convert JSON document into dictionaries
info = json.loads(response.content)

# Print the dicitionary
print(info)