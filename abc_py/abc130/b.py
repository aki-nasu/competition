# 2019/12/5 15[m] 1WA
# 負の整数があった場合のことが抜けていたためと推測する。
n,x = map(int,input().split())
l = list(map(int,input().split()))
ans = 1
d = 0
for i in range(n):
    d = d + l[i]
    if(d<=x):
        ans+=1
print(ans) 