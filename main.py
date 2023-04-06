from selenium import webdriver
from beautiful_soup import scrape_jobs
from fillOutJobForms import fillOutJobForms
from generateCSV import generateCSV
from visitWebsiteWithAuth import visitWebsiteWithAuth
from typing import Annotated
from fastapi import FastAPI, Form

def run_application(website, keyword, location):
    print("Application starting...")
    driver = webdriver.Chrome()
    visitWebsiteWithAuth(driver)
    current_url = fillOutJobForms(driver, keyword, location)
    driver.close()
    list_of_jobs = scrape_jobs(current_url)
    generateCSV(list_of_jobs)
    return "completed"



app = FastAPI()
@app.post("/jobs/")
async def root(website: Annotated[str, Form()], keywords: Annotated[str, Form()], location: Annotated[str, Form()]):
    message = run_application(website, keywords, location)
    # message = website, keywords, location
    return message



# @app.post("/login/")
# async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
#     return {"username": username}