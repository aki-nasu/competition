# 12/10 22:42-22:50 AC 8m
# 逆数をこういうふうに書く以外に方法がある気がする
import numpy as np
n = int(input())
a = list(map(int,input().split()))
s = 0
for i in range(n):
    s += 1/a[i]
print(1/s)