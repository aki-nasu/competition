s = input()
for i in range(len(s)):
    cnt=0
    for j in range(len(s)):
        if s[i] == s[j]:
            cnt+= 1
    if cnt != 2:
        print("No")
        exit(0)
print("Yes")