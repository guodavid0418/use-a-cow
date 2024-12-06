n, x = map(int, input().split())

weight = list(map(int, input().split()))

best = [[n + 1, 0] for i in range(1 << n)]
best[0] = [1, 0]

for s in range(1, 1 << n):
    for p in range(n):
        if s & (1 << p):
            option = best[s ^ (1 << p)].copy()

            if option[1] + weight[p] <= x:
                option[1] += weight[p]
            else:
                option[0] += 1
                option[1] = weight[p]

            best[s] = min(best[s], option)

print(best[s][0])