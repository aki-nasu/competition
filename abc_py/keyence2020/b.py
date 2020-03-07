n = int(input())
l = []
for i in range(n):
    l.append(tuple(map(int,input().split())))
l = sorted(l)
ans = n
for i in range(n-1):
    L = l[i][0]+l[i][1]
    R = l[i+1][0]-l[i+1][1]
    if L > R:
        ans -= 1
        if i+2 < n:
            R2 = l[i+2][0]-l[i+2][1]
            if L <= R2:
                l[i+1] = l[i]
        else:
            l[i+1] = l[i]
print(ans)