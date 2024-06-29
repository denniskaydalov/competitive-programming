c = [15, 10, 6, 3, 1]
o = [0] + [float('inf')] * (15 * 10 * 6 * 3)
for i in range(0, len(o)):
    for j in c:
        if i - j >= 0:
            o[i] = min(o[i], o[i - j] + 1)

for _ in range(int(input())):
    n = int(input())
    d = 0
    if n > 15 * 10 * 6 * 3:
        t = n // 15 - 1
        d += t
        n -= t * 15

    if n > 0:
        d += o[n]
        n = 0

    print(d)
