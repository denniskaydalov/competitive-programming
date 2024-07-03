for _ in range(int(input())):
    n = int(input())
    h = list(map(int, input().split()))
    b = [0] * n
    c = [0] * n

    while any(h):
        for i in range(n - 1):
            if h[i] <= h[i + 1]:
                b[i] = h[i + 1] - h[i] + 1

        for i in range(n - 2, -1, -1):
            if not b[i]:
                c[i] = h[i] - h[i + 1] + c[i + 1]

        m = float('inf')
        for i in range(n - 1):
            if b[i] and b[i] < h[i + 1]:
                m = min(m, b[i])

        for i in range(1, n):
            if c[i]:
                h[i - 1] = max(h[i - 1] - min(c[i], m), 0)

        print(h)


