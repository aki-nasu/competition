# 22:12 - 22:24 12m
# あてずっぽうで書いたが、sum(w[:])みたいな書き方ができることを学んだ
n = int(input())
w = list(map(int,input().split()))
ans = abs(sum(w[:1]) - sum(w[1:]))
for i in range(2,n):
    if ans > abs(sum(w[:i]) - sum(w[i:])):
        ans = abs(sum(w[:i]) - sum(w[i:]))
print(ans)
