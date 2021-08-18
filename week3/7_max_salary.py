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
    for i, j in zip(sa, sb):
        if int(i) > int(j):
            return True
        elif int(i) < int(j):
            return False
    if len(sa) < len(sb):
        if int(sa[-1]) >= int(sb[len(sa)]):
            return True
        else:
            return False
    elif len(sa) > len(sb):
        return not is_gr_or_eq(b, a)
    return True


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
