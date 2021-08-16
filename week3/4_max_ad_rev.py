'''
Input:
    n - number of ads
    a0, ..., an - profit per click
    b0, ..., bn - clicks per day
Output:
    Max sum of products of permutations of (a, b)

Greedy step:
    Take max ai and max bi
'''
import fileinput

finput = fileinput.input()

n = int(next(finput))
A = [int(a) for a in next(finput).split()]
B = [int(b) for b in next(finput).split()]
A.sort(reverse=True)
B.sort(reverse=True)

result = 0
for a, b in zip(A, B):
    result += a*b
print(result)
