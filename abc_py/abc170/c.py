x,n = map(int,input().split())
if n==0: exit(print(x))
p = list(map(int,input().split()))
p.sort()
if x not in p: exit(print(x))
h=101
l=0
for i in range(x,101):
    if i not in p:
        h = i
        break
for i in range(x,0,-1):
    if i not in p:
        l = i
        break
if abs(x-h)>=abs(x-l): print(l)
if abs(x-l)>abs(x-h): print(h)
