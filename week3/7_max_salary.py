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
from functools import cmp_to_key

finput = fileinput.input()


def lex_cmp(lhs, rhs):
    if len(lhs) <= len(rhs):
        last = lhs[-1]
        for _ in range(len(rhs)-len(lhs)):
            lhs += last
    else:
        return -lex_cmp(rhs, lhs)
    #print(f'cmp lhs={lhs} rhs={rhs}')
    for l, r in zip(lhs, rhs):
        if int(l) > int(r):
            #print(f'cmp l={l} > r={r}, return 1')
            return 1
        elif int(l) < int(r):
            #print(f'cmp l={l} < r={r}, return -1')
            return -1
    print(f'return 0')
    return 0


n = int(next(finput))
N = next(finput).split()
N.sort(key=cmp_to_key(lex_cmp), reverse=True)
print(''.join([str(i) for i in N]))
