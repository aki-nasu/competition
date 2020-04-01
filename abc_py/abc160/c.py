k,n = map(int,input().split())
a = list(map(int,input().split()))

max_dist = 0
for i in range(n):
    next = (i+1) % n
    dist = a[next] - a[i]
    if dist < 0: dist+= k
    max_dist = max(max_dist, dist)
print(k - max_dist)