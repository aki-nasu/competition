h,w = map(int,input().split())

import numpy as np
dp = np.zeros((h,w),np.int32)
s = np.full((h,w),'.',np.str)
for H in range(h):
    S = input()
    for W in range(w):
        s[H][W] = S[W]
        own = s[H][W]
        if H==0 and W==0: dp[H][W] = 0 if own=='.' else 1
        elif H==0: dp[H][W] = dp[H][W-1]+1 if s[H][W-1]=='.' and own=='#' else dp[H][W-1]
        elif W==0: dp[H][W] = dp[H-1][W]+1 if s[H-1][W]=='.' and own=='#' else dp[H-1][W]
        else:
            dp[H][W] = min(dp[H][W-1], dp[H-1][W])
            if own=='#':
                if s[H][W-1]=='.' and s[H-1][W]=='.': dp[H][W] += 1
                elif s[H][W-1]=='#' and s[H-1][W]=='.': dp[H][W] = min(dp[H][W-1], dp[H-1][W]+1)
                elif s[H][W-1]=='.' and s[H-1][W]=='#': dp[H][W] = min(dp[H][W-1]+1, dp[H-1][W])
print(dp[h-1,w-1])