# give up
import math
n = int(input())
x = list(map(int,input().split()))

ans = 0
i = 1
while True:
    for k in range(n-i):
        ans += (1/(n-i)) * (x[k+i]-x[k])
    i += 1
    if i == (n-1):
        break
    else:
        ans += ans
for k in range(n-1):
    ans +=  (x[n-1] - x[k])/2

ans = (ans * math.factorial(n-1)) % 1000000007
print(ans)