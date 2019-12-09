# 2019/12/7 15[m] 0WA
# 特別複雑なことはない。
n,l = map(int,input().split())
a = 0
for i in range(n):
    a += l + i
t = 0
u = 0
z = 999
ans = 0
for i in range(n):
    t = a - (l+i)
    u = abs(a - t)
    if z > u:
        z = u
        ans = t
print(ans)