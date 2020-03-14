n = int(input())
t,a = map(int,input().split())
h = list(map(int,input().split()))
p = -1
for i in range(n):
    q = t-(h[i]*0.006)
    if p == -1 or p > abs(a-q):
        p = abs(a-q)
        ans = i+1
print(ans)