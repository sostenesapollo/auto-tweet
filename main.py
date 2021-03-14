from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

def load_credentials_from_json():
    try:
        file_data = open('credentials.json', ).read()
        return json.loads(file_data)
    except:
        exit(print("❌ Error to open credentials.json"))

def navigate_twitter():
    driver = webdriver.Chrome()
    driver.get("https://twitter.com/login")
    return driver

def login():
    input_username = driver.find_element_by_name('session[username_or_email]')
    input_password = driver.find_element_by_name('session[password]')

    input_username.click()
    input_username.send_keys(credentials['username'])

    input_password.click()
    input_password.send_keys(credentials['password'], Keys.RETURN)


credentials = load_credentials_from_json()

driver = navigate_twitter()

login()