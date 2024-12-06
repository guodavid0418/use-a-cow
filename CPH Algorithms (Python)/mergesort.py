n = int(input())

arr = list(map(int, input().split()))

def mergesort(arr):
    if len(arr) > 1:
        m = len(arr) // 2

        l = arr[:m]
        r = arr[m:]

        mergesort(l)
        mergesort(r)

        i = 0
        j = 0
        k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1

mergesort(arr)
print(*arr)