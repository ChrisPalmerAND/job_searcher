from selenium.webdriver.common.by import By
import time

def visitWebsiteWithAuth(driver):
    print("Locating LinkedIn")
    driver.get("https://www.linkedin.com")
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Jobs").click()
    time.sleep(3)
    