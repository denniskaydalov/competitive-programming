def rbin(a, x):
    l = -1
    r = len(a) 
    while r > l + 1:
        m = (l + r) // 2
        if a[m] < x:
            l = m
        else:
            r = m

    return r

def lbin(a, x):
    l = -1
    r = len(a) 
    while r > l + 1:
        m = (l + r) // 2
        if a[m] <= x:
            l = m
        else:
            r = m
    return l

n = int(input())
a = list(map(int, input().split()))
k = int(input())
a.sort()
for _ in range(k):
    l, r = map(int, input().split())
    print(lbin(a, r) - rbin(a, l) + 1, end=' ')

