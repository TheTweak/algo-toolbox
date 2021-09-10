import fileinput


def get_ops_n(n: int) -> int:
    dp = [(float('inf'), [])] * (n+1)
    dp[1] = (0, [1])
    for i in range(2, n+1):
        plus_one = dp[i-1]
        mult_two = (float('inf'), []) if i%2 else dp[i//2]
        mult_three = (float('inf'), []) if i%3 else dp[i//3]
        variants = sorted([plus_one, mult_two, mult_three], key=lambda x: x[0])
        opt_var = variants[0]
        dp[i] = (opt_var[0]+1, opt_var[1]+[i])
    return dp[-1]


if __name__ == '__main__':
    n = int(next(fileinput.input()))
    x, path = get_ops_n(n)
    print(x)
    print(*path)
