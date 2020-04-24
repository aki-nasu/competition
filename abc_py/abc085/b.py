n = int(input())
d = []
for _ in range(n):
    d.append(int(input()))
count_0 = 1
d = sorted(d)
for i in range(n):
    if i == n-1: break
    if d[i] == d[i+1]: continue
    count_0 += 1

d = sorted(d,reverse=True)
count_1 = 1
for i in range(n):
    if i == n-1: break
    if d[i] == d[i+1]: continue
    count_1 += 1
print(max(count_0,count_1))