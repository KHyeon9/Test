i = 0
while 1:
    i += 1
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break
    r = (v // p) * l
    r2 = v - (v // p * p)
    if r2 > l:
        r += l
    else:
        r += r2
    print(f"Case {i}: {r}")



