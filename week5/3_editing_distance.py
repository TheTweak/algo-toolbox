import fileinput
from collections import defaultdict


def get_edit_distance(a: str, b: str) -> int:
    def default_dp():
        return float('inf')
    dp = defaultdict(default_dp)
    for i in range(len(a)):
        dp[(i, 0)] = i
    for j in range(len(b)):
        dp[(0, j)] = j

    for i in range(1, len(a)):
        for j in range(1, len(b)):
            diff = 0 if a[i-1] == b[j-1] else 1
            dp[(i, j)] = min(dp[i, j-1]+1,
                    dp[i-1, j]+1,
                    dp[i-1, j-1]+diff)
    return dp[(i, j)]


if __name__ == '__main__':
    finput = fileinput.input()
    a = next(finput)
    b = next(finput)
    print(get_edit_distance(a, b))
