from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from beautiful_soup import scrape_jobs
from fillOutJobForms import fillOutJobForms
from generateCSV import generateCSV

from visitWebsiteWithAuth import visitWebsiteWithAuth

def main():
    print("Application starting...")
    driver = webdriver.Chrome()
    visitWebsiteWithAuth(driver)
    current_url = fillOutJobForms(driver, "field application scientist", "uk")
    driver.close()
    list_of_jobs = scrape_jobs(current_url)
    generateCSV(list_of_jobs)



if __name__ == "__main__":
    main()