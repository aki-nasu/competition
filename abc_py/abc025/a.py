s = input()
n = int(input())
count = 0
for i in range(len(s)):
    S = s[i]
    for j in range(len(s)):
        T = s[j]
        count += 1
        if count == n:
            print(S + T)
            exit(0)