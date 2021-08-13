import fileinput


def fib_period(m):
    f0 = 0
    f1 = 1
    for i in range(2, 10**5):
        f0, f1 = f1%m, (f0+f1)%m
        if f0 == 0 and f1 == 1:
            return i - 1


finput = fileinput.input()
m, n = next(finput).split()
m, n = int(m), int(n)

s = 0
if m >= 1:
    s += 1

f0 = 0
f1 = 1
p = fib_period(10)

sm = 0
for i in range(2, m%p):
    f0, f1 = f1, f0 + f1
    sm += f1
print(sm%10)

f0 = 0
f1 = 1
sn = 0
for i in range(2, n%p+1):
    f0, f1 = f1, f0 + f1
    sn += f1
print(sn%10)
print(abs(sn%10-sm%10))
