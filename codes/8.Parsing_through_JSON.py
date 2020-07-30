# Parsing through JSON

# Import the dependencies
import requests
import json

# Assigning the base URL
baseURL = 'https://api.upcitemdb.com/prod/trial/lookup'

# Construct the parameter for the API call
# The parameter is a Python dictionary
parameters ={'upc': '710244229739'}

# Send the GET query containing the parameters and the base URL
response = requests.get(baseURL, params=parameters)

# Create the response content
content = response.content

# Convert JSON document into dictionaries
info = json.loads(content)

# Extract the item from the dictionary
item = info['items']

# Extract the item info form item
itemInfo = item[0]

# Extrac the title of the item
title = itemInfo['title']

# Extract the brand name of the item
brand = itemInfo['brand']

# Extract the highest price
high = itemInfo['highest_recorded_price']

# Extract the lowest price
low = itemInfo['lowest_recorded_price']

# Print the titel and brand
print("Item Title: ", title)
print("Item Brand: ", brand)
print("Highest Price: ", high)
print("Lowest Price: ", low)