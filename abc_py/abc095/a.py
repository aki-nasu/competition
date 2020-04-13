s=input()
ans=700
for i in range(len(s)):
    ans += 100 if s[i]=='o' else 0
print(ans)