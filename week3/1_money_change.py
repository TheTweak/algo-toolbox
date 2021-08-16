import fileinput

m = int(next(fileinput.input()))

coins = [10, 5, 1]
n = 0
while m > 0:
    for c in coins:
        if m - c >= 0:
            m -= c
            break
    n += 1
print(n)
