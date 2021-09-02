import fileinput


def partition(a, l, r):
    j = l
    j_ = l
    pivot = a[l]
    for i in range(l+1, r+1):
        if a[i] <= pivot:
            j_ += 1
            if a[i] < pivot:
                j += 1
                a[i], a[j] = a[j], a[i]
            if a[i] == pivot:
                a[i], a[j_] = a[j_], a[i]
    a[l], a[j] = a[j], a[l]
    return j, j_


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

print(*a)
