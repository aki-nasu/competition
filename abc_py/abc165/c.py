n,m,q = map(int,input().split())
tp = [tuple(map(int,input().split())) for _ in range(q)]
tp = sorted(tp, key=lambda x: x[3], reverse=True)

import numpy as np
# 0があり、1はなし
A = np.zeros((n,2),np.int32)
for i in range(n):
    A[i][0] = m+1
    A[i][1] = m+1
ans = 0
for i in range(q):
    a,b,c = tp[i][0]-1,tp[i][1]-1,tp[i][2]
    # j >= k
    flg = True
    for j in range(1,m+1):
        for k in range(1,j+1):
            if j - k == c:
                # 下限
                if flg:
                    A[b][0],A[a][0]=min(j,A[b][0]),min(k,A[a][0])
                    flg = False
                # 上限
                else:
                    A[b][1],A[a][1]=min(j,A[b][1]),min(k,A[a][0])
            
print(A)