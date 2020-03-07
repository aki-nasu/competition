n = int(input())
x = list(map(int,input().split()))

a = sum(x)//n

y,z = 0,0
for i in range(n):
    y += (a-x[i])**2
    z += ((a+1)-x[i])**2
print(min(y,z))