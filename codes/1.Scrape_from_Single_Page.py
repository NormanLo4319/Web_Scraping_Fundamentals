# Web Scraping Basics
# Extracting Data from Single Page

import requests
from bs4 import BeautifulSoup

# Setting the URL for scraping
url = 'http://quotes.toscrape.com'

# Create a request for the HTML document
response = requests.get(url)

# Parsing responses text attribute using lxml parser
soup = BeautifulSoup(response.text, 'lxml')

# Extracting the elements with tag, span and the class, text from the HTML documents
quotes = soup.find_all('span', class_='text')

# Extracting the elements with tag, small and the class, author from the HTML documents
authors = soup.find_all('small', class_='author')

# Extracting the elements with tag, div and the class, tags from the HTML documents
tags = soup.find_all('div', class_='tags')

# Create a loop to print the quote, author's name, tags
for i in range(0, len(quotes)):
    print("Quote: ", quotes[i].text)
    print("Author: ", authors[i].text)
    quoteTags = tags[i].find_all('a', class_='tag')
    for quoteTag in quoteTags:
        print("Tags: ", quoteTag.text)