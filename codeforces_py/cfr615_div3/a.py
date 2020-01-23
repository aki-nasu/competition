t = int(input())
ans = ['']*t
for i in range(t):
    a,b,c,n = map(int,input().split())
    l = sorted([a,b,c],reverse=True)
    n -= ((l[0]-l[1])+(l[0]-l[2]))
    if n >= 0 and n % 3 == 0:
        ans[i] = 'YES'
    else:
        ans[i] = 'NO'
for i in range(t):
    print(ans[i])