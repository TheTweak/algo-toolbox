import fileinput

input = fileinput.input()
a, b = next(input).split()
a, b = int(a), int(b)

def gcd(c, d):
	if d == 0:
		return c
	return gcd(d, c % d)

if a > b:
	print(gcd(a, b))
else:
	print(gcd(b, a))
