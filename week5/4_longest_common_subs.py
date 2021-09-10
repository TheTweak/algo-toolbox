import fileinput


def longest_common_subs(n: list, m: list) -> int:
    dp = [[0]*len(m) for _ in range(len(n))]

    dp[0][0] = 1 if n[0] == m[0] else 0
    for row in range(1, len(n)):
        dp[row][0] = max(1 if n[row] == m[0] else 0, dp[row-1][0])
    for col in range(1, len(m)):
        dp[0][col] = max(1 if n[0] == m[col] else 0, dp[0][col-1])

    for row in range(1, len(n)):
        for col in range(1, len(m)):
            diff = 1 if n[row] == m[col] else 0
            dp[row][col] = max(dp[row-1][col], dp[row][col-1], dp[row-1][col-1]+diff)

    return dp[-1][-1]


if __name__ == '__main__':
    finput = fileinput.input()
    next(finput)
    n = [int(x) for x in next(finput).split()]
    next(finput)
    m = [int(x) for x in next(finput).split()]
    print(longest_common_subs(n, m))
