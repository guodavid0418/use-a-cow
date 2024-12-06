k, n = map(int, input().split())

price = [list(map(int, input().split())) for i in range(k)]

INF = 2 ** 31 - 1

def optimal_selection(k, n, price):
    total = []
    for i in range(1 << k):
        row = []
        for j in range(n):
            row.append(INF)
        total.append(row)
    
    for x in range(k):
        total[1 << x][0] = price[x][0]

    for d in range(1, n):
        for s in range(1 << k):
            total[s][d] = total[s][d - 1]
            for x in range(k):
                if s & (1 << x):
                    total[s][d] = min(total[s][d], total[s ^ (1 << x)][d - 1] + price[x][d])

    return total[s][d]

print(optimal_selection(k, n, price))