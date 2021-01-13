n = int(input())
A = list(map(int,input().split()))
if 0 in A: exit(print(0))
ans = 1
over = pow(10,18)
for i in range(n):
    ans *= A[i]
    if ans > over: exit(print(-1))
print(ans)