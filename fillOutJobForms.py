from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def fillOutJobForms(driver, keyword_string, location):
    keywordsInput = driver.find_element(By.NAME, "keywords")
    keywordsInput.send_keys(keyword_string)
    locationInput = driver.find_element(By.NAME, "location")
    locationInput.clear()
    locationInput.send_keys(location)
    locationInput.send_keys(Keys.RETURN)
    current_url = (driver.current_url)
    time.sleep(5)
    return current_url