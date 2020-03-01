n,m = map(int,input().split())
t='000'
if n==2: t='010'
if n==3: t='100'
f=[0]*len(t)
t=[int(t[0]),int(t[1]),int(t[2])]
ans = t[0]*100+t[1]*10+t[2] 
for i in range(m):
    ans = -1
    s,c = map(int,input().split())
    s=s-(n-2)
    if c <  t[s]: break
    if c >  t[s]:
        if f[s]==0:
            f[s],t[s]=1,c
        elif f[s]==1:
            break
    ans=t[0]*100+t[1]*10+t[2]
print(ans)