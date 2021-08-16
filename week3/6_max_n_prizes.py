'''
Input:
    n - number of candies
Output:
    m - number of distinct integers
    mi, ..., mm - distinct integers
Greedy step:
    while n > 0:
    pick number i, starting from 1
    check that n - i > i
    - if not, n -= i and continue with i + 1
    - otherwise stop, return n as a result
'''
import fileinput

finput = fileinput.input()

n = int(next(finput))

m = 1
M = []
i = 1
while n > 0:
    if n - i > i:
        n -= i
        M.append(i)
        i += 1
        m += 1
    else:
        M.append(n)
        break
print(m)
print(' '.join([str(i) for i in M]))
