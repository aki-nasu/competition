n = int(input())
d = [True for i in range(200001)]
p = list(map(int,input().split()))
ans = []
num = 0
for i in range(n):
    d[p[i]] = False
    if d[num]:
        ans.append(num)
    else:
        for j in range(num,200001):
            if d[j]:
                num = j
                break
        ans.append(num)

for i in range(len(ans)):
    print(ans[i])
