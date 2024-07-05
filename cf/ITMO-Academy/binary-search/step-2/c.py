n, x, y = map(int, input().split())
n -= 1
l = 0
r = n * max(x, y)
while r > l + 1:
    m = (r + l) // 2
    if m // x + m // y >= n:
        r = m
    else:
        l = m
print(r + min(x, y))

