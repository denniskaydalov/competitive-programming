n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [0] * m
l = 0
r = 0
while l < n or r < m:
    if l == n or b[r] <= a[l]:
        r += 1
        if r == m:
            break
        c[r] = c[r - 1]
    else:
        c[r] += 1
        l += 1
print(*c)
