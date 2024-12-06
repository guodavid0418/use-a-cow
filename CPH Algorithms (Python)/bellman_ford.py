n, m, x = map(int, input().split())

edges = [list(map(int, input().split())) for i in range(m)]

INF = 2 ** 31 - 1
distance = [INF] * (n + 1)
distance[x] = 0

for i in range(n - 1):
    for e in edges:
        a = e[0]
        b = e[1]
        w = e[2]
        distance[b] = min(distance[b], distance[a] + w)

print(*distance)