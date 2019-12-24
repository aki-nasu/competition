# 21:19 - 22:06
from collections import deque
n = int(input())
a = deque(list(map(int,input().split())))
ans = 0
count = 1
i = 0
while True:
    if a[i] != count:
        ans += 1
        a.popleft()
    else:
        count += 1
        i += 1
    if n == ans + i:
        break
if len(a) == 0:
    print(-1)
else:
    print(ans)


# for i in range(n-1):
#     if a[i] != count:
#         ans += 1
#     else:
#         count += 1
