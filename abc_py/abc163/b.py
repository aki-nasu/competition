n,m = map(int,input().split())
A = list(map(int,input().split()))

ans = n - sum(A)
print(-1 if ans<0 else ans)