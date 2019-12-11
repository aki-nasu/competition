# 21:15 - 22:33
# 最小公倍数lcm、最大公約数gcdを用いた実装を経験
# 包除の原理を使って、足し引きしていく。
# 範囲指定がある場合は、F(X)関数をつくるとよい、ということを学ぶ。
# バージョンの都合で、AtCoder上ではfractionsとのこと。
import fractions as math

a,b,c,d = map(int,input().split())

def F(n,c,d):
    x = n
    x -= n//c
    x -= n//d
    lcm = c*d//math.gcd(c,d)
    x += n//lcm
    return x

print(F(b,c,d) - F(a-1,c,d))