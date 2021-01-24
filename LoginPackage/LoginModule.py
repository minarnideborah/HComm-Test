'''
Created on Jan 24, 2021

@author: Minarni Debora
'''

from selenium import webdriver
import string
import random
import time

# Initialize the Url
url = "http://staging-hcomm-frontend.vnvglobal.id/"

# Generate Random Email
def randomEmailGenerator(y):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(y))

# Generate Random Domain
def randomDomainGenerator():
    domains = ["gmail.com", "outlook.com", "yahoo.com"]
    return ''.join(random.choice(domains))

# Generate Random Password
def randomPasswordGenerator(y):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for _ in range(y))

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

# Find SELL ON HCOMM button and click the button
element = driver.find_element_by_xpath("//a[text()='sell on hcomm']")
element.click()

# Find Email field and fill the field with random generated email
element = driver.find_element_by_id("email")
element.send_keys(randomEmailGenerator(8) + "@" + randomDomainGenerator())

# Find Password field and fill the field with random generated password
element = driver.find_element_by_id("password")
element.send_keys(randomPasswordGenerator(8))

# Find Login button and click the button
element = driver.find_element_by_xpath("//button[text()='Login']")
element.click()

# Delay 5 seconds, wait for Error Message element to shown
time.sleep(5)

# Find element that contains "Account does not exist"
element = driver.find_element_by_xpath("//*[contains(text(), 'Account does not exist')]")
# element = driver.find_element_by_xpath("//*[contains(text(), 'Incorrect Password')]")

# Check if the element is appeared
if element.is_displayed():
    print("Pass")
else:
    print("Failed")
    
# Close the Browser
driver.close()