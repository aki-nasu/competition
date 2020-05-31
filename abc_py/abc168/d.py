# 解けてません
n,m = map(int,input().split())
AB = []
ans = [-1]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    a,b = min(a,b),max(a,b)
    AB.append(tuple((a,b)))
AB = sorted(AB)
# [(1, 5), (1, 6), (2, 4), (2, 6), (3, 4), (3, 5), (4, 5), (4, 6), (5, 6)]

goal = []
for i in range(m):
    if AB[i][0] == 1:
        ans[AB[i][1]] = 1
        goal.append(AB[i][1])
    else:
        break
if len(goal) == 0: exit(print('No'))

# [(0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (1, 0), (1, 0)]


    


print(ans)
