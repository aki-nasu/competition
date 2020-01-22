n,k = map(int,input().split())

import math
# i*(2^x) >= k を満たす x を求める
ans = 0
for i in range(1,n+1):
    x = -(-math.log2(-(-k//i))//1)
    ans += 0.5**x
print(ans/n)
# print(f'{ans:.10f}')
# print('{:.9f}'.format(ans))