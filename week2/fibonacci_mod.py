import fileinput


def fib(n, m):
    f0 = 0
    if n == 0:
        return f0

    f1 = 1
    if n == 1:
        return f1

    for _ in range(n-1):
        f0, f1 = f1%m, (f0+f1)%m
    return f1


def fib_period(m):
    f0 = 0
    f1 = 1
    for i in range(2, 10**5):
        f0, f1 = f1%m, (f0+f1)%m
        if f0 == 0 and f1 == 1:
            return i - 1


finput = fileinput.input()
n, m = next(finput).split()
n, m = int(n), int(m)

period = fib_period(m)
print(fib(n%period, m))
