# A. Minutes Before the New Year
t = int(input())
ans = [0]*t
for i in range(t):
    h,m = map(int,input().split())
    h = 23-h
    m = 60-m
    ans[i] = (h*60) + m
for i in range(t):
    print(ans[i])
