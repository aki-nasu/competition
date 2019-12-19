# C - Maximal Value
# https://atcoder.jp/contests/abc140/tasks/abc140_c
# これも簡単。。minとるだけや。

# 0:50 - 0:58 事前にスマホで問題読んでる
n = int(input())
b = list(map(int,input().split()))
a = [0]*n
a[0] = b[0]
a[n-1] = b[n-2]
for i in range(1,n-1):
    a[i] = min(b[i],b[i-1])
print(sum(a))