import numpy as np
n,m,q = map(int,input().split())
point = [n]*(m+1)
point[0] = 0
score = np.zeros((n+1,m+1),dtype=np.int32)
ans = []
for _ in range(q):
    s = list(map(int,input().split()))
    if s[0] == 1:
        ans.append(sum(score[s[1]] * point))
    else:
        point[s[2]] -= 1
        score[s[1]][s[2]] = 1
for i in range(len(ans)):
    print(ans[i])