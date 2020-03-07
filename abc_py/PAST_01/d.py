n = int(input())
m = [0]*n
l = [0]*n
for i in range(n):
    m[i] = i+1
    l[i] = int(input())
l.sort()
print(l)
print(m)
if l==m:
    print('Correct')
    exit(0)
bottom = 0
top = n
while True:
    t = (bottom + (top - bottom)) // 2
    if m[t] == l[t]:
        bottom = t
    else:
        top = t
