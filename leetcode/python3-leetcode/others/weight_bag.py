def test_2_wei_bag_problem1():
    weight = [4, 5, 6]
    value = [15, 20, 30]
    bagweight = 11

    dp = [[0] * (bagweight + 1) for _ in range(len(weight))]

    for j in range(weight[0], bagweight + 1):
        dp[0][j] = value[0]

    # weight数组的大小就是物品个数
    for i in range(1, len(weight)):  # 遍历物品
        for j in range(bagweight + 1):  # 遍历背包容量
            if j < weight[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])

    print(dp[len(weight) - 1][bagweight])


def test_bag2():
    weight = [4, 5, 6]
    value = [15, 20, 30]
    n = len(weight)
    bagweight = 11

    dp = [[0] * (bagweight + 1) for _ in range(n)]

    # while j = 0, value = 0
    for i in range(n):
        dp[i][0] = 0

    for i in range(weight[0], bagweight + 1):
        dp[0][i] = value[0]

    for i in range(1, n):
        for j in range(1, bagweight + 1):
            if weight[i] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])

    return dp[n - 1][bagweight]


def test_bag1():
    weight = [5, 1, 3]
    value = [15, 20, 30]
    bagWeight = 4

    # 初始化
    dp = [0] * (bagWeight + 1)
    for i in range(len(weight)):  # 遍历物品
        for j in range(bagWeight, weight[i] - 1, -1):  # 遍历背包容量
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

    print(dp[bagWeight])


test_bag1()
