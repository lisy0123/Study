import requests
import os

quit = 'y'

while quit == 'y':
	print("Welcom to IsItDown.py!")
	print("Please write a URL or URLs you wnat to check. (separated by comma)")

	url = input().split(",")

	for i in range(len(url)):
		url[i] = url[i].strip().lower()
		if '.' not in url[i]:
			print(url[i] + " is not a valid URL.")
			continue
		if 'http' not in url[i]:
			url[i] = 'http://' + url[i]
		try:
			res = requests.get(url[i])
			if res.status_code == requests.codes.ok:
				print(url[i] + " is up!")
			else:
				print(url[i] + " is down!")
		except:
			print(url[i] + " is down!")
	
	tmp = True
	while tmp:
		quit = input("Do you want to start over? y/n ")
		if quit != 'y' and quit != 'n':
			print("That's not a valid answer.")
		else:
			tmp = False
			if quit == 'y':
				os.system('clear')
print("Ok. bye!")
