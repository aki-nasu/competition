# C - City Savers
# https://atcoder.jp/contests/abc135/tasks/abc135_c
# 例題に救われただけでごり押し感が強い

# 22:22 - 23:02
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 0
for i in range(n):
    if b[i] > a[i]+a[i+1]:
        ans += a[i]+a[i+1]
        a[i+1] = 0
    else:
        ans += b[i]
        if a[i] - b[i] < 0:
            a[i+1] = a[i] + a[i+1] - b[i]
print(ans)