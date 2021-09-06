import sys


def distance(p1: (int, int), p2: (int, int)) -> float:
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5


def get_middle(x: list) -> float:
    m = len(x)//2
    x1 = x[m-1]
    x2 = x[m]
    return x1+(x2-x1)/2


def closest_points(x: list, y: list) -> float:
    if len(x) == 1:
        return float('inf')
    if len(x) == 2:
        return distance(p1=(x[0],y[0]), p2=(x[1],y[1]))

    xy = zip(x, y)
    xy = sorted(xy, key=lambda a: a[0])
    x, y = zip(*xy)

    # split the points into two halves
    # by drawing vertical line in the middle
    middle = get_middle(x)
    left_side = filter(lambda p: p[0] <= middle, xy)
    left_x, left_y = zip(*left_side)
    right_side = filter(lambda p: p[0] > middle, xy)
    right_x, right_y = zip(*right_side)

    d1 = closest_points(left_x, left_y)
    d2 = closest_points(right_x, right_y)
    d = min(d1, d2)

    # filter out points from initial set xy
    # that lie within distance d to the middle
    within_d = filter(lambda p: distance(p, (middle, p[1])) <= d, xy)
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
    print(closest_points(x, y))
