n,a,b = map(int,input().split())
c,d = divmod(n,a+b)
print(a*c + min(a,d))