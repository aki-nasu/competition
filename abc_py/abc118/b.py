n,m = map(int,input().split())
count = [0]*(m+1)
for _ in range(n):
    a = list(map(int,input().split()))
    for i in range(1,a[0]+1): count[a[i]] += 1
ans = 0
for i in range(1,m+1):
    if count[i] == n: ans += 1
print(ans)