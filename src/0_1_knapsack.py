def knapsack(weights, values, total_weight):
    n = len(values)
    T = total_weight
    P = [[0 for j in range(T + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(T + 1):
            if i == 0 or j == 0:
                P[i][j] = 0
            else:
                if weights[i - 1] > j:
                    P[i][j] = P[i - 1][j]
                else:
                    P[i][j] = max(
                        P[i - 1][j - weights[i - 1]] + values[i - 1], P[i-1][j]
                    )

    return P[n][T]


if __name__ == "__main__":
    res = knapsack(weights=[1, 3, 4, 5], values=[1, 4, 5, 7], total_weight=7)
    import pdb; pdb.set_trace()