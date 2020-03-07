t = int(input())
ans = ['']*t
for i in range(t):
    a = int(input())
    l = list(map(int,input().split()))
    if sum(l) % 2 != 0:
        ans[i] = 'YES'
    else:
        ans[i] = 'NO'
for i in range(t):
    print(ans[i])