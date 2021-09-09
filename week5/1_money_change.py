import fileinput


def get_change(money: int) -> int:
    coins = [1, 3, 4]
    dp = [0] * (money+1)
    for m in range(1, money+1):
        new_sol = float('inf')
        for c in coins:
            if m-c == 0:
                sol = dp[m-1]+1
                new_sol = 1
            elif m-c > 0:
                sol = dp[m-c]+1
                new_sol = min(new_sol, sol)
        dp[m] = new_sol
    return dp[-1]


if __name__ == '__main__':
    money = int(next(fileinput.input()))
    print(get_change(money))

