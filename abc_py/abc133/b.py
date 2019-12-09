# 2019/12/7 45[m] 0WA
# 2次元配列的な記法を覚えた。
# pow:累乗、math.sqrtを使用。
# 一時的に使用する変数を初期化していないという凡ミスで時間がかかった。
import math

n,d = map(int,input().split())
p = []
for i in range(n):
    p.append(list(map(int,input().split())))

ans = 0
for i in range(n):
    for j in range(n):
        t0 = 0
        for k in range(d):
            t0 += pow(p[i][k]-p[j][k],2)
        t  = math.sqrt(t0)
        if t.is_integer() and t != 0:
            ans += 1
print(ans//2)