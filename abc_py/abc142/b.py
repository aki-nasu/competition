# 21:56 - 21:59 3m
# for文があるからB問題だけど、内容はA問題レベルということなのか？
n,k = map(int,input().split())
h = list(map(int,input().split()))
ans = 0
for i in range(n):
    ans += 1 if h[i] >= k else 0
print(ans)