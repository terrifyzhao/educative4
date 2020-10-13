def solve_knapsack(profits, weights, capacity):
    dp = [[0 for _ in range(capacity + 1)] for _ in range(len(profits))]

    for i in range(len(profits)):
        dp[i][0] = 0

    for j in range(capacity + 1):
        if j >= weights[0]:
            dp[0][j] = profits[0]

    for i in range(1, len(profits)):
        for j in range(1, capacity + 1):
            pro2 = 0
            pro1 = dp[i - 1][j]
            if j >= weights[i]:
                pro2 = profits[i] + dp[i - 1][j - weights[i]]
            dp[i][j] = max(pro1, pro2)

    return dp[-1][-1]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
