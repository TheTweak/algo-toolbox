import fileinput


def longest_common_subs(n: list, m: list, k: list) -> int:
    dp = [[[0 for _ in range(len(k)+1)] for _ in range(len(m)+1)] for _ in range(len(n)+1)]

    for i in range(1,len(n)+1):
        for j in range(1,len(m)+1):
            for l in range(1,len(k)+1):
                if n[i-1] == m[j-1] == k[l-1]:
                    dp[i][j][l] = dp[i-1][j-1][l-1] + 1
                else:
                    dp[i][j][l] = max(dp[i-1][j][l], dp[i][j-1][l], dp[i][j][l-1])

    return dp[-1][-1][-1]


if __name__ == '__main__':
    finput = fileinput.input()
    next(finput)
    n = [int(x) for x in next(finput).split()]
    next(finput)
    m = [int(x) for x in next(finput).split()]
    next(finput)
    k = [int(x) for x in next(finput).split()]
    print(longest_common_subs(n, m, k))
