import collections
n = int(input())
S = [input() for _ in range(n)]
c = collections.Counter(S)
C = sorted(c.most_common(),key=lambda x: x[0])
C = sorted(C,key=lambda x: x[1], reverse=True)
t = C[0][1]
for i in range(len(C)):
    if C[i][1] == t:
        print(C[i][0])