import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
URL = "https://www.iban.com/currency-codes"
things = []
country = []
code = []

result = requests.get(URL)
soup = BeautifulSoup(result.text, "html.parser")
everything = soup.find("tbody").find_all("td")
for i in everything:
	things.append(i.string)
for i in range(len(things)):
	if i % 4 == 0:
		if things[i + 1] == "No universal currency":
			continue
		else:
			country.append(things[i].capitalize())
	if i % 4 == 2:
		if things[i] == None:
			continue
		else:
			code.append(things[i])

print("Hello! Please choose select a country by number:")
for i in range(len(country)):
	print(f"# {i} {country[i]}")

while True:
	try:
		num = int(input("#: "))
		if num >= 0 and num <= 264:
			break
		else:
			print("Choose a number from the list.")
	except ValueError:
		print("That wasn't a number")

print(f"You chose {country[num]}.")
print(f"The currency code is {code[num]}.")
