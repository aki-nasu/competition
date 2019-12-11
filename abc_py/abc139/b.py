# 12/11 15:50 give up
a,b = map(int,input().split())
ans = 1
t = a
while True:
    if t >= b:
        print(ans)
        exit(0)
    ans += 1
    t = t-1 + a
