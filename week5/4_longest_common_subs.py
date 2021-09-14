import fileinput


def longest_common_subs(n: list, m: list) -> int:
    dp = [[0 for _ in range(len(m)+1)] for _ in range(len(n)+1)]

    for i in range(1,len(n)+1):
        for j in range(1,len(m)+1):
            if n[i-1] == m[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]


if __name__ == '__main__':
    finput = fileinput.input()
    next(finput)
    n = [int(x) for x in next(finput).split()]
    next(finput)
    m = [int(x) for x in next(finput).split()]
    print(longest_common_subs(n, m))
