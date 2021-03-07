import copy
n = int(input())
l = []
for i in range(n):
    a,b = map(int,input().split())
    l.append((a,b))
m = copy.deepcopy(l)
l.sort(key=lambda x : x[0])
m.sort(key=lambda x : x[1])
# print(l,m)
# print(l[0]==m[0])

if l[0]==m[0]:
    sum = l[0][0] + l[0][1]
    p,q = l[1][0], m[1][1]
    if sum <= p and sum <= q:
        exit(print(sum))
    if p < q:
        exit(print(max(p, m[0][1])))
    else:
        exit(print(max(l[0][0], q)))
else:
    exit(print(max(l[0][0], m[0][1])))