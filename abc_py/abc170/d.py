n = int(input())
a = list(map(int,input().split()))
a = sorted(a)
count = 0
bl = []
for i in range(n):
    t = a[i]
    count+=1
    if i+1!=n:
        if t==a[i+1]:
            count-=1
            bl.append(i)
            continue
    if i!=0:
        if t==a[i-1]:
            count-=1
            bl.append(i)
            continue
    for j in range(i):
        if j in bl: continue
        if t%a[j]==0:
            count-=1
            bl.append(i)
            break
print(count)

TLE