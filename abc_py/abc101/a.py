s=input()
d={'+':1,'-':-1}

ans=0
for i in range(len(s)):
    ans+=d[s[i]]
print(ans)