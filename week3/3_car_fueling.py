# input: d - distance to the city
# m - miles on a single tank
# n - number of gas stations
# s1, s2, ..., sn - distance to stops
# output: min number of stops to reach d, or -1 if impossible

# greedy step: check if D is reachable from current location:
# 1) if not, find the next furthest reachable stop and move to it
# 1.a) if none stops are reachable, return -1
# 2) otherwise finish

import fileinput
from collections import deque

finput = fileinput.input()
d = int(next(finput))
m = int(next(finput))
n = int(next(finput))
stops = deque([int(s) for s in next(finput).split()])

i = 0
x = 0
while d - x > m:
    next_s = -1
    while stops:
        s = stops.popleft()
        if s - x <= m:
            next_s = s
        else:
            stops.appendleft(s)
            break
    if next_s < 0:
        i = -1
        break
    x = next_s
    i += 1
print(i)
