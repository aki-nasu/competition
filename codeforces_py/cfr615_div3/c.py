def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
# import numpy as np
t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    l = prime_factorize(n)
    L = l[0]
    R = l[-1]
    if L == R and len(l) > 3:
        R *= l[-2]
        l.pop(-1)
    if len(l) >=3 and L != R:
        # prod = np.prod(l[1:-1])
        prod = 0
        for i in range(len(l[1:-1])):
            prod = prod*(l[1+i]) if prod != 0 else l[1]
        if prod != L and prod != R:
            ans.append('YES')
            ans.append(str(L) + ' ' + str(prod) + ' ' + str(R))
        else:
            ans.append('NO')
    else:
        ans.append('NO')
for i in range(len(ans)):
    print(ans[i])