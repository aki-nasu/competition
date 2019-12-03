a,b = map(int,input().split())
l = a+b
m = a-b
n = a*b
x = m if l<=m else l
print(n if x<=n else x)
