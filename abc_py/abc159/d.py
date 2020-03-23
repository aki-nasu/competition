n = int(input())
A = list(map(int,input().split()))
total=[0]*n
k = []
for i in range(n):
    t = [0]*n
    for j in range(i+1,n):
        if A[i]==A[j]: t[j]=1
    k.append(t)
    total = list(map(sum, zip(total, t)))
for i in range(n):
    print(sum(total)-total[i]-sum(k[i]))