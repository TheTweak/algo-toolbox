import fileinput
import bisect

finput = fileinput.input()

s, p = next(finput).split()
s, p = int(s), int(p)

ends, starts = [], []
for _ in range(s):
    l, r = next(finput).split()
    starts.append(int(l))
    ends.append(int(r))
points = [int(x) for x in next(finput).split()]

starts = sorted(starts)
ends = sorted(ends)
result = [len(starts)] * len(points)
for index, point in enumerate(points):
    before = bisect.bisect_left(ends, point)
    after = len(starts) - bisect.bisect_right(starts, point)
    result[index] -= before
    result[index] -= after
print(*result)
