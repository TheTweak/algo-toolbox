import fileinput


def fib_period(m):
    f0 = 0
    f1 = 1
    period = [0, 1]
    for _ in range(2, 10**5):
        f0, f1 = f1%m, (f0+f1)%m
        period.append(f1)
        if f0 == 0 and f1 == 1:
            return period[:-2]


finput = fileinput.input()
n = int(next(finput))
if n == 0:
    print(0)
    exit(0)
if n == 1:
    print(1)
    exit(0)

p = fib_period(10)
lp = len(p)
quotient = n // lp
remainder = n % lp
print((sum(p)*quotient + sum(p[:remainder+1]))%10)
