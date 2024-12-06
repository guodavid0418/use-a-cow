n = int(input())

adj = [list(map(int, input().split())) for i in range(n)]

INF = 2 ** 31 - 1
distance = [[INF] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            distance[i][j] = 0
        elif adj[i][j]:
            distance[i][j] = adj[i][j]

for k in range(n):
    for i in range(n):
        for j in range(n):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

for i in distance:
    print(*i)