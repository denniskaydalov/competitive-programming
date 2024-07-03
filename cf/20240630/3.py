for _ in range(int(input())):
    n = int(input())
    h = list(map(int, input().split()))
    m = h[n - 1]
    for i in range(n - 2, -1, -1):
        m = max(m + 1, h[i])
    print(m)





