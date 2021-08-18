'''
Input:
    n - number of integers
    a1, a2, ..., an - integers
Output:
    largest number that can be composed out of a1, a2, ..., an
Greedy step:
    get the largest lexicographically number, append to the result
    continue with the rest
'''
import fileinput

finput = fileinput.input()


def is_gr_or_eq(a, b):
    sa = str(a)
    sb = str(b)
    return int(sa+sb) >= int(sb+sa)


n = int(next(finput))
N = [int(i) for i in next(finput).split()]
result = []
while N:
    max_digit = 0
    max_digit_i = 0
    for i, d in enumerate(N):
        if is_gr_or_eq(d, max_digit):
            max_digit = d
            max_digit_i = i
    result.append(max_digit)
    N.pop(max_digit_i)

print(''.join([str(i) for i in result]))
