# Web-Scraping Basics:
# Scraping from Multiple Pages (Paginated Scraping)

# Import the dependencies
from bs4 import BeautifulSoup
import requests

# Assigne the URL path
url = 'https://scrapingclub.com/exercise/list_basic/?page=1'

# Create a request to the web page
response = requests.get(url)

# Parsing the HTML document
soup = BeautifulSoup(response.text, 'lxml')

# Find the page buttons
pages = soup.find('ul', class_='pagination')

# Create an empty list for storing the page urls
urls = []

# Find all the links to different pages
links = pages.find_all('a', class_='page-link')

# Iterate through all the link element
for link in links:
    # Find the page number through each link
    pageNum = int(link.text)if link.text.isdigit() else None
    # Append the url to the list if it exists
    if pageNum != None:
        x = link.get('href')
        urls.append(x)

# Add the page url to the original url
# Print all item names and prices from each page
for i in urls:
    newUrl = url + i
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    count = 1
    for i in items:
        itemName = i.find('h4', class_='card-title').text.strip('\n')
        itemPrice = i.find('h5').text
        print('%s) Price: %s, Item Name: %s' % (count, itemPrice, itemName))
        count = count + 1