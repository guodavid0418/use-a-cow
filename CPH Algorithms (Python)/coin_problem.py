n = int(input())

coins = list(map(int, input().split()))

INF = 2 ** 31 - 1

value = [INF] * (n + 1)
value[0] = 0

for x in range(1, n + 1):
    for c in coins:
        if x - c >= 0:
            value[x] = min(value[x], value[x - c] + 1)

print(value[n])