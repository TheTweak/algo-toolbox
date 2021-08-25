import fileinput
import random


def partition(a, l, r):
    j = l
    j_ = l
    k = l
    pivot = a[l]
    for i in range(l+1, r+1):
        if a[i] == pivot:
            j_ += 1
            a[j_], a[i] = a[i], a[j_]
        if a[i] <= pivot:
            j += 1
            a[j], a[i] = a[i], a[j]
    m_size = j_
    while j_ >= l:
        a[j_], a[j] = a[j], a[j_]
        j_ -= 1
        j -= 1
    return j+1, j+1+m_size


def quick_sort(a, l, r):
    if l >= r:
        return
    m1, m2 = partition(a, l, r)
    quick_sort(a, l, m1-1)
    quick_sort(a, m2+1, r)

finput = fileinput.input()
n = int(next(finput))
a = [int(x) for x in next(finput).split()]

quick_sort(a, 0, len(a)-1)

print(' '.join([str(x) for x in a]))
