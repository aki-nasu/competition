n = int(input())
A = list(map(int,input().split()))
ans = [0]*(n+1)
for i in range(n-1):
    ans[A[i]]+=1

for i in range(1,n+1):
    print(ans[i])