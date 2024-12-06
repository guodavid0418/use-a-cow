n = int(input())

arr = list(map(int, input().split()))
arr.insert(0, 0)

tree = [0] * (2 * n)
for k in range(n):
    tree[k + n] = arr[k + 1]
for k in range(n - 1, 0, -1):
    tree[k] = tree[2 * k] + tree[2 * k + 1]

#bottom to top
def sum_q(a, b):
    a += n - 1
    b += n - 1
    s = 0
    while a <= b:
        if a % 2 == 1:
            s += tree[a]
            a += 1
        if b % 2 == 0:
            s += tree[b]
            b -= 1
        a //= 2
        b //= 2

    return s

#top to bottom
def sum_q2(a, b, k, x, y):
    if b < x or a > y:
        return 0
    if a <= x and y <= b:
        return tree[k]
    d = (x + y) // 2

    return sum_q2(a, b, 2 * k, x, d) + sum_q2(a, b, 2 * k + 1, d + 1, y)

def add(k, x):
    k += n - 1
    tree[k] += x
    k //= 2
    while k >= 1:
        tree[k] = tree[2 * k] + tree[2 * k + 1]
        k //= 2

print(*tree)