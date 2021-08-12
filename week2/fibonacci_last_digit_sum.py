import fileinput


def fib_period(m):
    f0 = 0
    f1 = 1
    for i in range(2, 10**5):
        f0, f1 = f1%m, (f0+f1)%m
        if f0 == 0 and f1 == 1:
            return i - 1


finput = fileinput.input()
n = int(next(finput))

s = 0
if n >= 1:
    s += 1

f0 = 0
f1 = 1
p = fib_period(10)

for i in range(2, (n+1)%p):
    f0, f1 = f1, f0 + f1
    s += f1
print(s%10)
