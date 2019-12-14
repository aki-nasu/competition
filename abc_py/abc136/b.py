# 20m over
n = int(input())
ans = 0
for i in range(n):
    ans += 1 if len(str(i+1))%2 == 1 else 0
print(ans)