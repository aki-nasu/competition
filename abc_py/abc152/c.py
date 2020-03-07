n = int(input())
p = list(map(int,input().split()))
count = 0
MIN = p[0]
for i in range(n):
    if p[i] <= MIN:
        count += 1
        MIN = p[i]
        if MIN == 1:
            break
print(count)