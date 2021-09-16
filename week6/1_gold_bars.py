import fileinput


def get_max_score(W: int, N: list) -> int:
    c = len(N)+1
    r = W+1
    dp = [[0 for _ in range(c)] for _ in range(r)]
    for w in range(1, r):
        for i in range(1, c):
            n = N[i-1]
            s = w-n
            if s >= 0:
                dp[w][i] = max(dp[w][i-1], dp[s][i]+n)
            else:
                dp[w][i] = dp[w][i-1]

    return dp[-1][-1]


if __name__ == '__main__':
    finput = fileinput.input()
    W = int(next(finput).split()[0])
    N = [int(x) for x in next(finput).split()]
    print(get_max_score(W, N))

