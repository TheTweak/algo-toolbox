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
m, n = next(finput).split()
m, n = int(m), int(n)

p = fib_period(10)
p_sum = sum(p)
lp = len(p)

quotient = (m-1) // lp
remainder = (m-1) % lp
sm = p_sum*quotient + sum(p[:remainder+1])

quotient = n // lp
remainder = n % lp
sn = p_sum*quotient + sum(p[:remainder+1])
#print(f'Sn={sn} Sm={sm}')
print((sn-sm)%10)
