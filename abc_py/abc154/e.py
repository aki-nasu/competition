S = input()
n = len(S)
K = int(input())

import numpy as np
dp = np.zeros((4,4,2),int)
dp[0][0][0] = 1

for i in range(n):
    for j in range(4):
        for k in range(2):
            nd = int(S[i])
            for d in range(10):
                ni,nj,nk = i+1,j,k
                if d != 0: nj +=1
                if nj > K: continue
                if(k==0):
                    if d > nd: continue
                    if d < nd: nk = 1
                dp[ni][nj][nk] += dp[i][j][k]
ans = dp[n][K][0] + dp[n][K][1]
print(dp[n][K])
print('=====')
print(dp)
print('=====')
print(ans)

