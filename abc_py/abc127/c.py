n,m = map(int,input().split())
MIN = 0
MAX = 10**5
for i in range(m):
    l,r = map(int,input().split())
    MIN = MIN if MIN > l else l
    MAX = MAX if MAX < r else r
ans = (MAX-MIN+1) if MIN <= MAX else 0
print(ans)
# MIN > MAX となるケースの考慮漏れによりWA