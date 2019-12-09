# 2019/12/7 14[m] 0WA
# if文の条件を複数行に渡って記述する方法を調べるのにほとんどの時間を掛けた。
n = int(input())
p = list(map(int,input().split()))
ans = 0
for i in range(1,n-1):
    if (p[i-1] < p[i] and p[i] < p[i+1]) \
        or (p[i-1] > p[i] and p[i] > p[i+1]):
        ans += 1
print(ans)