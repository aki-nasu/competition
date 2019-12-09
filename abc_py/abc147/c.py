n = int(input())
a = list()
xy = list()
for i in range(n):
    a.append(int(input()))
    for j in range(a[i]):
        x1,y1 = map(int,input().split())
        xy.append([x1,y1])
true_man = 0
print(a)
print(xy)
