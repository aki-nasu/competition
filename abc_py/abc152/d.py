n = int(input())
count = 0
l = []
c = []
for i in range(1,n+1):
    if i % 10 == 0:
        continue
    s = str(i)
    num = int(s[-1] + s[0])
    if num in l:
        print(num)
        c[l.index(num)] += 1
    else:
        l.append(num)
        c.append(1)
print(l)
print(c)
print(sum(c))
