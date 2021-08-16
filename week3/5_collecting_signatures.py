'''
Input:
    n - number of segments
    ai, bi - endpoints of a segment
Output:
    m - min number of points to mark all segments
    mi - points coordinates

Greedy step:
    take the leftmost segment and add a point to its right endpoint
    continue with segments that are not marked by previous point
'''

import fileinput

finput = fileinput.input()

n = int(next(finput))
segments = []
for _ in range(n):
    a, b = next(finput).split()
    segments.append((int(a), int(b)))

segments.sort(key=lambda p: p[1])

points = []
p = -1
for a, b in segments:
    if p < a:
        p = b
        points.append(p)

print(len(points))
print(' '.join([str(i) for i in points]))
