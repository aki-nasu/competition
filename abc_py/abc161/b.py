n,m = map(int,input().split())
a = list(map(int,input().split()))
a = sorted(a,reverse=True)
t = sum(a)

for i in range(m):
    if a[i]*(4*m) < t:
        print('No')
        exit(0)
print('Yes')