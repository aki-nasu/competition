##############
### 全探索 ###
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

def F(i,m):
    if m == 0:
        return True
    if i >= n:
        return False
    res = F(i+1,m) or F(i+1,m-A[i])
    return res

for i in range(q):
    if F(0,m[i]):
        print('yes')
    else:
        print('no')
ED = time.time()
print(ED-ST)

# 0.0009989738464355469
# 0.0009989738464355469
# 0.0019974708557128906