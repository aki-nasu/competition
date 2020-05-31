def F(k):
    ans = 1
    for _ in range(k): ans = A[ans-1]
    return ans

n,k = map(int,input().split())
A = list(map(int,input().split()))

dp = [0]*n
if A[0] == 1: exit(print(1))

p = A[0]-1
dp[0]+=1
count = 1
stop = False
while True:
    if p == A[p]-1:
        stop = True
        break
    p = A[p]-1
    if dp[p] > 0:
        count += 1
        break
    count += 1
    dp[p]+=count
dp[0]=0
if (stop and k >= count) or k == count: exit(print(p+1))
if k > count: k = k % (count-dp[p])

print(F(k))