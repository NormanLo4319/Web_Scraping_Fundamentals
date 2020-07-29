# Selenium Implicit Wait Functions

# Import Selenium Web Driver
from selenium import webdriver

# Assigning the URL
url = 'https://www.google.com/earth/'

# Initialize the webdriver
driver = webdriver.Chrome()

# Create the implicit wait (5 seconds)
driver.implicitly_wait(5)

# Open up the URL
driver.get(url)

# Find the button element
launchEarthButton = driver.find_element_by_xpath('/html/body/header/div/nav[1]/ul[2]/li[2]/a')

# Create a click action on the button
launchEarthButton.click()