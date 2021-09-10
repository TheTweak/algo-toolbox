import fileinput


def get_ops_n(n: int) -> int:
    dp = [float('inf')] * (n+1)
    dp[1] = 0
    for i in range(2, n+1):
        plus_one = dp[i-1]+1
        mult_two = float('inf') if i%2 else dp[i//2]+1
        mult_three = float('inf') if i%3 else dp[i//3]+1
        dp[i] = min(plus_one, mult_two, mult_three)
    return dp[-1]


if __name__ == '__main__':
    n = int(next(fileinput.input()))
    print(get_ops_n(n))
