import fileinput


def bin_search(arr, x):
    if not arr:
        return -1
    m = len(arr)//2
    if arr[m] == x:
        return m
    if arr[m] < x:
        return bin_search(arr[m+1:], x)
    else:
        return bin_search(arr[:m], x)


finput = fileinput.input()
A = [int(a) for i, a in enumerate(next(finput).split()) if i > 0]
B = [int(a) for i, a in enumerate(next(finput).split()) if i > 0]

result = []
for b in B:
    result.append(bin_search(A, b))

print(' '.join([str(i) for i in result]))
