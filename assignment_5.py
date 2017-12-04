def partition_set_solver(S):
    total = sum(S)

    if total & 1 == 1:
        return False

    total >>= 1
    n = len(S) + 1

    dp = [[False for i in range(total + 1)] for j in range(n)]

    for i in range(n):
        dp[i][0] = True

    for i in range(1, n):
        for j in range(1, total + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= S[i - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j - S[i - 1]]

    return dp[n - 1][total]


def subset_sum_solver(S, n):
    total = sum(S)
    if n > total:
        return False

    S1 = total + n
    S2 = 2 * total - n
    S.append(S1)
    S.append(S2)

    return partition_set_solver(S)


if __name__ == '__main__':
    print(subset_sum_solver([21, 10, 4, 500, 67], 3))
