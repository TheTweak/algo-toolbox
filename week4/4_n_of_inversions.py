import fileinput


def merge(l, r):
    res = []
    inv = 0
    i = 0
    j = 0
    while i < len(l) and j < len(r):
        if l[i] > r[j]:
            inv += len(l[i:])
            res.append(r[j])
            j += 1
        else:
            res.append(l[i])
            i += 1
    if i < len(l):
        res.extend(l[i:])
    if j < len(r):
        res.extend(r[j:])
    #print(f'l={l} r={r} inv={inv}')
    return res, inv


def merge_sort(a, n):
    if len(a) == 1:
        return a, 0
    l = a[:len(a)//2]
    r = a[len(a)//2:]
    l, ln = merge_sort(l, n)
    r, rn = merge_sort(r, n + ln)
    m, mn = merge(l, r)
    return m, mn + ln + rn


finput = fileinput.input()
n = int(next(finput))
a = [int(x) for x in next(finput).split()]

a, x = merge_sort(a, 0)
print(x)

