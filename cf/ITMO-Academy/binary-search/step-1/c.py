def bin(a, x):
    l = -1
    r = len(a) 
    while r > l + 1:
        m = (l + r) // 2
        if a[m] < x:
            l = m
        else:
            r = m
    return r + 1

n, k = [int(i) for i in input().split()]
N = [int(i) for i in input().split()]
K = [int(i) for i in input().split()]
for i in K:
    print(bin(N, i))
