n = 43
a, b = 1, 17
c = abs(a - b)

print(2**(c-1)+2**(n-c-1)-1)
print((1<<(c-1))+(1<<(n-c-1))-1)
