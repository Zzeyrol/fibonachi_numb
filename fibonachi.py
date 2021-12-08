n = int(input ())
def number (n):
	if n in (1, 2):
		return 1
	return  number(n - 1) + number (n - 2)

print (number(n))