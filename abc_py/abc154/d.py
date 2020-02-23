n,k = map(int,input().split())
p = list(map(int,input().split()))

t = [0]*n
for j in range(k):
    t[0] += p[j]
for i in range(1,n-k+1):
    t[i] = t[i-1]-p[i-1]+p[i+k-1]
T = t.index(max(t))
ans = 0
for i in range(k):
    ans += (p[T+i]+1)/2
print(ans)