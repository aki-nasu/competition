t = int(input())
ans = [0]*t
for i in range(t):
    s = int(input())
    a = s
    while s >= 10:
        q,mod = divmod(s,10)
        a += q
        s = q + mod
    ans[i] = a

for i in range(t):
    print(ans[i])