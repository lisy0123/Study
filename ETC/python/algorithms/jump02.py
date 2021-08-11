a= {'A':90, 'B':80}

try:
	a['C']
except KeyError:
	print(70)

if 'C' in a:
	print(a['C'])
else:
	print(70)

a.get('C', 70)
