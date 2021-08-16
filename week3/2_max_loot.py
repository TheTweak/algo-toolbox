import fileinput

finput = fileinput.input()
n, W = next(finput).split()
n, W = int(n), int(W)

items = []
for _ in range(n):
    v, w = next(finput).split()
    items.append((int(v), int(w)))

items.sort(key=lambda item: item[0]/item[1])

V = 0
while W > 0 and items:
    v, w = items.pop()
    if W >= w:
        V += v
        W -= w
    else:
        V += W*(v/w)
        break
print(V)
