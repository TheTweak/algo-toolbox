import fileinput
from collections import namedtuple

Major = namedtuple('Major', ['seq', 'el', 'cnt'])

finput = fileinput.input()

n = int(next(finput))
A = [int(x) for x in next(finput).split()]


def count(x, a):
    cnt = 0
    for y in a:
        if y == x:
            cnt += 1
    return cnt


def get_new_major(lhs, rhs):
    if lhs.el:
        cnt = count(lhs.el, rhs.seq)
        if cnt + lhs.cnt > (len(lhs.seq) + len(rhs.seq))//2:
            return Major(lhs.seq+rhs.seq, lhs.el, cnt+lhs.cnt)
    return None


def merge(lhs, rhs):
    #print(f'lhs={lhs} rhs={rhs}')
    new_major = get_new_major(lhs, rhs)
    if new_major:
        return new_major
    new_major = get_new_major(rhs, lhs)
    if new_major:
        return new_major
    return Major(lhs.seq+rhs.seq, None, 0)


def get_majority(a):
    #print(f'a={a}')
    if len(a.seq) == 1:
        return Major(a.seq, a.seq[0], 1)
    l = a.seq[:len(a.seq)//2]
    r = a.seq[len(a.seq)//2:]
    lm = get_majority(Major(l, None, 0))
    rm = get_majority(Major(r, None, 0))
    r = merge(lm, rm)
    #print(f'r={r}')
    return r


print(1 if get_majority(Major(A, None, 0)).el else 0)
