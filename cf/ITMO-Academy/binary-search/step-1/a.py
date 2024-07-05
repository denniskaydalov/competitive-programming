def bin(a, x):
    l = 0
    r = len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            return m
        elif a[m] < x:
            l = m + 1
        else:
            r = m - 1
    return len(a)

n, k = [int(i) for i in input().split()]
N = [int(i) for i in input().split()]
K = [int(i) for i in input().split()]
for i in K:
    if bin(N, i) == n:
        print('NO')
    else:
        print('YES')
