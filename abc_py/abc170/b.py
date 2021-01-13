x,y = map(int,input().split())
k = x*4
if k < y: exit(print('No'))
if k == y: exit(print('Yes'))

for i in range(x):
    k -= 2
    if k == y: exit(print('Yes'))
print('No')