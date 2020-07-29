# Handling Drag and Drop

# Import the dependency
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Create a web driver
driver = webdriver.Chrome()

# Maximize the window
driver.maximize_window()

# Open up the URL
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

# Specify the source and destination element
source = driver.find_element_by_xpath('//*[@id="box3"]')
dest = driver.find_element_by_xpath('//*[@id="box103"]')

# Use Action Chains to drag and drop
actions = ActionChains(driver)
actions.drag_and_drop(source, dest).perform()