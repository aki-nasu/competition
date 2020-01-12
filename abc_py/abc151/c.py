n,m = map(int,input().split())
ac = [0]*n
wa = [0]*n
for i in range(m):
    p,s = input().split()
    p = int(p)
    if ac[p-1]:
        continue
    if s == 'AC':
        ac[p-1] = 1
    else:
        wa[p-1] += 1
count_ac = 0
count_wa = 0
for i in range(n):
    count_ac += ac[i]
    if ac[i]:
        count_wa += wa[i]
print(str(count_ac) + " " + str(count_wa))