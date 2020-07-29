# Selenium Explicit Wait Functions

# Import the dependencies
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Assigning the URL
url = 'https://www.google.com/earth/'

# Initialize the webdriver
driver = webdriver.Chrome()

# Create the wait function for the web driver
# This function will throw an exception after 10 seconds 
# if the condition is not satisfied
wait = WebDriverWait(driver, 10)

# Creating condition for the button action
launchEarthButton = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/nav[1]/ul[2]/li[2]/a')))

# Add the click function to the button
launchEarthButton.click()