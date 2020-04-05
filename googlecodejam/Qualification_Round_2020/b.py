t = int(input())
ans = []
for _ in range(t):
    ans.append((input().replace('1','(1)').replace(')(','')))
for i in range(t):
    print('Case #' + str(i+1) + ': ' + ans[i])