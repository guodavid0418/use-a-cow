n, W = map(int, input().split())

v = list(map(int, input().split()))
w = list(map(int, input().split()))

def knapsack(n, W, v, w):
    t = []
    for i in range(n + 1):
        row = []
        for j in range(W + 1):
            row.append(-1)
        t.append(row)

    for j in range(W + 1):
        t[0][j] = 0

    for i in range(1, n + 1):
        for j in range(W + 1):
            if w[i - 1] > j:
                t[i][j] = t[i - 1][j]
            else:
                t[i][j] = max(t[i - 1][j], t[i - 1][j - w[i - 1]] + v[i - 1])

    return t[n][W]

print(knapsack(n, W, v, w))