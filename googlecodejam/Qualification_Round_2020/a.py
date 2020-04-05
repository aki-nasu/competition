t = int(input())
message = []
import numpy as np
for i in range(t):
    n = int(input())
    m = np.array([list(map(int,input().split())) for _ in range(n)],np.int32)
    r = 0
    c = 0
    for j in range(n):
        r += 0 if len(m[j]) == len(set(m[j])) else 1
        c += 0 if len(m[:,j]) == len(set(m[:,j])) else 1
    k = sum(np.diag(m))
    message.append('Case #' + str(i+1) + ': ' + str(k) + ' ' +  str(r) + ' ' + str(c))

for i in range(t):
    print(message[i])