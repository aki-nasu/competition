n,t = map(int,input().split())
ans = 1001
for _ in range(n):
    c,tp = map(int,input().split())
    if tp > t: continue
    ans = min(ans, c)
print(ans if ans != 1001 else 'TLE')