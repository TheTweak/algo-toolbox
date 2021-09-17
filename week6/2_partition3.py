import fileinput

def part3(arr: list) -> int:
    s = sum(arr)
    if s % 3:
        return 0
    dp = [[0 for _ in range(s+1)] for _ in range(s+1)]
    dp[0][0] = 1
    for n in arr:
        for i in range(s, -1, -1):
            for j in range(s, -1, -1):
                if dp[i][j]:
                    dp[i+n][j] = 1
                    dp[i][j+n] = 1
    return dp[s//3][s//3]


if __name__ == '__main__':
    finput = fileinput.input()
    next(finput)
    N = [int(x) for x in next(finput).split()]
    print(part3(N))

