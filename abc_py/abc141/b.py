# 16:20 - 16:24
s = input()
for i in range(len(s)):
    if s[i] != 'U' and s[i] != 'D':
        if (i+1)%2 == 0 and s[i] == 'R':
            print("No")
            exit(0)
        if (i+1)%2 != 0 and s[i] == 'L':
            print("No")
            exit(0)
print("Yes")