# 20:42
n,k = map(int,input().split())
r,s,p = map(int,input().split())
t = input()
dic = {'r':p, 's':r, 'p':s}
t1 = ['']*n
score = 0
for i in range(k):
    score += dic[t[i]]
    t1[i] = t[i]
for i in range(k,n):
    if t[i] != t1[i-k]:
        score += dic[t[i]]
        t1[i] = t[i]
    else:
        t1[i] = 'x'
print(score)