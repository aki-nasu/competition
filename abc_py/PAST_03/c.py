a,r,n = map(int,input().split())
if r == 1: exit(print(a))
MAX = pow(10,9)
for i in range(n):
    if a*pow(r,i) > MAX: exit(print('large'))
print(a*pow(r,n-1))