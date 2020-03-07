n,m,c = map(int,input().split())
b = list(map(int,input().split()))
count = 0
for i in range(n):
    a = list(map(int,input().split()))
    t = 0
    for j in range(m):
        t += a[j]*b[j]
    t += c
    if t>0: count+=1
print(count)