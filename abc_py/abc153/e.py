# give up
h,n = map(int,input().split())
l = []
for i in range(n):
    a,b = map(int,input().split())
    l.append((a,b,b/a))
l = sorted(l,key=lambda l: l[0],reverse=True)
l = sorted(l,key=lambda l: l[2])
ans = 0
atk = l[0][0]
mp = l[0][1]
print(l)
while True:
    if h >= atk:
        h -= atk
        ans += mp
    else:
        break
atk_t = atk
mp_t = 0
for i in range(1,n):
    if atk_t <= l[i][0]:
        continue
    if h <= l[i][0]:
        mp_t = l[i][0]
    r = h % l[i][0]
    mp_t += (h // l[i][0]) * l[i][1]
    if r == 0:
        break
    else:
        atk_t = r
if mp_t < mp:
    ans += mp_t
else:
    ans += mp
print(ans)
        