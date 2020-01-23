t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    p = []
    p.append((0,0))
    for _ in range(n):
        x,y = map(int,input().split())
        p.append((x,y))
    p.sort()
    route = ''
    X,Y = 0,0
    for i in range(1,n+1):
        X = p[i][0] - p[i-1][0]
        Y = p[i][1] - p[i-1][1]
        if X < 0 or Y < 0:
            route = ''
            break
        route += 'R'*X + 'U'*Y
    if route == '':
        ans.append('NO')
    else:
        ans.append('YES')
        ans.append(route)
for i in range(len(ans)):
    print(ans[i])