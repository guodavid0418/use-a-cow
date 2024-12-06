n, m = map(int, input().split())

edges = [list(map(int, input().split())) for i in range(m)]

edges = sorted(edges, key = lambda x: x[2])

link = [i for i in range(n + 1)]
size = [1 for i in range(n + 1)]

def find(x):
    global link

    while x != link[x]:
        link[x] = link[link[x]]
        x = link[x]
    return x

def same(a, b):
    global link

    return find(a) == find(b)

def unite(a, b):
    global link
    global size

    a = find(a)
    b = find(b)
    if size[a] < size[b]:
        a, b = b, a
    size[a] += size[b]
    link[b] = a

weight = 0
for e in edges:
    a = e[0]
    b = e[1]
    w = e[2]
    if not same(a, b):
        unite(a, b)
        weight += w

print(weight)