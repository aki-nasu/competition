# C - Lower
# https://atcoder.jp/contests/abc139/tasks/abc139_c
# え、これも簡単すぎる。。TLEになるかとおもた。

# 0:30 - 0:39
n = int(input())
h = list(map(int,input().split()))

ans = 0
count = 0
for i in range(n-1):
    if h[i] >= h[i+1]:
        count += 1
        if count > ans:
            ans  = count
    else:
        count = 0
if count > ans:
    ans = count
print(ans)