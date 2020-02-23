from functools import reduce

n,a,b = map(int,input().split())
MOD = 1000000007

# nCr の計算
def F(n,r):
    # 分子 n*(n-1)*(n-2)*...(n-r+1)
    numerator = reduce(lambda x,y: x * y % MOD, range(n,n-r,-1))
    # 分母 r!(rの階乗)
    denominator = reduce(lambda x,y: x * y % MOD, range(1,r+1))
    return numerator * pow(denominator, MOD - 2, MOD) % MOD

# 繰り返し二乗法
ans = pow(2,n,MOD)-1
ans -=F(n,a)
ans -=F(n,b)
ans %= MOD

print(ans)