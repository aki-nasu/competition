k = int(input())+1
ans = 0
for i in range(1,k):
    for j in range(i+1,k):
        if i%2==0: ans += 1 if j%2!=0 else 0
        else: ans += 0 if j%2!=0 else 1
print(ans)