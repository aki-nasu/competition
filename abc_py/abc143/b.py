# 22:00 - 22:09
# i+1からスタートするの、すぐに思いつかないといけない
n = int(input())
d = list(map(int,input().split()))
ans = 0
for i in range(n):
    for j in range(i+1,n):
        if i != j:
            ans += d[i] * d[j]
print(ans)