from collections import deque

def F(JC,d,c):
    prev = -1
    x = []
    while 0 < len(d):
        d_p = d.popleft()
        if d_p[1] >= prev:
            JC[d_p[0]] = c
            prev = d_p[2]
        else:
            x.append(d_p)
    return JC,deque(x)

ans = []

t = int(input())
for _ in range(t):
    n = int(input())
    jc = ['N']*n
    l = []
    for i in range(n):
        s,e = map(int,input().split())
        l.append((i,s,e))
    l = sorted(l,key=lambda x: x[2])
    l = deque(sorted(l,key=lambda x: x[1]))
    # print(l)
    jc,m = F(jc, l,'C')
    jc,z = F(jc, m, 'J')
    if len(z) > 0:
        ans.append('IMPOSSIBLE')
    else:
        ans.append(''.join(jc))

for i in range(t):
    print('Case #' + str(i+1) + ': ' + ans[i])