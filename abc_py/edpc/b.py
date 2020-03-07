n,k = map(int,input().split())
h = list(map(int,input().split()))

dp = [10**9]*(n+1)
dp[0] = 0
for i in range(1,n):
    K = k if i >= k else i
    for j in range(1,K+1):
        t = dp[i-j] + abs(h[i-j]-h[i])
        if dp[i] > t:
            dp[i] = t
# print(dp)
print(dp[n-1])