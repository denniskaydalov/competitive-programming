def f(w, h, n, x):
    return (x // w) * (x // h) >= n
w, h, n = map(int, input().split())
l = 0
r = 1
while not f(w, h, n, r):
    r *= 2
while r > l + 1:
    m = (r + l) // 2
    if f(w, h, n, m):
        r = m
    else:
        l = m
print(r)

