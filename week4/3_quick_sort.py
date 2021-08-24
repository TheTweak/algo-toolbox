import fileinput
import random


def partition(a, l, r):
    j = l
    pivot = a[l]
    for i in range(l+1, r+1):
        if a[i] <= pivot:
            j += 1
            a[j], a[i] = a[i], a[j]
    a[l], a[j] = a[j], a[l]
    return j


def quick_sort(a, l, r):
    if l >= r:
        return
    m = partition(a, l, r)
    quick_sort(a, l, m-1)
    quick_sort(a, m+1, r)


finput = fileinput.input()
n = int(next(finput))
a = [int(x) for x in next(finput).split()]

quick_sort(a, 0, len(a)-1)

print(' '.join([str(x) for x in a]))
