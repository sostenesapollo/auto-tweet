import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Explicit Wait libs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import json

def get_credentials_from_json():
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
    time.sleep(2)
    input_username = driver.find_element_by_name('session[username_or_email]')
    input_password = driver.find_element_by_name('session[password]')

    input_username.click()
    input_username.send_keys(credentials['username'])

    input_password.click()
    input_password.send_keys(credentials['password'], Keys.RETURN)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "partner_id_sync_pixel"))
        )
    except:
        exit(print("❌ Login Error."))
    
    print("✅ Logged In")


credentials = get_credentials_from_json()

driver = navigate_twitter()

login()

tweet = driver.find_element_by_xpath('''//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div
                                                  /div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div
                                                  /div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div
                                                  /div/div/div''')
for i in range(0,200):
    tweet.send_keys("""Hello World!"""+str(i))
    time.sleep(2)
    tweet.send_keys(Keys.CONTROL, Keys.ENTER)
    time.sleep(7)