# 15:18 - giveup
n,m = map(int,input().split())
a = [0]*(n+1)
for _ in range(m):
    a[int(input())] = 1
ans = 1
for i in range(n-1):
    if a[i] == 1: continue
    if a[i+1] == 1 and a[i+2] == 1: print(0),exit(0)
    if a[i+1] == 0 and a[i+2] == 0: ans *= 2
print(ans%(10**9+7))