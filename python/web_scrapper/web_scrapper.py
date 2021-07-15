import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/q-python-jobs.html?vjk=ef7a13e91a0db178")
indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("ul", {"class": "pagination-list"})
pages = pagination.find_all('a')
spans = []

for page in pages:
  spans.append(page.find("span"))

spans = spans[:-1]
print(spans)
