def solution(string):
	num = int(string)
	num = str(bin(num)[2:]).count('1')
	print (f"Ouput: {num}")

string = input("Input: ")
solution(string)
