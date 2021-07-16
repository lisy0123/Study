import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = "https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
	result = requests.get(URL)
	soup = BeautifulSoup(result.text, "html.parser")
	pagination = soup.find("ul", {"class": "pagination-list"})
	links = pagination.find_all('a')
	pages = []

	for link in links[:-1]:
	  pages.append(int(link.string))
	max_page = pages[-1]
	return (max_page)


def extract_indeed_jobs(last_page):
	jobs = []
	for page in range(last_page):
		result = requests.get(f"{URL}&start={0*LIMIT}")
		soup = BeautifulSoup(result.text, "html.parser")
		results = soup.find_all("div", {"class": "slider_container"})
		for result in results:
			jobtitle = result.find("h2", {"class": "jobTitle"})
			title = jobtitle.find("span").string
			if title == "new":
				title = jobtitle.find_all("span")[1].string
			print(title)
	return jobs
