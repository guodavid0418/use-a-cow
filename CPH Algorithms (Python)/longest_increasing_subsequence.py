n = int(input())

arr = list(map(int, input().split()))

length = [0] * n

for k in range(n):
    length[k] = 1
    for i in range(k):
        if arr[i] < arr[k]:
            length[k] = max(length[k], length[i] + 1)

print(max(length))