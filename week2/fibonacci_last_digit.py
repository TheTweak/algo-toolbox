import fileinput

n = int(next(fileinput.input()))

f0 = 0
if n == 0:
	print(f0)
	exit(0)

f1 = 1
if n == 1:
	print(f1)
	exit(0)

fn = 0
for _ in range(n-1):
	fn = (f0 + f1) % 10
	f0 = f1 % 10
	f1 = fn
print(fn)
