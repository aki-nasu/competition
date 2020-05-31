
# t = int(input())
# ans = []
# for i in range(t):
#     n,a,b,c,d = list(map(int,input().split()))
#     coin = 0
#     p = 1
#     while True:
#         ap = p*2


N2 = [pow(2,i) for i in range(1,61)]
N3 = [pow(3,i) for i in range(1,39)]
N5 = [pow(5,i) for i in range(1,26)]

import numpy as np


def getNearestValue(list, num):
    idx = np.abs(np.asarray(list) - num).argmin()
    return list[idx]


def F(n, f):
    ret = divmod(n, f)
    if abs(n - ((ret[0]+1)*f)) < ret[1]: ret = (ret[0]+1, abs(n-((ret[0]+1)*f)))
    return ret

t = int(input())
ans = []
for i in range(t):
    n,a,b,c,d = list(map(int,input().split()))
    a1,a2 = divmod(n, 2)
    at = a1*a+d
    b1,b2 = divmod(n, 3)
    bt = b1*b
    if b2 == 1: bt += d
    if b2 == 2: bt += min(2*d,a) 
    c1,c2 = divmod(n, 5)
    ct = c1*c
    if c2 == 1: ct += d
    if c2 == 2: ct += min(2*d,a)
    if c2 == 3: ct += min(3*d,a+d,b)
    if c2 == 4: ct += min(4*d,2*a,b+d,c+d)
    print(at,bt,ct)
    print(min(at,bt,ct))
    ans.append(min(at,bt,ct)+d)

for i in range(t): print(ans[i])
