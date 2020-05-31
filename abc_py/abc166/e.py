n = int(input())
A = list(map(int,input().split()))

count = 0
for i in range(n):
    if A[i] == i: continue
    for j in range(i+1,n):
        if A[i]+A[j] == j-i: count += 1
print(count)