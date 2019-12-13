# 15:09 giveup
n = int(input())

sp = []
for i in range(n):
    s,p = input().split()
    sp.append((s,-int(p),i+1))
sp.sort()
for s,p,i in sp:
    print(i)