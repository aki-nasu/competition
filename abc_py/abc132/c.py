# 22:39 - 23:06
n = int(input())
d = list(map(int,input().split()))
d.sort()
print(d[n//2] - d[n//2-1])