def F(p,q,r):
    ret = 0
    for i in range(len(p)):
        pq = [q[t] for t in range(len(q)) if p[i]<q[t]]
        for j in range(len(pq)):
            pr = [r[t] for t in range(len(r)) if pq[j]<r[t]]
            for k in range(len(pr)):
                if not (2*pq[j]==p[i]+pr[k]): ret += 1
    return ret

n,s = int(input()),input()
ans = 0
R = []
G = []
B = []
for i in range(n):
    if s[i]=='R': R.append(i)
    if s[i]=='G': G.append(i)
    if s[i]=='B': B.append(i)
ans += F(R,G,B)
ans += F(R,B,G)
ans += F(G,B,R)
ans += F(G,R,B)
ans += F(B,G,R)
ans += F(B,R,G)
print(ans)