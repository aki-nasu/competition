# C - Alchemist
# https://atcoder.jp/contests/abc138/tasks/abc138_c
# 簡単すぎる・・・。
# 求めたい最大の値を得るのであれば、小さい順に足して2で割るを繰り返せばよい。
# 前半に登場した値は、その後ずっと1/2にされつづけるため小さくなる。であれば、
# 大きい値ほど最後にとっておいたほうが最終的な値は大きくなる。

# 23:03 - 23:11
n = int(input())
v = list(map(int,input().split()))
v.sort()
ans = (v[0]+v[1])/2
for i in range(2,n):
    ans = (ans+v[i])/2
print(ans)