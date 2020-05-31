n = int(input())
for i in range(0,26):
    for j in range(0,16):
        if 4*i+7*j==n:
            print('Yes')
            exit(0)
        if 4*i+7*j>n:
            break
print('No')