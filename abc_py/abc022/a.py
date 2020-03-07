n,s,t = map(int,input().split())
x = int(input())
ans = 1 if s<=x and x<=t else 0
for i in range(1,n):
    x = x + int(input())
    ans += 1 if s<=x and x<=t else 0
print(ans)