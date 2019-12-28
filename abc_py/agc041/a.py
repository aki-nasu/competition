# 21:01
n,a,b = map(int,input().split())
if abs(b-a) % 2 == 0:
    print((b-a)//2)
else:
    ans = min(max(a-1,b-1),max(n-a,n-b))
    if (a-1) >= (n-b):
        t = (n-((n+1-b)+a))//2 + (n-b+1)
    else:
        t = (b-((a-1)+1)-1)//2 + (a-1+1)
    print(min(ans,t))