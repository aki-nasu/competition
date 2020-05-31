a,b,n = map(int,input().split())
x = b-1 if b<=n else n
print((a*x)//b - a * (x//b))