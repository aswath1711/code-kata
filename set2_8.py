v,p=[int(x) for x in input().split()]
for n in range(v,p):
    s = 0
    temp = n
    while temp > 0:
        d = temp % 10
        s += d ** 3
        temp //= 10

    if n == s:
        print(n)