import fileinput


def bin_search(arr, x, lo, hi):
    if lo > hi:
        return -1
    mid = (lo+hi)//2
    if x == arr[mid]:
        return mid
    elif x > arr[mid]:
        return bin_search(arr, x, mid+1, hi)
    else:
        return bin_search(arr, x, lo, mid-1)


finput = fileinput.input()
n = next(finput)
A = [int(a) for a in next(finput).split()]
m = next(finput)
B = [int(a) for a in next(finput).split()]

result = []
for b in B:
    result.append(bin_search(A, b, 0, len(A)-1))

print(*result)

