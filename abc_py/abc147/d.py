n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in range(n):
    for j in range(i,n):
        if i != j:
            ans += a[i] ^ a[j]
print(ans%1000000007)
