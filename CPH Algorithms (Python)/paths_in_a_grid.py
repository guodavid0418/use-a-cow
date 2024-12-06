n = int(input())

value = [list(map(int, input().split())) for i in range(n)]

total = [[0] * n for i in range(n)]

for x in range(n):
    for y in range(n):
        total[x][y] = max(total[x - 1][y], total[x][y - 1]) + value[x][y]

print(total[n - 1][n - 1])