import math
n,d = map(int,input().split())
count = 0
xy = []
for i in range(n):
    x,y = map(int,input().split())
    if (x,y) in xy: continue
    xy.append((x,y))
    count+= 1 if math.sqrt(pow(x,2)+pow(y,2)) <= 5 else 0
print(count)
# incomplete