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

x = int(input())
if x == 1: exit(print(0,-1))
xp = set(prime_factorize(x))
for a in range(-1000000000,x):
    b = pow(-1,0.4) * a 
    if b-a == min(xp):
        exit(print(a,b))