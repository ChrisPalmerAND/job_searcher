from selenium import webdriver
from beautiful_soup import scrape_jobs
from fillOutJobForms import fillOutJobForms
from generateCSV import generateCSV
from visitWebsiteWithAuth import visitWebsiteWithAuth
from fastapi import FastAPI

def run_application(keyword, location):
    print("Application starting...")
    driver = webdriver.Chrome()
    visitWebsiteWithAuth(driver)
    current_url = fillOutJobForms(driver, keyword, location)
    driver.close()
    list_of_jobs = scrape_jobs(current_url)
    generateCSV(list_of_jobs)
    return "completed"



app = FastAPI()
@app.get("/jobs/")
async def root(keyword: str, location: str):
    message = run_application(keyword, location)
    return message