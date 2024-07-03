for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    d = list()
    m = 0
    c = 0
    for i in range(n - 1):
        if a[i + 1] < a[i] + b[i]:
            b[i + 1] = a[i] + b[i] - a[i + 1]
    for i in b:
        if i:
            d.append(i)
    d.sort()

    for j in range(len(d)):
        if d[j] - m > 0:
            c += (len(d) - j + 1) * (d[j] - m)
            m = d[j]
    print(c)
