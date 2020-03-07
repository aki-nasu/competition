h,n = map(int,input().split())
ab = [tuple(map(int,input().split())) for _ in range(n)]
dp = [10**8] * (h+1)
dp[0] = 0

for i in range(1,h+1):
    for a,b in ab:
        if i >= a:
            # HPより小さいとき、減らした後のHPに対して消費するMPを足す
            atk = b + dp[i-a]
            if atk < dp[i]:
                dp[i] = atk
        elif b < dp[i]:
            # どの攻撃よりも小さいHPであれば、一番MP消費が少ない攻撃のMPを記録する
            dp[i] = b
# 配列の最後が、求めたいHP
print(dp[-1])