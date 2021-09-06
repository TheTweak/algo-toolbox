import sys


def distance(p1: (int, int), p2: (int, int)) -> int:
    return (p1[0]-p2[0])**2+(p1[1]-p2[1])**2


def closest_points(x: list, y: list) -> int:
    if len(x) == 1:
        return float('inf')
    if len(x) == 2:
        return distance(p1=(x[0],y[0]), p2=(x[1],y[1]))

    # split the points into two halves
    m = len(x)//2
    left_x, left_y = x[:m], y[:m]
    right_x, right_y = x[m:], y[m:]

    d1 = closest_points(left_x, left_y)
    d2 = closest_points(right_x, right_y)
    d = min(d1, d2)

    # filter out points from initial set xy
    # that lie within distance d to the middle
    xy = zip(x, y)
    within_d = filter(lambda p: distance(p, (x[m], p[1])) <= d, xy)
    # sort these points by y coordinate
    within_d = sorted(within_d, key=lambda p: p[1])
    # for each of these points, compute its distance to
    # 7 next points (d'), and update d=min(d, d')
    for i in range(len(within_d)):
        for j in range(i+1, min(i+8, len(within_d))):
            d_ = distance(within_d[i], within_d[j])
            d = min(d_, d)
    return d


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    xy = zip(x, y)
    xy = sorted(xy, key=lambda a: a[0])
    x, y = zip(*xy)
    print(closest_points(x, y)**0.5)

