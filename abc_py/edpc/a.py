# EDPCは、下記のDP専門ｺﾝﾃｽﾄ
# https://atcoder.jp/contests/dp

n = int(input())
h = list(map(int,input().split()))
dp = [10**4] * (n+1)
dp[0] = 0
dp[1] = abs(h[1]-h[0])
for i in range(2,n):
    dp[i] = min(dp[i-2] + abs(h[i-2] - h[i]), dp[i-1] + abs(h[i-1] - h[i]))
# print(dp)
print(dp[n-1])