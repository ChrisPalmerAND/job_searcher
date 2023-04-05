import bs4 as bs
import urllib.request

def scrape_jobs(current_url):
    source = urllib.request.urlopen(current_url).read()
    soup = bs.BeautifulSoup(source,'lxml')

    list_of_jobs = []
    for job in soup.find_all('div', class_="base-search-card"):
        link = job.find('a')['href'].replace('\n', '')
        title = job.find('h3').text.strip()
        company = job.find('h4').text.strip()
        list_of_jobs.append({"title": title, "link": link, "company": company})

    return list_of_jobs
