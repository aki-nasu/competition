n,m = map(int,input().split())
a = list(map(int,input().split()))
a = sorted(a,reverse=True)
max_num = a.pop(0)
i  = 0
while True:
    i += 1
    x = max_num * (i * 0.5)
    if x > m:
        break
    for i in range(n):
        a[i]