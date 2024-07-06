m, n = map(int, input().split())
t = list()
z = list()
y = list()

def f(x):
    c = list()
    for i in range(n):
        c.append(0)
        e = t[i] * z[i] + y[i]
        if x >= e:
            c[i] += z[i] * (x // e)
        c[i] += min((x % e), t[i] * z[i]) // t[i]
    return sum(c), c


for _ in range(n):
    i, j, k = map(int, input().split())
    t.append(i)
    z.append(j)
    y.append(k)

l = 0
r = 10**9

while r > l + 1:
    mi = (l + r) // 2
    cs, ct = f(mi)
    if cs >= m:
        ll = ct
        r = mi
    else:
        l = mi


if m == 0:
    print(0)
    print(0)
else:
    if m != sum(ll):
        mi = sum(ll) - m
        for i in range(n):
            if ll[i] < mi:
                mi -= ll[i]
                ll[i] = 0
            else:
                ll[i] -= mi
                break
        
    print(r)
    print(*ll)
