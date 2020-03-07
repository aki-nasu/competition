N,W = map(int,input().split())
wv = [tuple(map(int,input().split())) for _ in range(N)]

dp = [0]*(W+1)
for i in range(1,W+1):
    for w,v in wv:
        if w <= i:
            total_value = v + dp[i-w]
            if total_value > dp[i]:
                dp[i] = total_value
print(dp)