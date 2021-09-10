import fileinput


def get_edit_distance(a: str, b: str, i: int, j: int, dp: dict) -> int:
    if not (i, j) in dp:
        if i == 0:
            dp[(i, j)] = j
        elif j == 0:
            dp[(i, j)] = i
        else:
            diff = 0 if a[i-1] == b[j-1] else 1
            dp[(i, j)] = min(get_edit_distance(a, b, i, j-1, dp)+1,
                    get_edit_distance(a, b, i-1, j, dp)+1,
                    get_edit_distance(a, b, i-1, j-1, dp)+diff)
    return dp[(i, j)]


if __name__ == '__main__':
    finput = fileinput.input()
    a = next(finput)
    b = next(finput)
    print(get_edit_distance(a, b, len(a), len(b), {}))
