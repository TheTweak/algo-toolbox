import fileinput

input = fileinput.input()
a, b = next(input).split()
a, b = int(a), int(b)

def gcd(c, d):
	if d == 0:
		return c
	return gcd(d, c % d)

gcdN = 0
if a > b:
	gcdN = gcd(a, b)
else:
	gcdN = gcd(b, a)

print(int((a*b)/gcdN))