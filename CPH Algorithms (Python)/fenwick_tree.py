n = int(input())

arr = list(map(int, input().split()))
arr.insert(0, 0)

tree = [0] * (n + 1)

def sum_q(k):
    s = 0
    while k >= 1:
        s += tree[k]
        k -= k&-k

    return s

def add(k, x):
    while k <= n:
        tree[k] += x
        k += k&-k

for k in range(1, n + 1):
    add(k, arr[k])

print(*tree)