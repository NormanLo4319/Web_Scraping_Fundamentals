# Basic Browser Interaction

# Import the dependencies
from selenium import webdriver

# Initialize the webdriver
driver = webdriver.Chrome()

# Open up the URL
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

# Find element by xpath
messageField = driver.find_element_by_xpath('//*[@id="sum1"]')

# Pass a string to the message field using the send keys method
messageField.send_keys('Hello World')

# Click the Show Message button
showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')

# Click on the button using click()
showMessageButton.click()

# Input the first number to the first field
additionField1 = driver.find_element_by_xpath('//*[@id="sum1"]')
additionField1.send_keys('10')

# Input the first number to the second field
additionField2 = driver.find_element_by_xpath('//*[@id="sum2"]')
additionField2.send_keys('20')

# Click the "Get Total" button
getTotalButton = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
getTotalButton.click()