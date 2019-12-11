# 16:07 -16:19 11m
# 1度解いた問題。
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

bonus = 0
for i in range(1,n):
    if a[i]-a[i-1] == 1:
        bonus += c[a[i-1]-1]

print(sum(b) + bonus)

