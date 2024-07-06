n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list()
l = 0
r = 0
while l < n or r < m:
    if l == n:
        c.append(b[r])
        r += 1
    elif r == m:
        c.append(a[l])
        l += 1
    else:
        if a[l] < b[r]:
            c.append(a[l])
            l += 1
        else:
            c.append(b[r])
            r += 1
print(*c)
