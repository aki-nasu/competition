##############
###   DP   ###
##############

import time
ST = time.time()
# n = int(input())
# A = list(map(int,input().split()))
# q = int(input())
# m = list(map(int,input().split()))
n = 5
A = [1,5,7,10,21]
q = 4
m = [2,4,17,8]
import numpy as np
dp = np.full((6,100),9)

# 1==True,0==False,9==未計算
def F(i,m):
    # print(i,m)
    if dp[i][m] != 9:
        return dp[i][m]
    if m == 0:
        dp[i][m] = 1
    elif i >= n:
        dp[i][m] = 0
    elif F(i+1,m):
        dp[i][m] = 1
    elif F(i+1,m-A[i]):
        dp[i][m] = 1
    else:
        dp[i][m] = 0
    return dp[i][m]

for i in range(q):
    judge = F(0,m[i])
    if judge:
        print('yes')
    else:
        print('no')
ED = time.time()
print(ED-ST)


# 0.0009989738464355469
# 0.0009989738464355469
# 0.0019974708557128906

