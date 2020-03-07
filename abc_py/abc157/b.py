a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))
a3 = list(map(int,input().split()))
t1 = [0,0,0]
t2 = [0,0,0]
t3 = [0,0,0]
n = int(input())
for _ in range(n):
    b = int(input())
    for i in range(3):
        if a1[i]==b: t1[i]=1
        if a2[i]==b: t2[i]=1
        if a3[i]==b: t3[i]=1

l=[1,1,1]
if t1==l or t2==l or t3==l:
    print('Yes')
    exit(0)
if [t1[0],t2[0],t3[0]]==l or [t1[1],t2[1],t3[1]]==l or [t1[2],t2[2],t3[2]]==l:
    print('Yes')
    exit(0)
if [t1[0],t2[1],t3[2]]==l or [t1[2],t2[1],t3[0]]==l:
    print('Yes')
    exit(0)
print('No')