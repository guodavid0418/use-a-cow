import heapq

n, m, x = map(int, input().split())

adj = []
for i in range(n + 1):
    adj.append([])

for i in range(m):
    a, b, w = map(int, input().split())
    adj[a].append([b, w])

INF = 2 ** 31 - 1
distance = [INF] * (n + 1)
distance[x] = 0

processed = [False] * (n + 1)

q = []
heapq.heappush(q, [0, x])
while q:
    a = heapq.heappop(q)[1]
    if processed[a]:
        continue
    processed[a] = True

    for u in adj[a]:
        b = u[0]
        w = u[1]
        if distance[a] + w < distance[b]:
            distance[b] = distance[a] + w
            heapq.heappush(q, [distance[b], b])

print(*distance)