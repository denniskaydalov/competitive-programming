import math

def bin(a, k):
    l = 0
    r = 10**8
    for i in range(75):
        m = (r + l) / 2
        if sum([math.floor(i / m) for i in a]) >= k:
            l = m
        else:
            r = m
    return l

n, k = map(int, input().split())
a = list()
for i in range(n):
    a.append(int(input()))

p = bin(a, k)

print(round(p, 7))



